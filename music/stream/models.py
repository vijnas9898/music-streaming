from django.db import models

class Songs(models.Model):
    tittle = models.CharField( max_length=50)
    song = models.FileField(upload_to='media/', max_length=100)
    artist = models.CharField(max_length=50)
    album = models.CharField( max_length=50)

    def __str__(self):
        return self.tittle
    
