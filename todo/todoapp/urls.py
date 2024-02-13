from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name = 'home'),
    path('task/',views.tasklist, name = 'task'),
    path('timer/',views.timer,name = 'timer'),
    
]
