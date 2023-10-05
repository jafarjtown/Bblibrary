from django.forms import ModelForm, CharField, RadioSelect
from .models import Question, Option

class OptionForm(ModelForm):
    #value = CharField(required=False)
    class Meta:
        model = Option
        fields = "__all__"
        


class QuestionForm(ModelForm):
    class Meta:
        model = Question 
        fields = ["question"]
