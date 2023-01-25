from django.contrib import admin
from django.urls import path,include
from . import views
from . import views
urlpatterns = [
    path('hello',views.hello_world),
    path('task',views.task),
    path('',views.home_page),
    path('analytics',views.analytics),
    path('<slug:customname>',views.redirect_url)
    path('delete/<int:pk>', views.HistoryDelete.as_view(), name='history_delete'),
    path('', views.HistoryList.as_view(), name='history'),
]