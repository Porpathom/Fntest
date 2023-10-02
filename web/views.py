from web.models import Department, Employ, SEX_CHOICES, EDUCATION_CHOICES
from django.shortcuts import render

# Create your views here.
def getModelChoice(num, choices):
    for choice in choices:
        if choice[0] == num:
            return choice[1]
        
def index(request):
    context = {}
    emps = Employ.objects.all()
    for emp in emps :
        emp.edu_str = getModelChoice(emp.education,EDUCATION_CHOICES)
    for emp in emps :
        emp.sex_str = getModelChoice(emp.sex,SEX_CHOICES)
        
    context['emps'] = emps
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def details(request, id):
    context = {}
    emps = Employ.objects.filter(id=id)
    for emp in emps :
        context['emp'] = emp
    for emp in emps :
        emp.sex_str = getModelChoice(emp.sex,SEX_CHOICES)
    for emp in emps :
        emp.edu_str = getModelChoice(emp.education,EDUCATION_CHOICES)
    return render(request, 'details.html', context)

def details_dep(request, id):
    context = {}
    deps = Department.objects.get(id=id)
    emps = Employ.objects.filter(dep = deps).order_by('age')
    for emp in emps :
        emp.edu_str = getModelChoice(emp.education,EDUCATION_CHOICES)
    for emp in emps :
        emp.sex_str = getModelChoice(emp.sex,SEX_CHOICES)
    context['emp'] = emps
    
    return render(request, 'details_dep.html', context)

def department(request):
    context = {}
    emps = Employ.objects.all()
    context['emps'] = emps
    return render(request, 'department.html', context)