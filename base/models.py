from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.

# null=False/True
# Blank=False/True
# verbose_name = 'aksjfaskf'
# default = ''

class Person(models.Model):
    GENDERS = [
        ('1','دختر'),
        ('2','پسر'),
    ]
    EXPERIENCE = [
        ('0','مقدماتی'),
        ('1','متوسط'),
        ('2','پیشرفته'),
    ]

    first_name = models.CharField(max_length=127, null=True, verbose_name='نام')
    last_name = models.CharField(max_length=127, null=True, verbose_name='نام خانوادگی')
    bio = models.TextField(max_length=2047, null=True, blank=True, verbose_name='بیوگرافی')
    phone = models.CharField(max_length=13, null=True, verbose_name='شماره تلفن')
    email = models.EmailField(max_length=127, null=True, verbose_name='ایمیل')
    birthDate = models.DateField( null=True, verbose_name='تاریخ تولد')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ثبت')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ به روز رسانی')
    jalali_date = jmodels.jDateField(null=True)
    password = models.CharField(max_length=20, null=True, verbose_name='رمز عبور')
    age = models.IntegerField( null=True, verbose_name='سن')
    height = models.DecimalField(max_digits=4, decimal_places=1, null=True, verbose_name='قد')
    is_stuff = models.BooleanField( verbose_name='وضعیت کارمندی')

    gender = models.CharField(max_length=1, choices=GENDERS, null=True, verbose_name='جنسیت')
    experience = models.CharField(max_length=1, choices=EXPERIENCE, null=True, verbose_name='سطح تجربه')

    def __str__(self):
        return self.first_name + " " + self.last_name

class Blog(models.Model):

    title = models.CharField(max_length=127, null=True)
    body = models.TextField(max_length=2047, null=True)
    author = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='posts')
    readers = models.ManyToManyField(Person, related_name='readed_blogs')

    def __str__(self):
        return self.title + 'written by :' + self.author.first_name + " " + self.author.last_name