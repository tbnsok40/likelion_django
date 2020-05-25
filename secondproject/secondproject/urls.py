from django.contrib import admin
from django.urls import path
from blog.views import home, detail # def home 을 선언해뒀으니 import한다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/<int:blog_id>/', detail, name = 'detail') # templates가 define되지 않았다는 에러는, templates파일이 제 형식에 맞게 뜨도록 고쳐주어야한다.
]
