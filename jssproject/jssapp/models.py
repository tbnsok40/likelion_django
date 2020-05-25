from django.db import models

# Create your models here.

# 얘는 틀일 뿐이다.
# 클래스로 인해 생성된 내용들이 object라고 한다.
class Jasosul(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now = True)
# 클래스 안의 함수를 메서드라 한다.
    def __str__(self):
        return self.title
