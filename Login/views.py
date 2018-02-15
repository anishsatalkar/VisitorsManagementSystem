from django.contrib.auth import authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def login_user(request):
    # user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponseRedirect('/home/add_visitor/',{'user_data' : username})
        else:
            return HttpResponse('invalid credentials')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')
