from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.TextField()
    questions = models.ManyToManyField("Question", blank=True)
    
class Question(models.Model):
    question = models.TextField()
    options = models.ManyToManyField("Option", blank=True)
        
class Option(models.Model):
    value = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    
class EssayTest(models.Model):
    topic = models.CharField(max_length=100)
    note = models.TextField()
    questions = models.ManyToManyField("EssayQuestion", blank=True)

class EssayQuestion(models.Model):
    question = models.TextField()