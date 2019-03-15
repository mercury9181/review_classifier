from django.urls import path

from . import views

urlpatterns = [

path('',views.allblogs, name= 'allblogs'),
path('<int:blog_id>/',views.detail, name= 'detail'),
path('givereview',views.givereview, name= 'givereview'),
path('rc',views.rc, name= 'rc'),
path('search',views.search, name= 'search'),

]
