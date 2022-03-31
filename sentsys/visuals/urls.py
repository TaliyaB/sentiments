from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.upload, name='visuals'),
    path('visuals', views.visuals, name='visuals'),
    path('data', views.data, name='data'),
    path('lda', views.data, name='lda'),
    path('admin/', admin.site.urls),
]
