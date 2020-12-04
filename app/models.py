from django.db import models

# Create your models here.

class Asset(models.Model):
    reg_number = models.CharField(max_length=20)

    def __str__(self):
        return self.reg_number


class Track(models.Model):
    time = models.DateTimeField(auto_now=True)
    location=models.CharField(max_length=200,null=True)
    building=models.CharField(max_length=200,blank=True,null=True)
    tracking=models.ForeignKey(Asset,on_delete=models.CASCADE,related_name='tracking')

    def __str__(self):
        return self.location
