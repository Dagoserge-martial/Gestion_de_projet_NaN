from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from . import models
# Create your views here.
def home(request):
    return render(request, 'page/dashboard/dashboard.html')

def projet(request):
    return render(request, 'page/dashboard/list_projet.html')

def list_user(request):
    return render(request, 'page/dashboard/users.html')

def detailuser(request):
    return render(request, 'page/dashboard/detail_user.html')

def projetdetail(request):
    return render(request, 'page/dashboard/projetdetail.html')

def commit(request):
    return render(request, 'page/dashboard/commit.html')

def commits(request):
    return render(request, 'page/dashboard/commits.html')

def newproject(request):
    clt = models.Client.objects.filter(statut=True)
    data = {
        'clt': clt,
    }
    return render(request, 'page/dashboard/createproject.html', data)

def newusetask(request):
    return render(request, 'page/dashboard/addusertache.html')

def connexion(request):
    return render(request, 'page/dashboard/connexion.html')

