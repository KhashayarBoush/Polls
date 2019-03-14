from django.db import models
from django.utils import timezone
import datetime
import uuid

class Writer(models.Model):
    name = models.CharField(max_length = 300)
    family = models.CharField(max_length = 300)
    Email = models.EmailField(blank = True)
    born = models.DateField(blank = True,null = True)
    def __str__(self):
        return '%s, %s' % (self.name, self.family)

    def get_absolute_url(self):
        return reverse("model_detail", args=[str(self.id)] )



class Book(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "unique id for each book")
    writer = models.ForeignKey('Writer', on_delete=models.CASCADE)
    name = models.CharField(max_length = 300)
    Create =  models.DateField(blank = True, null = True)
    def __str__(self):
        return '%s, %s' %(self.writer,self.name)
