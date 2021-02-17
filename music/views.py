from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def promotion(request):
    return render(request, 'promotion.html')

def torronut(request):
    return render(request, 'torronut.html')

def dashboard(request):
    return render(request, 'dashboard.html')
 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(
                request, "You entered incorrect username or password")
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password, first_name=firstName, last_name=lastName, email=email)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return render(request, 'index.html')
    return render(request, 'signup.html')

def usernameCheck(request):
    username = request.GET.get('username', None)
    flag = 1
    users = User.objects.all()
    

    for user in users:
        if user.username == username:
            flag = 0
            break     
                    
    data = {
        'flag': flag
    }
    
    return JsonResponse(data)