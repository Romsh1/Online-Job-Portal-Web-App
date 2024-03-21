from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('applicant-dashboard/', views.applicant_dashboard, name='applicant-dashboard'),
    # path('recruiter-dashboard/', views.recruiter_dashboard, name='recruiter-dashboard')
]
