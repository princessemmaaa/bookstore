from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from books import views as books_views  # new import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', books_views.register_request, name='register'),  # moved here
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='books/password_change.html'), name='password_change'),  # moved here
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='books/password_change_done.html'), name='password_change_done'),  # moved here
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='books/password_reset.html'), name='password_reset'),  # moved here
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='books/password_reset_done.html'), name='password_reset_done'),  # moved here
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='books/password_reset_confirm.html'), name='password_reset_confirm'),  # moved here
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='books/password_reset_complete.html'), name='password_reset_complete'),  # moved here
    # add more paths for other apps if needed...
]
