from django.shortcuts import render, redirect 
from django.http import JsonResponse 
from .models import Course as cbt, Question, Option, EssayTest, EssayQuestion,TrueFalseQuestion, TrueFalseCourse, FillInTheBlank
from .forms import QuestionForm, OptionForm, TrueFalseQuestionForm

from user_account.decorators import has_enough_coins, subtract_coins
import random as r
import json
# Create your views here.

def index(request):
    courses = cbt.objects.all()
    return render(request, "cbt/index.html", {"courses": courses})

def tests(request):
    obj = cbt.objects.all()
    ess = EssayTest.objects.all()
    fill = FillInTheBlank.objects.all()
    trfs = TrueFalseCourse.objects.all()
    return render(request, "cbt/cbt_tests.html", {"obj": obj, "ess": ess, "fill":fill, "trf":trfs})

#@has_enough_coins(100)
#@subtract_coins(100)
def cbt_test(request, id=None):
    t = int(request.GET.get("t", 15))
    course = cbt.objects.get(id=id)
    questions= course.questions.order_by("?").all()
    return render(request, "cbt/cbt_test.html", {"course": course, "qs": questions[:t]})
    
def cbt_time_base(request, id=None):
    time = int(request.GET.get("t", 15))
    if time == 15 or time < 20:
        t = 30
    elif time == 20 or time < 35:
        t = 40
    else:
        t = 60
    course = cbt.objects.get(id=id)
    questions= course.questions.order_by("?").all()
    return render(request, "cbt/cbt_time_base.html", {"course": course, "qs": questions[:t], "time":time})
    
    
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
            op = qq.options.get(id=a)
            qs.append({"q":qq, "select": a})
            
            if op.is_correct:
                result["score"] += 1
    return render(request, "cbt/cbt_time_base_result.html", {"course": course, "qs": qs, "result": result})


def cbt_create_course(request):
    courses = cbt.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        course,_ = cbt.objects.get_or_create(name=name)
        return redirect("cbt_add_qs", course=course.id)
    return render(request, 'cbt/add_course.html', {"courses":courses})
    
def cbt_add_qs(request, course):
    course = cbt.objects.get(id=course)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        option_forms = []
        for key, value in request.POST.items():
        
            if key.startswith('option_') and key.endswith("value"):
                option_number = key.split("_")[1].split("-")[0]
                option_form = OptionForm(request.POST, prefix=f"option_{option_number}")
                option_forms.append(option_form)            
        option_forms = [OptionForm(request.POST, prefix=f'option_{i}') for i in range(4)]
        if question_form.is_valid() and len(option_forms) > 0:
            question = question_form.save()
            course.questions.add(question)
            course.save()
            option_forms = [option_form for option_form in option_forms if option_form.is_valid()]
            for option_form in option_forms:
                option = option_form.save()
                question.options.add(option)
                question.save()
            return redirect("cbt_add_qs", course=course.id)
    else:
        question_form = QuestionForm()
        option_forms = [OptionForm(prefix=f'option_{i}') for i in range(4)]
    return render(request, "cbt/add_qs.html", {"course":course, 'question_form': question_form, 'option_forms': option_forms})


def add_by_upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        if uploaded_file:
                js = json.load(uploaded_file)
                co, _ = cbt.objects.get_or_create(name=js.get("course"))
                for q in js.get("questions"):
                    if co.questions.filter(question=q["question"]).exists():
                        continue 
                    qu = Question.objects.create(question=q["question"])
                    for op in q.get("options"):
                        is_correct = False
                        if q["answer"] == op:
                            is_correct = True
                        o = Option.objects.create(value=op, is_correct=is_correct)
                        qu.options.add(o)
                        qu.save()
                    co.questions.add(qu)
                    co.save()
        else:
            return JsonResponse({"error": "No file uploaded"}, status=400)
    return redirect("cbt")


def essay_cbt(request):
    courses = EssayTest.objects.all()
    return render(request, "cbt/essay_cbt.html", {"courses":courses})
    
def add_by_upload_essay(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        if uploaded_file:
              js = json.load(uploaded_file)
              for topic in js:
                  co, cr = EssayTest.objects.get_or_create(topic=topic.get("Topic"))
                  if cr:
                      co.note = topic.get("Essay")
                  for q in topic.get("Questions"):
                      if co.questions.filter(question=q).exists():
                            continue 
                      qu = EssayQuestion.objects.create(question=q)
                      co.questions.add(qu)
                      co.save()
        else:
            return JsonResponse({"error": "No file uploaded"}, status=400)
    return redirect("essay_cbt")

def cbt_create_course_essay(request):
    if request.method == "POST":
        name = request.POST.get("name")
        course = EssayTest.objects.get_or_create(name=name)
        return redirect("cbt_add_qs", course=course.id)
    return render(request, 'cbt/upload_essay_qs.html')
    
#@has_enough_coins(50)
#@subtract_coins(50)    
def cbt_test_essay(request, id=None):
    course = EssayTest.objects.get(id=id)
    questions= list(course.questions.all())
    r.shuffle(questions)
    return render(request, "cbt/cbt_test_essay.html", {"course": course, "qs": questions[:6]})
    

def true_false_test(request):
    tfs = TrueFalseCourse.objects.all()
    return render(request, "cbt/tf.html", {"tfs":tfs})
    
def true_false_result(request, tid):
    tf = TrueFalseCourse.objects.get(id=tid)
    if request.method == "POST":
        attempts = dict(request.POST)
        del attempts["csrfmiddlewaretoken"]
        for qid, ans in attempts.items():
            ans = True if ans == true else False
            qq = tf.questions.get(id = qid)
    questions= list(tf.questions.all())
    r.shuffle(questions)
    return render(request, 'cbt/tfr.html', {"questions": questions, "course":tf.name})

def create_true_false_question(request, course):
    if request.method == 'POST':
        course = TrueFalseCourse.objects.get(id=course)
        form = TrueFalseQuestionForm(request.POST)
        if form.is_valid():
            trf = form.save(commit=False)
            trf.course = course
            trf.save()
            return redirect('cbt_add_tr_qs', course=course.id)
    else:
        form = TrueFalseQuestionForm()

    return render(request, 'cbt/true_question_form.html', {'form': form})
    
def fill_in_blank(request, id):
    fill = FillInTheBlank.objects.get(id=id)
    return render(request, 'cbt/fill-in-blank.html', {"fill":fill})
