from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignupView, SigninView, ResetPasswordView, ChangePasswordView, profile

from .forms import LoginForm

app_name = "account"
urlpatterns = [
    path('register/', SignupView.as_view(), name='signup'),
    path('login/', SigninView.as_view(redirect_authenticated_user=True, template_name='user/login.html', authentication_form=LoginForm), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='signout'),
    path('profile/', profile, name='profile'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]
