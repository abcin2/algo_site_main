import datetime
from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class Test(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class AlgorithmType(models.Model):
    algo_type = models.CharField(max_length=200)
    algo_description = models.TextField(max_length=2000)
    algo_thumbnail = models.ImageField(upload_to='algo_thumbs/')
    
    def __str__(self):
        return self.algo_type
    
    @property
    def str_to_url(self):
        return '_'.join(self.algo_type.lower().split(' '))
    
class DataSet(models.Model):
    your_data = ArrayField(models.IntegerField())
    bar_width = models.IntegerField()
    max_bar = models.IntegerField()
    data_id = models.AutoField(primary_key=True, default=None)
    
    def __str__(self):
        return str(self.data_id)