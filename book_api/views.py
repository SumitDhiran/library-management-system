from django.shortcuts import render

from .serializers import Book
from book_api.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializers = BookSerializer(books,many=True)
        return Response(serializers.data)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_book(request):
    if request.method == 'POST':
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def book(request,pk):
    try:
        book = Book.objects.get(id=pk)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = BookSerializer(book)
        return Response(serializers.data)


@api_view(['PUT'])
def update_book(request,pk):
    try:
        book = Book.objects.get(id=pk)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializers = BookSerializer(book,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_book(request,pk):
    try:
        book = Book.objects.get(id=pk)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)