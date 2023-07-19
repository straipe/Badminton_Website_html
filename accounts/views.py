from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입이 되었습니다.")
            #signed_user.send_welcome_email() # FIXME: Celery 처리
            next_url=request.GET.get('next','/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form':form,
    })
