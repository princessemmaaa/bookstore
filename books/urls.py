from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # add more paths for other authentication views if needed...
]