from django.urls import path
from .import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('booklist', views.PublicView.as_view(), name='booklist'),
    path('books', views.BookCreate.as_view(), name='booklist'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='bookDetail'),
    path('register/',views.Register.as_view(),name = "register"),
    path('login/',obtain_auth_token,name ="login"),
]