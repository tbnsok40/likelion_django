"""jssproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from jssapp.views import index, create, detail, delete, update, comment_create
from accounts.views import register
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings # setting안에 있는거 가져오기
from django.conf.urls.static import static # static처럼 url제공하고 싶다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:jss_id>/', detail, name='detail'), # jss_id는 그냥 너가원하는대로 선언해도 된다.
    path('delete/<int:jss_id>/', delete, name = 'delete'),
    path('update/<int:jss_id>/', update, name = 'update'),
    path('accounts/', include('accounts.urls')),
    path('comment_create/<int:jss_id>', comment_create, name='comment_create'),
    # accounts 앱에 url을 옮겨주는 이유. 관리성의 효율, 편의성. 유지보수를 위함.
    # 그말인즉슨, 여기다 모두 url을  써도 동작은 한다. 
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

