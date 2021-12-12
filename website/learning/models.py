from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Topic(models.Model):
    topicName=models.CharField(max_length=100)
    creationdate=models.DateField(auto_created=True)




class SubTopics(models.Model):
    topicName=models.ForeignKey(Topic,on_delete=CASCADE)
    subTopicName=models.CharField(max_length=100)
    content=models.TextField()



