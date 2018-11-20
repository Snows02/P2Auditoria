from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def proyect_view(request):
    return render(request, 'inicio/index.html')

# @login_required(login_url='/')
# def graphics(request):
#     return render(request, 'inicio/graficas.html')
#
# @login_required(login_url='/')
# def rgrafi(request):
# 	return redirect('grafica')
