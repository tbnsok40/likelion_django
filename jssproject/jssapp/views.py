from django.shortcuts import render, redirect
from .models import Jasosul

# Create your views here.
def index(request):
    all_jss = Jasosul.objects.all()  # Jasosul의 object를 다 가져와라 => all_jss에 할당
    return render(request, 'index.html', {'all_jss': all_jss})

def create(request):
    if request.method == 'POST':
        print(request.POST)
        myform = JssForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('index')
    myform = JssForm()
    return render(request, 'create.html',{'myform':myform})

    # render 와 redirect의 차이, url요청만 한다(redirect) <=> render는 보낼게 많아 사전이라던가 등등.

def detail(request, jss_id):
    my_jss = Jasosul.objects.get(pk=jss_id)
    return render(request, "detail.html", {'my_jss':my_jss} )

def delete(request, jss_id):
    my_jss = Jasosul.objects.get(pk=jss_id)
    my_jss.delete()
    
    return redirect('index') # index page로 redirect해준다.

def update(request, jss_id):
    my_jss = Jasosul.objects.get(pk=jss_id)
    if request.method == 'POST':
        update_form = JssForm(request.POST, instance=my_jss) # instance == objects 비슷
        if update_form.is_valid():
            update_form.save()
            return redirect('index')
    update_form = JssForm(instance=my_jss) # 기존의 내용들을 update할 때 그대로 불러들여온다.


    return render(request, 'update.html', {'update_form':update_form})