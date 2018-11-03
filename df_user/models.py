from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  #用户名
    upwd = models.CharField(max_length=40)  #用户密码
    uemail = models.CharField(max_length=30) #邮箱
    ushou = models.CharField(max_length=20,default='') #收货地址
    uaddress = models.CharField(max_length=100,default='') #收获地址
    uyoubian = models.CharField(max_length=6,default='') #邮编
    uphone = models.CharField(max_length=11,default='') #手机号


#设置default的时候不需要迁移，因为他是在python层面更改的，约束，不影响数据库 blank也不需要迁移
#设置null的时候就要从新迁移了，因为他影响到数据库层面了