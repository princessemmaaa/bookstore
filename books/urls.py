from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "books"  # URL namespace for the books app
urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:id>/', views.profile_detail, name='profile_detail'),
    path('register/', views.register_request, name='register'),  # added comma here
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='books/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='books/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='books/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='books/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='books/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='books/password_reset_complete.html'), name='password_reset_complete'),
    # add more paths for other authentication views if needed...
]
