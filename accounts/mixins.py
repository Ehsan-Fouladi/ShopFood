from django.shortcuts import redirect

class AuthenticatedMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

class AnonymousMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect("account:login")
        return super().dispatch(request, *args, **kwargs)