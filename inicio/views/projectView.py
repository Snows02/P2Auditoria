from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from projects.models import *
from numerals.models import *

@login_required(login_url='/')
def proyect_view(req, id_project=None):
    template = get_template('inicio/index.html')

    if req.method == "POST":
        id_lig = req.POST.get('id_lig')
        id_proyect = req.POST.get('id_proyect')
        id_subnumeral = req.POST.get('id_subnumeral')

        lig = Project_SubNumeral.objects.filter(subnumeral__id=id_subnumeral, project__id=id_project, id=id_lig)

        if lig.count() != 0:
            lig = lig[0]
            print(req.FILES.get('file'))
            lig.file = req.FILES.get('file')
            lig.save()

    projects = Project.objects.filter(admin=req.user)
    project = None
    if projects.count() == 0:
        project = Project(name='Proyecto de prueba para usuario (tutorial)', admin=req.user)
        project.save()
        return redirect('/project/' + str(project.id) + '/')

    projects = Project.objects.filter(admin=req.user)
    project = Project.objects.filter(admin=req.user, id=id_project)

    if project.count() == 0:
        id = projects[0].id
        return redirect('/project/' + str(id) + '/')

    project = project[0]
    project_ligs = Project_SubNumeral.objects.filter(project=project)

    titles = Title.objects.all()


    for title in titles:
        title.numerals = Numeral.objects.filter(title=title)
        for indexNumeral in range(0, len(title.numerals)):
            numeral = title.numerals[indexNumeral]
            title.numerals[indexNumeral].subnumerals = Project_SubNumeral.objects.filter(subnumeral__numeral=numeral, project=project)

    ctx = {
        'projects': projects,
        'id_project': id_project,
        'titles': titles,
        'email': req.user.email
    }

    return HttpResponse(template.render(ctx, req))
