from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'active_dash': 'active'
    }
    return render(request, 'page/dashboard/dashboard.html', data)

def projet(request):
    data = {
        'active_projets': 'active'
    }
    return render(request, 'page/dashboard/list_projet.html', data)

def list_user(request):
    data = {
        'active_users': 'active'
    }
    return render(request, 'page/dashboard/users.html', data)

def detailuser(request):
    return render(request, 'page/dashboard/detail_user.html')

def projetdetail(request):
    return render(request, 'page/dashboard/projetdetail.html')

def commit(request):
    return render(request, 'page/dashboard/commit.html')

def commits(request):
    return render(request, 'page/dashboard/commits.html')

def newproject(request):
    return render(request, 'page/dashboard/createproject.html')

def newusetask(request):
    return render(request, 'page/dashboard/addusertache.html')

def connexion(request):
    return render(request, 'page/dashboard/connexion.html')

