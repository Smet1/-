# Generated by Django 2.0 on 2018-01-08 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20180108_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankmodel',
            name='image',
            field=models.ImageField(default='lab6/static/img/banks/default.jpg', upload_to='lab6/static/img/banks'),
        ),
    ]