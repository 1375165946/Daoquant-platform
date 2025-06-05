from django.db import models


# Create your models here.
class User(models.Model):
    usernumber = models.CharField(max_length=20, unique=True)  # 账号
    password = models.CharField(max_length=128)  # 密码
    name = models.CharField(max_length=50)  # 姓名

    def __str__(self):
        return f"{self.name} ({self.usernumber})"
