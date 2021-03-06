# Generated by Django 3.2.4 on 2021-06-22 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeightTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='測定日時')),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('height', models.FloatField(verbose_name='身長')),
                ('weight', models.FloatField(verbose_name='体重')),
            ],
        ),
    ]
