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