from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('bigfootreports/', views.BigFootReportListView.as_view(), name="bigfootreports"),
  path('bigfootreport/<int:pk>', views.BigFootReportDetailView.as_view(), name='report-detail'),
]
