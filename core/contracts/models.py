from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contracts(models.Model):
    cont_num = models.CharField(max_length=30, null=False)
    name_g = models.CharField(max_length=30, null=False)
    name_r = models.CharField(max_length=30, null=False)
    sname_e = models.CharField(max_length=30, null=False)
    sname_g = models.CharField(max_length=30, null=False)
    sname_r = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user who add row')
    host_name = models.CharField(max_length=30, null=False)

    class Meta:
        db_table = 'contracts'