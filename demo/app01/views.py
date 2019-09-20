from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return HttpResponse('hello')
def addperson(request):
     #1.save
    #第一种
    # person = Person(name='lisi',age=19,height=170,birthday='1999-08-08')
    # person.save()

    #第二种
    # person=Person()
    # person.name='mingming'
    # person.age=17
    # person.height=180
    # person.birthday='1998-08-07'
    # person.save()
    # return HttpResponse('增加数据')
    #crate
    # data=dict(name='xiaohong',age=17,height=190,birthday='1992-02-18')
    # Person.objects.create(**data)
    return HttpResponse('增加数据')
#查询
def queryset(request):
    #all方法
    # data=Person.objects.all()
    # print(data)
    #get
    # data=Person.objects.get(id=1)
    # print(data.name)
    # print(data.age)
    #filter
    # data=Person.objects.filter(name='lisi')
    # print(data)
    #first方法和last
    # data=Person.objects.filter(name='wangwu').first()
    # print(data.age)
    # data=Person.objects.filter(name='wangwu').last()
    # print(data.age)

    #order_by
    # data=Person.objects.order_by('age')
    # for one in data:
    #     print(one.age)


    #exclud
    # data=Person.objects.exclude(name='wangwu')
    # for one in data:
    #     print(one.name)

    #reverse对查询结果反向排序 逆序
    # data=Person.objects.order_by('-id').reverse()
    # print(data)


    # value queryset[对象，对象]
    # data=Person.objects.filter(name='wangwu').values()
    # print(data)

    #count
    # data=Person.objects.filter(name='wangwu').count()
    # print(data)

    #切片
    # data = Person.objects.order_by('id')[2:5]
    # print(data)


    #双下划线查询
    #__lt小于
    # data=Person.objects.filter(id__lt=3)
    # print(data)
    #gt
    # data=Person.objects.filter(id__gt=3)
    # print(data)

    #gte
    # data=Person.objects.filter(id__gte=3)
    # print(data)

    #in 包含 select * from stu where id in [1,2,3];
    # data=Person.objects.filter(id__in=[1,2,3])
    # print(data)


    #excloude 不包含

    #range 范围
    # data=Person.objects.filter(id__range=[1,5])
    # print(data)

    #startswith 像 like j% endswith 像 %j
    # data= Person.objects.filter(name__startswith='w')
    # print(data)
    #endswith是后边结尾

    #__contains 包含  大小敏感
    # data=Person.objects.filter(name__contains='m')
    # print(data)
    #__icontains 包含 大小写不敏感
    # ss=Person.objects.filter(name__icontains='m')
    # print(ss)

    return HttpResponse('查询数据')

def updata(request):
    #save
    #先查询查询到数据，然后重新赋值进行，然后save复制
    # data=Person.objects.get(id=2)
    # data.name='python'
    # data.save()
    # data=Person.objects.filter(name='wangwu').all()
    # for one in data:
    #     if one.id==4:
    #         one.age=22
    #     else:
    #         one.age=19
    #     one.save()

    #updata
    # Person.objects.filter(id=3).update(name='Mary')

    return HttpResponse('修改数据')

def drop(request):
    #delete
    # Person.objects.filter(id=6).delete()
    return HttpResponse('删除数据')

#一对多增加
def addonemore(request):
    #增加出版社
    # Publish.objects.create(name='清华出版社',address='北京')
    # Publish.objects.create(name='河南出版社',address='河南')
    # Publish.objects.create(name='河北出版社',address='河北')
    # #增加书
    # Book.objects.create(name='python入门',publish_id=1)
    # Book.objects.create(name='web入门',publish_id=1)
    #第二种方法
    # publish=Publish.objects.get(name='河南出版社')
    # Book.objects.create(name='docker入门',publish_id=publish.id)
    #第三种方法
    #正向操作 从外键所在的表到主表叫正向
    # book=Book()
    #     # book.name='笨办法学web'
    #     # book.publish=Publish.objects.get(name='河南出版社')
    #     # book.save()
    #反向操作 从主表到从表 叫反向
    # publish_obj=Publish.objects.get(name='河北出版社')
    # publish_obj.book_set.create(name='pythonweb开发')

    return HttpResponse("一对多关系增加")

#一对多查询
def getonemore(request):
    #第一种查询方法
    # publish=Publish.objects.get(name='清华出版社')
    # book=Book.objects.filter(publish_id=publish.id).all()
    # for one in book:
    #     print(one.name)

    #第二种查询方法
    #正向查询 从外键所在的表到主表 叫正向
    book = Book.objects.filter(name='pythonWeb开发').first()
    print(book.name)
    print(book.publish.name)

    #第三种查询
    #反向查询 从主键到外键所在的表 叫反向
    publish=Publish.objects.get(name='河北出版社')
    book=publish.book_set.all()
    for one in book:
        print(one.name)
    return HttpResponse("一对多关系查询")

