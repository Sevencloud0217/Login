from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from bokeson.models import *

def loginVaild(fun):
    def inner(request,*arge,**kwargs):
        username = request.COOKIES.get('username')
        username_session=request.session.get('username')
        print(username_session)
        if username:
            return fun(request,*arge,**kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return inner
@loginVaild
def about(request):
    return render(request,'about.html')
@loginVaild
def index(request):
    #获取cookie 获取用户名
    # username= request.COOKIES.get('username')
    # print(request.COOKIES)
    # print(username)
    # if username:
    #来源
    url = request.META.get('HTTP_REFERER')
    print(url)

    article = Article.objects.order_by('-date')[:6]
    recommend_acticle=Article.objects.order_by('-date').all()[:7]

    click_article=Article.objects.order_by('-click')[:12]

    # else:
    #     return HttpResponseRedirect('/login/')
    return render(request, 'index.html', locals())
def listpic(request):
    return render(request,'listpic.html')


def newslistpic(request,type,page=1):
    page=int(page)
    # article=Article.objects.order_by('-date')
    article = Type.objects.get(name=type).article_set.order_by("-date")

    paginator = Paginator(article,6)#每页6个
    page_obj = paginator.page(page)

    #获取当前页
    current_page = page_obj.number
    start = current_page - 3
    if start < 1:
        start=0
    end = current_page + 2
    if end > paginator.num_pages:
        end = paginator.num_pages
    if start == 0:
        end = 5
    if end == 17:
        start=12
    page_range = paginator.page_range[start:end]
    return render(request,'newslistpic.html',locals())

def base(request):
    return render(request,'base.html')

def addariticle(request):
    # for x in range(100):
    #     article=Article()
    #     article.title='title_%s'%x
    #     article.content='content_%s'%x
    #     article.description='description_%s'%x
    #     article.auther=Article.objects.first()
    #     article.save()
    #     article.type.add(Type.objects.first())
    #     article.save()
    return HttpResponse('增加数据')

def xiangxi(request,id):
    article=Article.objects.get(id=int(id))
    return render(request,'xiangxi.html',locals())


from django.core.paginator import Paginator
def fytest(request):
    article=Article.objects.all().order_by("-date")
    # print(article)
    #每次显示 5条数据
    paginator =Paginator(article,5)#设置每一页显示多少条数据
    # print(paginator.count)#返回内容的总条数
    # print(paginator.page_range)#可迭代内容的总条数
    # print(paginator.num_pages)#最大页数
    # page_obj=paginator.page(2)
    # print(page_obj)
    # for one in page_obj:
    #     print(one.content)
    # print(page_obj.number)#当前的页数
    # print(page_obj.has_next())#有没有下一页
    # print(page_obj.has_previous())#有没有上一页
    # print(page_obj.next_page_number())#返回下一页的页码
    # print(page_obj.previous_page_number())#返回上一页

    return HttpResponse('分页管理')
def reqtest(request):
    ##获取get请求传递的参数
    # data=request.GET
    #获取post的请求参数
    data = request.POST
    print(data)
    print(data.get('name'))
    print(type(data.get('name')))
    print(data.get("age"))

    return HttpResponse("姓名：%s年龄:%s"%(data.get("name"),data.get('age')))

    # print(dir(request))

    # print(request.COOKIES)

    # print(request.FILES)
    # print(request.GET)

    # print(request.POST)

    # print(request.scheme)

    # print(request.method)

    # print(request.path)
    #
    # print(request.body)

    # meta=request.META
    # print(meta)
    # for key in meta:
    #     print(key)
    # print('*******')
    # print(request.META.get('OS'))
    # print(request.META.get('HTTP_USER_AGENT'))
    # print(request.META.get('HTTP_HOST'))
    # print(request.META.get('HTTP_REFERE'))

    # return HttpResponse('请求测试')

def fromtest(request):
    #get请求
    data=request.GET
    serach=data.get('serach',"")
    print(serach)
    #通过from提交的数据
    #通过模型查询
    article=Article.objects.filter(title__contains=serach).all()
    print(article)

    print(request.method)
    data=request.POST
    print(data.get('username'))
    print(data.get('password'))

    return render(request,"fromtest.html",locals())

from bokeson.froms import Register
# def register(request):
#     register_form = Register() #返回一个form表单
#     if request.method=="POST":
#         # username=request.POST.get("username")
#         username=request.POST.get("name")
#         password=request.POST.get("password")
#         content = '参数不全'
#         if username and password:
#             # if password != password2:
#             #     content='两次密码不一样'
#             #     pass
#             # else:
#             user = User()
#             user.name=username
#             # user.password=password
#             #加密密码
#             user.password = setPassword(password)
#             user.save()
#             content='添加成功'
#     return render(request,"register.html",locals())
import hashlib
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result
def register(request):
    register_form = Register() #返回一个form表单
    error=""
    if request.method=="POST":
        # username=request.POST.get("username")
        data=Register(request.POST)#将post请求过来的数据，交给from表单进行效验
        if data.is_valid():  #判断效验是否通过，通过 返回一个Ture否则 是通过False
            clean_data = data.cleaned_data
            # 获取数据库
            username=clean_data.get("name")
            password=clean_data.get("password")
            user = User()
            user.name = username
           #加密密码
            user.password = setPassword(password)
            user.save()
            error='添加成功'
        else:
            error = data.errors
            print(error)
    return render(request,"register.html",locals())


def ajax_get(request):

    return render(request,'ajax_get.html')

def ajax_get_data(request):
    result = {"code":10000,"content":""}
    data  = request.GET
    username = data.get('username')
    password = data.get('password')
    if len(password) == 0 or len(password) == 0:
        result['code'] = 10001
        result['content'] = '请求参数为空'
    else:
        user=User.objects.filter(name=username,password=setPassword(password)).first()
        if user:
            result["code"]=10000
            result["content"]='用户可登入'
        else:
            result["code"] = 10002
            result["content"] = '用户名的密码不存在'


    return JsonResponse(result)
    # return HttpResponse('ajax的请求')
def ajax_post(request):
    return render(request,"ajax_post.html")
def ajax_post_data(request):
    result = {}
    username = request.POST.get('username')
    password = request.POST.get("password")
    print(request.POST)
    print (username)
    if len(username) == 0 or len(password) == 0:
        result['code'] = 10001
        result['content'] = '请求参数为空'
    else:
        user = User()
        user.name=username
        user.password=setPassword(password)
        # user=User.objects.filter(name=username,password=setPassword(password)).first()
        # if user:
        try:
            user.save()
            result["code"]=10000
            result["content"]='添加成功'
        except:
            result["code"] = 10002
            result["content"] = '用户名的密码不存在'

    return JsonResponse(result)
##效验账户是否存在
def checkusername(request):
    result = {'code':10001,'content':""}
    #get 请求
    username =request.GET.get('name')
    print(username)
    #判断用户是否存在
    user = User.objects.filter(name=username).first()
    print(user)
    if user:
        result = {"code":10001,'content':"用户已存在"}
    else:
        result = {'code':10000,"content":'用户不存在'}
    return JsonResponse(result)
from django.http import HttpResponseRedirect
def login(request):
    result=''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(name=username).first()
        if user:
            if user.password == setPassword(password):
                # # 密码正确
                # #跳转首页 状态码
                # return HttpResponseRedirect('/index/')
                response = HttpResponseRedirect('/index/')
                response.set_cookie('username',username)
                request.session['username']=username
                return response
    return render(request,"login.html")
#登出
def logout(request):
    response = HttpResponseRedirect('/index/')
    response.delete_cookie('username')
    del request.session['username']#删除指定的
    request.session.flush()#删除所有的
    return response