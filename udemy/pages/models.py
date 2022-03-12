from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=2555)
    designation = models.CharField(max_length=255)
    photos = models.ImageField(upload_to = 'photos/%y/%m/%d/')
    facebook_link  = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    goodle_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.first_name