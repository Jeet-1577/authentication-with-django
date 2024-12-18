from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# password for demo
# jac.
# jac@1577

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginuser(request):
    if request.method=="POSt":
        user = request.post.get('username')
        password = request.post.get('pasword')

        # check if user has entered correct credential
        user = authenticate(username=user, password=password)
        if user is not None:
    # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
    else:
    # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect("/login")