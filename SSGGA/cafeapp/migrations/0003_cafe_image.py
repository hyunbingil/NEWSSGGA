# Generated by Django 3.0.6 on 2020-06-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0002_auto_20200603_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='카페아이콘'),
        ),
    ]
