from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('log/', views.detection_log, name='log'),
    path('report/', views.end_of_day_report, name='report'),
    path('export/', views.download_report_excel, name='export_report'),
]
