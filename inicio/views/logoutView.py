from django.contrib.auth import logout
from django.shortcuts import redirect

def logoutView(req):
    logout(req)
    return redirect('/')
