from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Diction(models.Model):
    """
    Table contains all possible values of diction's
    """
    custom_name = models.CharField(max_length=150, null=True, default=None, verbose_name='custom name')
    name_e = models.CharField(max_length=30, null=False, verbose_name='english name')
    name_g = models.CharField(max_length=30, null=False, verbose_name='georgian name')
    name_r = models.CharField(max_length=30, null=False, verbose_name='russian name')
    custom_order = models.IntegerField(null=True, default=None, verbose_name='custom order')
    color = models.IntegerField(null=True, default=None, verbose_name='color')
    visible = models.BooleanField(default=True, verbose_name='visible')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='create date')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user who add row')

    class Meta:
        verbose_name_plural = 'Diction'
        ordering = ('id',)
        db_table = 'diction'

    def __str__(self):
        return self.name_e


class InsTypes(models.Model):
    """
    Contains all insurance types
    """
    custom_name = models.CharField(max_length=150, null=True, default=None, verbose_name='custom name')
    name_e = models.CharField(max_length=150, null=False, verbose_name='english name')
    name_g = models.CharField(max_length=150, null=False, verbose_name='georgian name')
    name_r = models.CharField(max_length=150, null=False, verbose_name='russian name')
    diction = models.ForeignKey(Diction, on_delete=models.CASCADE, verbose_name='diction id')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user who add row')

    class Meta:
        verbose_name_plural = 'InsTypes'
        ordering = ('id',)
        db_table = 'ins_types'

    def __str__(self):
        return self.name_e


class Risks(models.Model):
    """
    Contains all risks list
    """
    custom_name = models.CharField(max_length=150, null=True, default=None, verbose_name='custom name')
    name_e = models.CharField(max_length=150, null=False, verbose_name='english name')
    name_g = models.CharField(max_length=150, null=False, verbose_name='georgian name')
    name_r = models.CharField(max_length=150, null=False, verbose_name='russian name')
    diction = models.ForeignKey(Diction, on_delete=models.CASCADE, verbose_name='diction id')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user who add row')

    class Meta:
        verbose_name_plural = 'Risks'
        ordering = ('id',)
        db_table = 'risks'

    def __str__(self):
        return self.name_e


class Objects(models.Model):
    """
    Contains all insurance object possible values
    """
    custom_name = models.CharField(max_length=150, null=True, default=None, verbose_name='custom name')
    name_e = models.CharField(max_length=30, null=False, verbose_name='english name')
    name_g = models.CharField(max_length=30, null=False, verbose_name='georgian name')
    name_r = models.CharField(max_length=30, null=False, verbose_name='russian name')
    diction = models.ForeignKey(Diction, on_delete=models.CASCADE, verbose_name='diction id')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user who add row')

    class Meta:
        verbose_name_plural = 'Objects'
        ordering = ('id',)
        db_table = 'objects'

    def __str__(self):
        return self.name_e



