from django.contrib import admin
from django.urls import path
from inicio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name='login'),
    path('project/', proyect_view, name='index'),
    path('project/<int:id_project>/', proyect_view, name='index'),
]
