# Generated by Django 2.2.1 on 2019-09-12 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20190911_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': '书本'},
        ),
        migrations.AlterModelOptions(
            name='publish',
            options={'verbose_name_plural': '出版社'},
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=32, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Publish', verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='publish',
            name='address',
            field=models.CharField(max_length=32, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='publish',
            name='name',
            field=models.CharField(max_length=32, verbose_name='出版社'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('gender', models.CharField(max_length=12)),
                ('person', models.ManyToManyField(to='app01.Person')),
            ],
        ),
    ]
