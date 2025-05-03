from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Optional: log them in after signup
            return redirect('shop:product_list')  # Or wherever you want
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})