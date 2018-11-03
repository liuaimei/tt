from django.db import models
from  tinymce.models import HTMLField
# Create your models here.

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)


    def __str__(self):
        return  self.ttitle.encode("utf-8")

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)  #名字
    gpic = models.ImageField(upload_to="df_goods") #上传图片
    gprice = models.DecimalField(max_digits=5,decimal_places=2)  #价格  max_digits最大金额,decimal_places最大小数
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default='500g')  #单位
    gclick = models.IntegerField()  #点击率，“人气”
    gjianjie = models.CharField(max_length=200)  #商品的简介
    gkucun = models.IntegerField()
    gcontent = HTMLField()  #fuwenbenbianjiqi
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE)

    def __str__(self):
        return  self.gtitle.encode("utf-8")