#一对多修改
def updataonemore(request):
    #save 方法
    # book=Book.objects.filter(name='mysql入门',id=5).first()
    # book=Book.objects.get(id=5)
    # book.publish=Publish.objects.get(name='清华出版社')
    # book.save()
    #update
    # Book.objects.filter(name='mysql入门',id=5).update(publish=Publish.objects.get(name='河北出版社'))
    #set
    # publish=Publish.objects.get(name='河南出版社')
    # book=Book.objects.get(id=3)
    # book_s=Book.objects.get(id=5)
    # publish.book_set.set([book,book_s])

    return HttpResponse("一对多关系修改")

#一对多删除
def deleteonemore(request):

    return HttpResponse("一对多关系删除")



#多对多
def manytomanyadd(request):
    #老师
    # Teacher.objects.create(name='laozhang',gender='女',age=32)
    # Teacher.objects.create(name='老王',gender='女',age=32)
    # Teacher.objects.create(name='老边',gender='男',age=32)
    # Teacher.objects.create(name='老岳',gender='女',age=32)
    # Teacher.objects.create(name='老云',gender='男',age=32)


    #新学生  创建关系 create 正向操作
    # teacher_obj=Teacher.objects.filter(name='老边').first()
    # teacher_obj.person.create(name='Jason',age=17,height=170,birthday='1888-09-07')
    #老学生 创建关系   add 正向操作
    # teacher_obj=Teacher.objects.filter(name='老岳').first()
    # person_obj=Person.objects.filter(name='mingming').first()
    # teacher_obj.person.add(person_obj)

    #反向操作
    # teacher_obj=Teacher.objects.filter(name='laozhang').first()
    # person_obj=Person.objects.filter(name='Jason').first()
    # person_obj.teacher_set.add(teacher_obj)
    return HttpResponse('多对多添加')

def manytomanyget(request):
    #正向查询
    teacher_obj=Teacher.objects.filter(name='laozhang').first()
    person=teacher_obj.person.all().values()
    print(person)
    #反向查询
    person_obj=Person.objects.filter(name='Jason').first()
    teacher_obj=person_obj.teacher_set.all().values()
    print(teacher_obj)



    return HttpResponse('多对多查询')

def manytomanyupdate(request):
    #正向
    #第一种
    # teacher_obj=Teacher.objects.filter(name="laozhang").first()
    # teacher_obj.person.set([1,2,3,4,])
    #第二种
    # teacher_obj=Teacher.objects.filter(name='老王').first()
    # person1 = Person.objects.filter(name='wy').first()
    # person2=Person.objects.filter(name='xiaohong').first()
    # teacher_obj.person.set([person1,person2])


    #反向
    # 第一种
    # person_obj=Person.objects.filter(name='mingming').first()
    # person_obj.teacher_set.set([2])
    #第二种
    person_obj = Person.objects.filter(name='wy').first()
    teacher1 = Teacher.objects.filter(name='老王').first()
    teacher2 = Teacher.objects.filter(name='老岳').first()
    person_obj.teacher_set.set([teacher1,teacher2])

    return HttpResponse('多对多修改')

def manytomanydelete(request):
    # remove
    # 正向
    # person_obj=Person.objects.filter(name='mingming').first()
    # teacher_obj=Teacher.objects.filter(name='老岳').first()
    # teacher_obj.person.remove(person_obj)
    #反向
    # person_obj = Person.objects.filter(name='lisi').first()
    # teacher_obj=Teacher.objects.filter(name='laozhang').first()
    # person_obj.teacher_set.remove(teacher_obj)
    # delete
    # 删除老师
    # Teacher.objects.filter(name='laozhang').first().delete()
    #删除同学
    # Person.objects.filter(name='lise').delete()
    return HttpResponse('多对多删除')

from django.db.models import *
def jhtest(request):
    data=Person.objects.all().aggregate(Avg('age'))
    print(data)
    data=Person.objects.all().aggregate(avg_age=Avg('age'),sum_age=Sum('age'))
    print(data)
    return HttpResponse('聚合函数，查询')

#F对象
def Ftest(request):
    ##查询存num 大于销量salled num_get=3
    data=Book.objects.filter(num__gt=F('stell'))
    print(data)
    return HttpResponse('F 对象')

def Qtest(request):
    # data=Book.objects.filter(Q(num=10)&Q(stell=100))
    # print(data)
    data = Book.objects.filter(Q(num=10)|Q(stell=100)).all()
    print(data)
    data = Book.objects.filter(~Q(num=10) | ~Q(stell=100)).all()
    print(data)
    return HttpResponse('Q对象')