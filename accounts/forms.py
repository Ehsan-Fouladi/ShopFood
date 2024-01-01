from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", "username"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "username", "is_active", "is_admin"]

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-constraints':'@Required'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'data-constraints':'@Required'}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-constraints':'@Required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-constraints':'@Required @Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'data-constraints':'@Required'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'data-constraints':'@Required'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("کاربر با این ایمیل در سایت وجود دارد.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("گذرواژه یکسان نمی باشد لطف دوباره تلاش کنید.")
        return password2

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "image"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "md:w-72 h-full bg-gray-600 outline-none rounded-md px-2 py-1 mt-2 text-white focus:ring-2 focus:ring-purple-600 focus:ring-inset", "id":"username"}),
            "email": forms.EmailInput(attrs={"class": "md:w-72 h-full bg-gray-600 outline-none rounded-md px-2 py-1 mt-2 text-white focus:ring-2 focus:ring-purple-600 focus:ring-inset", "id":"email"}),
            "image": forms.FileInput(attrs={"class": "inputs block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400", "id":"file_input", "name":"file"}),
        }

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError("گذرواژه فعلی تان اشتباه وارد شد. لطفا دوباره تلاش کنید")
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("گذرواژه ها یکسان نمی باشد لطف دوباره سعی کنید؟")
        return password2