from django.urls import path

from . import views

urlpatterns = [path('',views.index,name='index'),
                path('add_post/',views.add_post,name='add_post'),
                path('delete_post/<int:pk>/',views.delete_post,name='delete_post'),
                path('delete_com/',views.delete_com,name='delete_com'),
                path('about_me/',views.about_me,name='about_me'),

                path('profile/<int:pk>',views.profile,name='profile'),

                path('dashboard/',views.Dashboard.as_view(),name = 'dashboard'),
                path('test/',views.test,name = 'test'),

                path('login/',views.loginPage,name = 'login'),
                path('register/',views.registerPage,name = 'register'),
                path('logout',views.logoutUser,name = 'logout')
]