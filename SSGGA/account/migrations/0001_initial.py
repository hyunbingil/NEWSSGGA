# Generated by Django 3.0.7 on 2020-06-07 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='이름')),
                ('nickname', models.CharField(max_length=20, null=True, verbose_name='닉네임')),
                ('birth', models.DateField(null=True, verbose_name='생년월일')),
                ('phone', models.CharField(max_length=20, verbose_name='전화번호')),
                ('gender', models.CharField(choices=[('남', '남'), ('여', '여')], max_length=2, verbose_name='성별')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('image', models.ImageField(default='./images/userdefaultimg.png', null=True, upload_to='', verbose_name='(선택) 프로필사진')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
