from django.db import models

# Create blog model
class Blog(models.Model):
    #ceate structure
    title = models.CharField(max_length=500)
    rating = models.FloatField(null=True, blank=True, default=None)
    location=models.CharField(max_length=30,default='something')
    pub_date= models.DateTimeField()
    body= models.TextField()
    image = models.ImageField(upload_to='images/')

    #add the blog app in the setings.py

    #create a migration

    #migrate

    #add to the admin.py in blog

    def __str__(self):
        return self.title

        #for make summary of the body ..
    def summary(self):
        return self.body[:100]

            #make date structure pretty

    def pub_date_pretty(self):
            return self.pub_date.strftime(' %c ')


            
