from django.shortcuts import render, HttpResponse, redirect
from .models import Student

# Create your views here.
def in_content(request):
    return render(request, 'workshop19/students_input.html')
   
def out_content(request):
    input_name = request.POST.get('input_name')
    input_email = request.POST.get('input_email')
    input_birth = request.POST.get('input_birth')
    input_age = request.POST.get('input_age')
    
    student = Student(name=input_name, email=input_email, birthday=input_birth, age=input_age)
    student.save()
    return redirect(f'/workshop19/students/{student.id}')
    
# R
def index(request):
    students = Student.objects.all()
    return render(request, 'workshop19/students_index.html', {'students':students})
    
def detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'workshop19/students_detail.html', {'student':student})

# user가 넘긴 데이터를 실제 DB에 저장하는 액션
# @csrf_exempt > csrf 방어를 해제
# def create(request):
#     input_title = request.POST.get('input_title')
#     input_content = request.POST.get('input_content')
    
#     article = Article(title=input_title, content=input_content)
#     article.save()
#     return redirect(f'/boards/articles/{article.id}')

# Read
    # index : 모든 article 들을 보여주는 html (목록)
# def index(request):
#     articles = Article.objects.all()
#     return render(request, 'boards/index.html', {'articles':articles}) #templates>boards 이기 때문에space name도 써줘야함

    # 특정 article 을 보여주는 html (상세)
# def detail(request, id):
#     article = Article.objects.get(id=id)
#     return render(request, 'boards/detail.html', {'article':article})