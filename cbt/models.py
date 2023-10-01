from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.TextField()
    questions = models.ManyToManyField("Question", blank=True)
    
class Question(models.Model):
    question = models.TextField()
    options = models.ManyToManyField("Option", blank=True)
    answer = models.ForeignKey("Option", on_delete=models.CASCADE, related_name="answer_for", null=True)
    
class Option(models.Model):
    value = models.TextField()