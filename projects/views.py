from django.views.decorators.csrf import csrf_exempt
from .utils import returnJSONObject

@csrf_exempt
def updateValueLigAPIView(req, id_project, id_lig, value):
    if req.method != 'POST':
        return returnJSONObject({'err':'bad method'}, 403)

    from .models import Project_SubNumeral

    project = Project_SubNumeral.objects.filter(id=id_lig, project__id=id_project)

    if project.count() == 0:
        return returnJSONObject({'err':'not found'}, 400)

    project = project[0]
    project.level = value
    project.save()

    return returnJSONObject({'ok':'ok'}, 200)
