from django.urls import path
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    # path('register/',views.create_user,name='register'),
    # path('books/',views.GetUser.as_view(),name='books'),
    path('books_search/',views.SearchUserView.as_view(),name='search_books'),
        # path('books/<int:pk>/', views.BookDestroyAPIView.as_view(), name='book_delete'),
    path('product-categories',views.ProductCategoriesView.as_view(),name='product-categories')

]


            