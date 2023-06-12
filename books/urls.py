from django.urls import path
from . import views

app_name = "books"  # URL namespace for the books app
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:id>/', views.book_detail, name='book_detail'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:id>/', views.profile_detail, name='profile_detail'),
    path('profile/', views.profile, name='profile'),
    path('<int:id>/edit/', views.book_edit, name='book_edit'),
    path('<int:id>/delete/', views.book_delete, name='book_delete'),
    path('edit/', views.edit, name='edit'),
    path('profile/edit/done/', views.profile_edit_done, name='profile_edit_done'),
    path('edit/complete/', views.profile_edit_complete, name='profile_edit_complete'),

    # add more paths for other views if needed...
]
