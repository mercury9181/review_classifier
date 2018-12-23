from django.db import models

# Create blog model
class Blog(models.Model):
    #ceate structure
  title = models.CharField(max_length=255)
  pub_date= models.DateTimeField()
  body= models.TextField()
  image = models.ImageField(upload_to='images/')

  #add the blog app in the setings.py

  #create a migration

  #migrate

  #add to the admin.py in blog
