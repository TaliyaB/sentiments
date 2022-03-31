    from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('visuals/', include('visuals.urls')),
    path('admin/', admin.site.urls),
]
