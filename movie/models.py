from django.db import models
class Movie(models.Model):
    name=models.CharField(max_length=40)
    desc=models.CharField(max_length=50)
    year=models.IntegerField()
    image=models.ImageField(upload_to='movies',null=True,blank=True)

    def __str__(self):
        return self.name

