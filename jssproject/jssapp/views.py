from django.shortcuts import render, redirect
from .models import Jasosul, Comment
from .forms import JssForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    all_jss = Jasosul.objects.all()  # Jasosul의 object를 다 가져와라 => all_jss에 할당
    return render(request, 'index.html', {'all_jss': all_jss})

@login_required #decorator, 로그인이 필요하다-> 로그인을 유도하게 돼있다.
def create(request):
    if request.method == 'POST':
        print(request.POST, request.FILES)
        myform = JssForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('index')
    myform = JssForm()
    return render(request, 'create.html',{'myform':myform})

    # render 와 redirect의 차이, url요청만 한다(redirect) <=> render는 보낼게 많아 사전이라던가 등등.

def detail(request, jss_id):
    # my_jss = Jasosul.objects.get(pk=jss_id)
    try:
        my_jss = Jasosul.objects.get(pk=jss_id)
    except:
        raise Http404

    temp_comment_form = CommentForm()
    context = {'comment_form':temp_comment_form, 'my_jss':my_jss}
    return render(request, "detail.html", context)

@login_required #decorator, 로그인이 돼 있어야 삭제할수있도록 권한부여를 한다.
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

def comment_create(request, jss_id):
    # myform = CommentForm()

    if request.method == 'POST':
        # print(request.POST, request.FILES)
        myform = CommentForm(request.POST) # 댓글 form안에 넘어오는 request값을 담아준다.
 
        if myform.is_valid(): # 유효성 검사
            
            temp_form = myform.save(commit=False) # 잠시 저장을 멈추고 기다려라.
            # myform.post = jss_id # 댓글이 달릴 글의 id는 넘어오는 jss_id로 해주자
            temp_form.post = Jasosul.objects.get(pk=jss_id) # 넘어오는 id와 일치하는 글을 불러와서
            # 해당 글을 댓글의 주인글로 설정해주겠다.
            temp_form.save() # 찐 저장
            return redirect('detail',jss_id)

    return render(request, 'detail.html', {'comment_form':myform})
