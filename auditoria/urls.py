from django.contrib import admin
from django.urls import path, include
from inicio.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name='login'),
    path('logout/',logoutView, name='logout'),
    path('project/', proyect_view, name='index'),
    path('project/<int:id_project>/', proyect_view, name='index'),
    path('api/project/', include('projects.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
