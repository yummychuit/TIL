from django.shortcuts import render

def ssafy(request):
    return render(request, 'ssafy.html')

def student(request, name):
    return render(request, 'student.html', { 'name':name })