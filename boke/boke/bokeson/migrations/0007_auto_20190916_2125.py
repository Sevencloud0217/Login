# Generated by Django 2.2.1 on 2019-09-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokeson', '0006_auto_20190916_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='pricture',
        ),
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(default='images/01.jpg', upload_to='images'),
            preserve_default=False,
        ),
    ]
