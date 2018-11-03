coding="utf-8"
from django.shortcuts import render,redirect
from  .models import  *
from goods.models import  *
from  hashlib import  sha1
from  django.http import  JsonResponse,HttpResponse,HttpResponseRedirect
# Create your views here.




#写一个装饰器判断用户是否登录
# def login(func):
#     def login_func(request,*args,**kwargs):
#          if request.session.has_key('user_id'):
#              return  func(request,*args,**kwargs)
#          else:
#                 red = HttpResponseRedirect("/login/")
#                 red.set_cookie('url',request.get_full_path())
#                 return  red
#     return login_func
#注册
def register(request):
    return  render(request,'register.html')

#处理注册
def register_handle(request):
    #1.1 接收用户输入
    post = request.POST
    # 1.2 获取post提交的数据
    uname = post.get("user_name")
    upwd = post.get("pwd")
    upwd2 = post.get("cpwd")
    uemail = post.get("email")


    # 2 判断两次密码
    if  upwd != upwd2:
        return  redirect('/register/')

    # #3 密码加密
    # s1 = sha1()  #先构造这个对象
    # s1.update(upwd) # 接收upwd这个参数然后加密
    # upwd3 = s1.hexdigest() #获取加密后的密码


    # 3.1 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uemail = uemail
    user.save()  #存入数据中

    #4 注册成功转入登录页面
    return  redirect('/index/')

#注册的时候判断用户是否已经存在
def register_exist(request):
    uname = request.GET.get("username")
    count = UserInfo.objects.filter(uname=uname).count()
    return  JsonResponse({"count":count})
#
def login(request):
        uname = request.COOKIES.get("uname",'')
        context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
        return  render(request,'login.html',context)

def login_handle(request):
#接收请求信息
    uname = request.POST.get("username")
    upwd = request.POST.get("pwd")
    #根据用户名查询对象
    user = UserInfo.objects.filter(uname=uname,upwd=upwd).first()
    if user:
        request.session["user_id"] = user.id
        request.session['user_name'] = uname
        return redirect('/user_center_info/')
    else:
        return redirect('/login/')

def user_center_info(request):
    user = UserInfo.objects.get(id=request.session["user_id"])
    if user:
        return  render(request,'user_center_info.html',{"user_email":user.uemail,
                                                        "user_name": request.session['user_name'],
                                                   "user_address": user.uaddress})
    else:
        return  render(request,'login.html')

#订单
def  user_center_order(request):
    user = UserInfo.objects.get(id=request.session["user_id"])
    if user:
        return  render(request,'user_center_order.html')

#收获地址
def user_center_site(request):
    user = UserInfo.objects.filter(id=request.session['user_id']).first()
    if request.method =="POST":
        user.uname = request.POST.get("uname")
        user.uaddress = request.POST.get("uaddress")
        user.uyoubian = request.POST.get("uyoubian")
        user.uphone = request.POST.get("uphone")
        user.save()
    return  render(request,'user_center_site.html',{ "uname":user.uname,
                                                     "uaddress": user.uaddress,
                                                     "uyoubian": user.uyoubian,
                                                     "uphone": user.uphone})

def index(request):
    return  render(request,"index.html")

def cart(request):
    return  render(request,'cart.html')

def place_order(request):
    return  render(request,'place_order.html')

def list(request):
    return  render(request,'list.html')

def detail(request,id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick+1
    goods.save()
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {"title":goods.gtype.ttitle,"guest_cart":1,
               'g':goods,"news":news,'id':id}
    return  render(request,'detail.html',context)




