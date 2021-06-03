from django.db import models

# Create your models here.
class BookInfo(models.Model ):
    #charfiled
    btitle = models.CharField(max_length=22)
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=122)
    hgender = models.BooleanField(default=True)
    # hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname




