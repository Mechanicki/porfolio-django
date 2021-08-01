from django.urls import path

from . import views

urlpatterns = [path('',views.index,name='index'),
                path('add_post/',views.add_post,name='add_post'),
                path('delete_post/<int:pk>/',views.delete_post,name='delete_post'),
                path('delete_com/>',views.delete_com,name='delete_com'),
]