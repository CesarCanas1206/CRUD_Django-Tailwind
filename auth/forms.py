from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class LoginForm(AuthenticationForm):

    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'username',
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none px-[15px] text-[#212121] text-[16px]',
    }))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'data-toggle': 'password',
        'id': 'password',
        'name': 'password',
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none outline-none px-[15px] text-[#212121] text-[16px]',
    }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class RegisterForm(UserCreationForm):

    username = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none outline-none px-[15px] text-[#212121] text-[16px]',
    }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none outline-none px-[15px] text-[#212121] text-[16px]',
    }))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'data-toggle': 'password',
        'id': 'password',
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none outline-none px-[15px] text-[#212121] text-[16px]',
    }))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'data-toggle': 'password',
        'id': 'password',
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none outline-none px-[15px] text-[#212121] text-[16px]',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):

    username = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none outline-none px-[15px] text-[#212121] text-[16px]',
    }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none outline-none px-[15px] text-[#212121] text-[16px]',
    }))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none outline-none px-[15px] text-[#212121] text-[16px]'
    }))
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full h-[48px] border border-[#CCCCCC] rounded-[8px] bg-transparent focus:outline-none outline-none px-[15px] text-[#212121] text-[16px]',
        'rows': 5
    }))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
