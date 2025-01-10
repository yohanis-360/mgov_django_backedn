# admin_panel/urls.py
from django.urls import path
from .views import app_approval_page, approve_app, reject_app,request_revision

urlpatterns = [
    path('approvals/', app_approval_page, name='app_approval_page'),
    path('approve/<int:app_id>/', approve_app, name='approve_app'),
    path('reject/<int:app_id>/', reject_app, name='reject_app'),
    path('request_revision/<int:app_id>/', request_revision, name='request_revision'),
]
