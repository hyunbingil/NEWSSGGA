# Generated by Django 3.0.7 on 2020-06-15 03:04

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0007_auto_20200615_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default='images/user_default_img.png', null=True, upload_to='images/'),
        ),
    ]