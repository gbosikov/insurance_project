from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    """
    exists all customers
    """
    ext_num = models.IntegerField(null=True, default=None, verbose_name='extra number')
    name_e = models.CharField(max_length=30, null=False, verbose_name='english name')
    name_g = models.CharField(max_length=30, null=False, verbose_name='georgian name')
    name_r = models.CharField(max_length=30, null=False, verbose_name='russian name')
    sname_e = models.CharField(max_length=30, null=False, verbose_name='english name')
    sname_g = models.CharField(max_length=30, null=False, verbose_name='georgian name')
    sname_r = models.CharField(max_length=30, null=False, verbose_name='russian name')
    cust_type = models.IntegerField(null=False, default=0, verbose_name='all types of customers')
    parent_cust = models.IntegerField(null=True, default=None, verbose_name='parent customer')
    org_type = models.IntegerField(null=True, default=None)
    sex = models.IntegerField(null=False)
    date_of_birth = models.DateField(null=False)
    date_of_death = models.DateField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    close_date = models.DateTimeField(null=True, default=None)
    vip_state = models.BooleanField(default=0)


class Cust_Name_His(models.Model):
    name_e = models.CharField(max_length=30, null=False)
    name_g = models.CharField(max_length=30, null=False)
    name_r = models.CharField(max_length=30, null=False)
    sname_e = models.CharField(max_length=30, null=False)
    sname_g = models.CharField(max_length=30, null=False)
    sname_r = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user who add row')
    host_name = models.CharField(max_length=30, null=False)


