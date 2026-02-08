from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method=='POST':
          u_form = UserUpdateForm(request.POST,instance=request.user)
          f_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
          if u_form.is_valid() and f_form.is_valid():
              u_form.save()
              f_form.save()
              messages.success(request,'Updated Successfully')
              return redirect('profile')
          
    else:
        u_form = UserUpdateForm(instance=request.user)
        f_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'f_form': f_form
    }
    return render(request, 'users/profile.html', context)
