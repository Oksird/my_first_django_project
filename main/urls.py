from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('create',views.create, name='create'),
    path('delete/<int:pk>',views.delete_task, name='delete_task'),
    path('update/<int:pk>', views.update_task, name ='update_task')
]
