# Generated by Django 3.2.4 on 2021-06-23 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210623_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('F', '女性'), ('M', '男性'), ('U', '不詳')], max_length=1, verbose_name='性別'),
        ),
    ]
