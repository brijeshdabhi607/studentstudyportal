from django.shortcuts import render, redirect
from .accountform import CustomUserCreationForm , CustomLoginForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,level=messages.SUCCESS,message="user created successfully")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request,"registration/register.html",{'form':form})


