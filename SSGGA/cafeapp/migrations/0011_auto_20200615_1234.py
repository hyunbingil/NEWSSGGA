# Generated by Django 3.0.7 on 2020-06-15 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0010_auto_20200615_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='image',
            field=models.ImageField(default='images/user_default_img.png', null=True, upload_to='images/', verbose_name='카페 아이콘'),
        ),
    ]