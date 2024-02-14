from django.urls import path
from .import views
urlpatterns = [
    path('',views.tasklist, name = 'task'),
    path('edit/<str:pk>/',views.edit, name = 'edittask'),
    path('timer/',views.timer,name = 'timer'),
]
