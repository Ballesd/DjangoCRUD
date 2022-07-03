from xml.dom.minidom import Document
from django.urls import URLPattern, path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('inicial',views.index, name='inicial'),
    path('proveedor',views.proveedor, name='proveedor'),
    path('proveedor/crear',views.crear_proveedor, name='crear'),
    path('proveedor/editar/<int:id>',views.editar_proveedor, name='editar'),
    path('proveedor/<int:id>',views.borrar_proveedor, name='eliminar'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)