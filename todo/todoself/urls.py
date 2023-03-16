
from django.urls import path, include
from .import views
urlpatterns = [


    path('', views.home, name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.detailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.taskupdateveiw.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteveiw.as_view(),name='cbvdelete')
]