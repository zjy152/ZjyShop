
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    '''
    用户信息
    '''

    GENDER_CHOICES = (
        ('male', u'男'),
        ('female', u'女')
    )
    # 用户用手机注册，所以姓名，生日和邮箱可以为空
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='female', verbose_name='性别')
    mobile = models.CharField(max_length=11, null=True, blank=True,verbose_name='手机号码')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            # 如果不为空则返回用户名
            return self.name
        else:
            # 如果用户名为空则返回不能为空的对象
            return self.username


class VerifyCode(models.Model):
    '''
    验证码
    '''

    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


    class Meta:
        verbose_name = '短信验证'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code