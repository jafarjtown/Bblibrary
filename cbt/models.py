from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.TextField()
    questions = models.ManyToManyField("Question", blank=True)
    
class Question(models.Model):
    question = models.TextField()
    options = models.ManyToManyField("Option", blank=True)
    
    @property
    def correct_answer(self):
        for o in self.options.all():
            if o.is_correct:
                return o
        
class Option(models.Model):
    value = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    
class EssayTest(models.Model):
    topic = models.CharField(max_length=100)
    note = models.TextField()
    questions = models.ManyToManyField("EssayQuestion", blank=True)

class EssayQuestion(models.Model):
    question = models.TextField()

class FillInTheBlank(models.Model):
    name = models.CharField(max_length=255)


class FillInTheBlanksQuestion(models.Model):
    course = models.ForeignKey(FillInTheBlank, on_delete=models.CASCADE, related_name="questions")
    blanks = models.TextField(help_text="Enter blanks separated by [BLANK]. Example: The capital of [BLANK] is [BLANK].")
    correct_answers = models.TextField(help_text="Enter correct answers separated by commas. Example: Paris, France")
    
    def get_blanks_list(self):
        return self.blanks.split("[BLANK]")

    def get_correct_answers_list(self):
        return [answer.strip() for answer in self.correct_answers.split(",")]

    def is_answer_correct(self, user_answers):
        correct_answers = self.get_correct_answers_list()
        return user_answers == correct_answers

    def __str__(self):
        return self.blanks
    
    def parse_html(self):
        return self.blanks.replace('[BLANK]', '<input type="text" name="answer" />')
        

class TrueFalseCourse(models.Model):
    name = models.CharField(max_length=200)     
        
class TrueFalseQuestion(models.Model):
    course = models.ForeignKey(TrueFalseCourse, on_delete=models.CASCADE, related_name="questions")
    question_text = models.CharField(max_length=500)
    correct_answer = models.BooleanField()

    def __str__(self):
        return self.question_text
