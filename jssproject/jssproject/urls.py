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
from django.urls import path
from jssapp.views import index, create, detail, delete, update
from accounts.views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:jss_id>', detail, name='detail'), # jss_id는 그냥 너가원하는대로 선언해도 된다.
    path('delete/<int:jss_id>', delete, name = 'delete'),
    path('update/<int:jss_id>', update, name = 'update'),
    path('register/', register, name='register'),
    # path('login/', LoginView.as_view, name='login'),
    path('login/', LoginView.as_view(), name='login'), #괄호가 빠져서 오류생겼었따, + 똑같은 문장 위에 하나 더 있어서,,,, 눈치좀 채지 그랬어 ㅠ
    path('logout/', LogoutView.as_view(), name='logout'),
]

