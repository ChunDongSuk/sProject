from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student


def regStudent(request):
    return render(request, 'students/registerStudent.html')


def regConStudent(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    qs = Student(s_name=name, s_major=major, s_age=age,
                 s_grade=grade, s_gender=gender)
    qs.save()

    return HttpResponseRedirect(reverse('students:stuAll'))


def readStudentAll(request):
    qs = Student.objects.all()
    context = {'student_list': qs}
    return render(request, 'students/readStudents.html', context)
