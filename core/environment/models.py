from django.db import models

# Create your models here.


class Diction(models.Model):
    """
    Table contains all possible values of diction's
    """
    custom_id = models.IntegerField(null=True, default=None)
    name_e = models.CharField(max_length=30, null=False)
    name_g = models.CharField(max_length=30, null=False)
    name_r = models.CharField(max_length=30, null=False)
    custom_order = models.IntegerField(null=True, default=None)
    color = models.IntegerField(null=True, default=None)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Diction'
        ordering = ('id',)

    def __str__(self):
        return self.name_e


class InsTypes(models.Model):
    """
    Contains all insurance types
    """
    custom_id = models.IntegerField(null=True, default=None)
    name_e = models.CharField(max_length=150, null=False)
    name_g = models.CharField(max_length=150, null=False)
    name_r = models.CharField(max_length=150, null=False)
    diction = models.ForeignKey(Diction, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'InsTypes'
        ordering = ('id',)

    def __str__(self):
        return self.name_e


class Risks(models.Model):
    """
    Contains all risks list
    """
    custom_id = models.IntegerField(null=True, default=None)
    name_e = models.CharField(max_length=150, null=False)
    name_g = models.CharField(max_length=150, null=False)
    name_r = models.CharField(max_length=150, null=False)
    diction = models.ForeignKey(Diction, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Risks'
        ordering = ('id',)

    def __str__(self):
        return self.name_e


class Objects(models.Model):
    """
    Contains all insurance object possible values
    """
    custom_id = models.IntegerField(null=True, default=None)
    name_e = models.CharField(max_length=30, null=False)
    name_g = models.CharField(max_length=30, null=False)
    name_r = models.CharField(max_length=30, null=False)
    diction = models.ForeignKey(Diction, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Objects'
        ordering = ('id',)

    def __str__(self):
        return self.name_e



