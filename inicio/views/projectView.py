from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from projects.models import *
from numerals.models import *

@login_required(login_url='/')
def proyect_view(req):
    template = get_template('inicio/index.html')

    projects = Project.objects.filter(admin=req.user)
    project = None
    if projects.count() == 0:
        project = Project(name='Proyecto de prueba para usuario (tutorial)', admin=req.user)
        project.save()
    else:
        project = projects[0]

    project_ligs = Project_SubNumeral.objects.filter(project=project)

    titles = Title.objects.all()


    for title in titles:
        title.numerals = Numeral.objects.filter(title=title)
        for indexNumeral in range(0, len(title.numerals)):
            numeral = title.numerals[indexNumeral]
            title.numerals[indexNumeral].subnumerals = Project_SubNumeral.objects.filter(subnumeral__numeral=numeral, project=project)

    ctx = {
        'titles': titles,
        'email': req.user.email
    }

    return HttpResponse(template.render(ctx, req))
