from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicos/', include('doctors.urls')),
]
urlpatterns += [
    path('', lambda request: HttpResponseRedirect('/medicos/')),
]