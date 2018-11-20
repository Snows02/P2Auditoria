from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user is not None and not request.user.is_anonymous:
        user = request.user
        userBussiness = Company.objects.filter(
            admin=user,
        )

        if userBussiness.count() != 0:
            return redirect('/home/')
        else:
            return redirect('/logout/')

    showAlert = False
    message = ''

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_staff:
                login(request, user)
                return redirect('/project/')

        showAlert = True
        message = 'Usuario incorrecto'

    template = get_template('inicio/login.html')
    ctx = {
        'showAlert': showAlert,
        'message': message
    }

    return HttpResponse(template.render(ctx, request))
