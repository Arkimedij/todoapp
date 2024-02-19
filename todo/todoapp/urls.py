from django.urls import path
from .import views
urlpatterns = [
    path('',views.tasklist, name = 'task'),
    path('edit/<str:pk>/',views.edit_task, name = 'edit_task'),
    path('<int:pk>/',views.Delete, name = 'delete'),
    path('timer/',views.timer,name = 'timer'),
]
