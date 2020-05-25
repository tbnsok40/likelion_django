from django.shortcuts import render, redirect
# from .forms import JssForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        regiform = UserCreationForm(request.POST)
        # request.POST 안에 담긴 정보들을 UserCreationFrom에 담고,
        if regiform.is_valid():
            regiform.save()
            return redirect('index')
        else:
            #유효하지 않으면
            return redirect('register')
            #다시 register page로 보내라
    
    # GET방식으로 요청이 들어올 때
    registerform = UserCreationForm
    return render(request, 'registration/register.html', {'registerform': registerform})

# app등록이 안돼있어서 철자 다 맞아도 오류가 났다.