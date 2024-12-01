from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View

class RegisterView(View):  
    template_name = 'users/register.html'
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect after successful registration
        return render(request, self.template_name, {'form': form})

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = ''

class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = 'login'
