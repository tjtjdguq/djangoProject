from django.db import models
# Create your models here.
class Songs(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    lyric=models.TextField()
    rank=models.DecimalField(max_digits=3,decimal_places=0)
    image=models.ImageField(blank=True)
    def __str__(self):
        return self.title+str(Songs.pk)
