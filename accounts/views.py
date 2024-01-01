from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView, UpdateView, DetailView
from .forms import LoginForm, RegisterForm, ProfileForm, PasswordChangeForm
from .models import User
from django.contrib.auth.views import PasswordChangeView
from .mixins import AuthenticatedMixin, AnonymousMixin
from django.contrib.auth.decorators import login_required

# Login user
class LoginView(AuthenticatedMixin, FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(self.request, username=cd['email'] , password=cd['password'])
        if user is not None:
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(self.request, 'شما با موفقیت وارد سایت شدید')
            return redirect(reverse_lazy('home:home'))
        else:
            form.add_error("email", "اطلاعات شما نادرست است؟")
            return render(self.request, "accounts/login.html", {"form": form})

# Register user
class RegisterView(AuthenticatedMixin, FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account:panel')

    def form_valid(self, form):
        if self.request.user.is_authenticated == True:
            messages.error(self.request, "شما قبلا ثبت نام کرده اید")
            return redirect(reverse_lazy('home:home'))
        else:
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password1'])
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(self.request, 'شما با موفقیت ثبت نام کرده اید')
            return redirect('account:panel', self.request.user.pk)

# panel
class PanelView(AnonymousMixin, DetailView):
    template_name = "accounts/panel.html"

    def get_queryset(self):
        if self.request.user.is_admin:
            superusers = User.objects.all()
            return superusers
        else:
            superuser = User.objects.filter(email=self.request.user)
            return superuser

# profile
class ProfileView(AnonymousMixin, UpdateView):
    template_name = "accounts/profile.html"
    model = User
    form_class = ProfileForm

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_success_url(self):
        pk = self.request.user.pk
        messages.success(self.request, "پروفایل شما بروزرسانی شد.")
        return format(reverse('account:panel', kwargs={'pk': pk}))

@login_required(login_url="account:login")
def LogoutView(request):
    logout(request)
    messages.success(request, "شما خارج شدید از سایت")
    return redirect("home:home")

# password change
class PasswordChangeView(AnonymousMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("account:password_change_done")