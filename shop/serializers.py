from django.contrib.auth.models import User
from .models import BookNew,ProductCategories
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookNewSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookNew
        fields = '__all__'


class ProductCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCategories
        fields = '__all__'
       

