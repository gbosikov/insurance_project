from django.db import models

# Create your models here.


class Diction(models.Model):
    """
    Table contains all possible values of diction's
    """
    name_id = models.CharField(max_length=150, null=True, default=None, verbose_name='custom name')
    name_e = models.CharField(max_length=30, null=False, verbose_name='english name')
    name_g = models.CharField(max_length=30, null=False, verbose_name='georgian name')
    name_r = models.CharField(max_length=30, null=False, verbose_name='russian name')
    custom_order = models.IntegerField(null=True, default=None, verbose_name='custom order')
    color = models.IntegerField(null=True, default=None, verbose_name='color')
    visible = models.BooleanField(default=True, verbose_name='visible')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='create date')
    # ALTER TABLE [dbo].[environment_diction] ADD  CONSTRAINT [DF_environment_diction_created_at]  DEFAULT (getdate())
    # FOR [created_at]

    class Meta:
        verbose_name_plural = 'Diction'
        ordering = ('id',)

    def __str__(self):
        return self.name_e


class InsTypes(models.Model):
    """
    Contains all insurance types
    """
    custom_id = models.CharField(max_length=150, null=True, default=None, verbose_name='custom name')
    name_e = models.CharField(max_length=150, null=False, verbose_name='english name')
    name_g = models.CharField(max_length=150, null=False, verbose_name='georgian name')
    name_r = models.CharField(max_length=150, null=False, verbose_name='russian name')
    diction = models.ForeignKey(Diction, on_delete=models.CASCADE, verbose_name='diction id')
    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    # ALTER TABLE [dbo].[environment_instypes] ADD  CONSTRAINT [DF_environment_instypes_created_at]  DEFAULT (getdate())
    # FOR [created_at]

    class Meta:
        verbose_name_plural = 'InsTypes'
        ordering = ('id',)

    def __str__(self):
        return self.name_e
# class Risks(models.Model):
#     """
#     Contains all risks list
#     """
#     custom_id = models.IntegerField(null=True, default=None)
#     name_e = models.CharField(max_length=150, null=False)
#     name_g = models.CharField(max_length=150, null=False)
#     name_r = models.CharField(max_length=150, null=False)
#     diction = models.ForeignKey(Diction, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'Risks'
#         ordering = ('id',)
#
#     def __str__(self):
#         return self.name_e
#
#
# class Objects(models.Model):
#     """
#     Contains all insurance object possible values
#     """
#     custom_id = models.IntegerField(null=True, default=None)
#     name_e = models.CharField(max_length=30, null=False)
#     name_g = models.CharField(max_length=30, null=False)
#     name_r = models.CharField(max_length=30, null=False)
#     diction = models.ForeignKey(Diction, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'Objects'
#         ordering = ('id',)
#
#     def __str__(self):
#         return self.name_e
#
#
#
