from django.db import models

# Create your models here.
class Person(models.Model):
    # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='姓名')
    age=models.IntegerField(verbose_name='性别')
    height=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='身高')
    birthday=models.DateField(verbose_name='生日')
    def __str__(self):
        return self.name
    class Meta:
        db_table='persion'#修改名字
        verbose_name='用户'
        verbose_name_plural=verbose_name





class Publish(models.Model):
    name=models.CharField(max_length=32,verbose_name='出版社')
    address=models.CharField(max_length=32,verbose_name='地址')
    def __str__(self):
        return self.name
    class Meta:
        db_table='publish'
        verbose_name_plural='出版社'


class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name='书名')
    num=models.IntegerField(default=10)
    stell=models.IntegerField(default=10)
    publish = models.ForeignKey(to=Publish,to_field='id',on_delete=models.DO_NOTHING,verbose_name='出版社')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'book'
        verbose_name_plural='书本'

class Teacher(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    gender=models.CharField(max_length=12)
    person = models.ManyToManyField(to=Person)
    class Meta:
        db_table='teacher'