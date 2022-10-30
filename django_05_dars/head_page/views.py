from django.shortcuts import render
from .models import Student
def register(request):
    if request.POST:
        model = Student()
        model.name = request.POST['name']
        model.email = request.POST['email']
        model.phono_number = request.POST['phono_number']
        model.password = request.POST['password']
        model.course_type = request.POST['course_type']
        model.save()
        print(request.POST)
    return render(request, 'register.html')


def index_page(request):
    return render(request, "index.html")

def ios_page(request):
    return render(request, "ios.html")

def android_page(request):
    return render(request, "android.html")