from django.db import models


# Create your models here.
#create structure
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    #add the jobs app in the setings.py

    #create a migration

    #migrate

    #add to the admin.py in jobs
    
