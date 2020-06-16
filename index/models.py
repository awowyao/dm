from django.db import models

# Create your models here.
# class Information(models.Model):
#     username = models.CharField(max_length=10)
#     enail = models.EmailField()
#     sex = models.CharField(max_length=5)
#     address = models.CharField(max_length=50)
#     hobby = models.CharField(max_length=50)
#     massage = models.CharField(max_length=100)
#     time = models.TimeField(autro_now=True)
class Information(models.Model):
    username = models.CharField(max_length=10)
    enail = models.EmailField()
    sex = models.CharField(max_length=5)
    address = models.CharField(max_length=50)
    hobby = models.CharField(max_length=50)
    massage = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username

class Meta:
    crdering = ['create_time']