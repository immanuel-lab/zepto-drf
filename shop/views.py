
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
import os
from dotenv import load_dotenv
from . import models
from . import serializers
from rest_framework import generics,filters


# @api_view(['POST'])
# def create_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             load_dotenv()
#             username = os.environ['DJANGO_SUPERUSER_USERNAME']
#             message = f"User created successfully. Superuser username: {username}"
#             return Response({'message':message,'data':serializer.data}, status=status.HTTP_201_CREATED)
         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class GetUser(generics.ListAPIView):
#      queryset = models.BookNew.objects.all()
#      serializer_class = serializers.BookNewSerializer


# class GetUser(generics.ListCreateAPIView):
#      queryset = models.BookNew.objects.all()
#      serializer_class = serializers.BookNewSerializer

# class BookDestroyAPIView(generics.DestroyAPIView):
#      queryset = models.BookNew.objects.all()
#      serializer_class = serializers.BookNewSerializer


class SearchUserView(generics.ListAPIView):
    queryset = models.BookNew.objects.all()
    serializer_class = serializers.BookNewSerializer
    filter_backends=[filters.SearchFilter]
   
    # search_fields=['^name']
    # search_fields=['=name']


# product =models.Product.objects.get(pk=2)
# print(product.total_price) 

from rest_framework.pagination import PageNumberPagination
class ProductCategoriesPagination(PageNumberPagination):
    page_size = 5
   

class ProductCategoriesView(generics.ListAPIView):
    queryset=models.ProductCategories.objects.all()
    serializer_class=serializers.ProductCategoriesSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['category_name']
    pagination_class = ProductCategoriesPagination
   
   