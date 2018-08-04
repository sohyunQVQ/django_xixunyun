from django.db import models

# Create your models here.
class Users(models.Model):
    studentid = models.CharField(max_length=8)
    password =  models.CharField(max_length=256)
    schoolid = models.IntegerField()
    address = models.CharField(max_length=256)
    latitude = models.CharField(max_length=256)
    longitude = models.CharField(max_length=256)
    playcard = models.CharField(max_length=256,null=True)

    def __unicode__(self):
        return self.studentid
