from django.db import models
#Create your models here.
class Anima(models.Model):
    name = models.CharField(max_length=50)
    An_type = models.CharField(max_length=10)
    l_ing = models.ImageField(upload_to='static/ANindex')
    web = models.URLField()
    time = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=10,null=True)
    class Meta:
        verbose_name = '动画'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class m_user(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    email = models.EmailField()
    time = models.DateTimeField(auto_now=True)
    anime = models.ManyToManyField(Anima)
    def __str__(self):
        return self.user