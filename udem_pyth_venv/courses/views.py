from django.shortcuts import render, get_object_or_404
from .models import Course

from django.http import HttpResponse

# Create your views here. Just testing
# Added a new comment to test GIT

def index(request):
    courses = Course.objects
    return render(request, 'courses/index.html', {'courses':courses})

def detail(request, course_id):
    course_detail = get_object_or_404(Course,pk=course_id)
    return render(request, 'courses/detail.html', {'course':course_detail})
