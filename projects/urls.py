from django.contrib import admin
from django.urls import path, include
from .views import updateValueLigAPIView

urlpatterns = [
    path('update/<int:id_project>/<int:id_lig>/<int:value>/', updateValueLigAPIView),
]
