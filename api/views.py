from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import BookSerializer
from app.models import Book




@api_view(['GET'])
def get_data(request):
    books = Book.objects.all()
    serialzed_data = BookSerializer(books, many=True)

    return Response(serialzed_data.data)



@api_view(['POST'])
def post_data(request):
    serialzed_data = BookSerializer(data = request.data)
    if serialzed_data.is_valid():
        serialzed_data.save()
        return Response(serialzed_data.data)
    return Response(serialzed_data.errors,status=400)


# ALL the CRUD in one function

@api_view(['GET','PUT','DELETE'])
def books_detailes(request,pk):
    book = Book.objects.get(pk=pk)

    if request.method =="GET" :
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    
    elif request.method =='PUT':
        serializer = BookSerializer(book,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method =='DELETE':
        book.delete()
        return Response(status=204)
    


    