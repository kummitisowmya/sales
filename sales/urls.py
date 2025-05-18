from django.urls import path

from sales import views
from sales.views import *

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('home/', sales_home, name='sales_home'),
    path('dashboard/', sales_dashboard, name='sales_dashboard'),
    path('enroll-student/', enroll_student, name='enroll_student'),
    path('record-payment/<int:student_id>/', record_payment, name='record_payment'),
    path('pending-payments/', view_pending_payments, name='view_pending_payments'),
    path('create-pending-payment/<int:student_id>/', create_pending_payment, name='create_pending_payment'),
    path('add-user/', add_user, name='add_user'),
    path('add-class/', add_class, name='add_class'),
    path('download-excel/', views.download_sales_excel, name='download_sales_excel'),

]
