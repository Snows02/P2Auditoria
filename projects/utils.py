from django.http import JsonResponse

def returnJSONObject(data, status):
    return JsonResponse(
        data,
        safe=False,
        status=status
    )
