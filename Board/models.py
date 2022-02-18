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

class LyricInsert(models.Model):
    song=models.ForeignKey('Board.Songs',on_delete=models.CASCADE,related_name='inserted_lyric')
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    lyric=models.TextField()