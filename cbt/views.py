from django.shortcuts import render
from .models import Course as cbt
import random as r
# Create your views here.

def index(request):
    courses = cbt.objects.all()
    return render(request, "cbt/index.html", {"courses": courses})
    
def cbt_test(request, id=None):
    course = cbt.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)
    questions= list(course.questions.all())
    r.shuffle(questions)
    return render(request, "cbt/cbt_test.html", {"course": course, "qs": questions[:40]})
    
    
def cbt_test_result(request, id):
    result = {"score":0, "qss":{}}
    course = cbt.objects.get(id=id)
    qs = []
    if request.method == "POST":
        attempts = dict(request.POST)
        del attempts["csrfmiddlewaretoken"]
        for q, a in attempts.items():
            a = int(a[0])
            qq = course.questions.get(id = q)
            qs.append({"q":qq, "correct":qq.answer.id == a, "select": a})
            print(qq.id, a)
            
            if qq.answer.id == a:
                result["score"] += 1
    return render(request, "cbt/cbt_test.html", {"course": course, "qs": qs, "result": result})
