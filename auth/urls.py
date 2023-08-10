from django.urls import path
from auth import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "account"
urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
]