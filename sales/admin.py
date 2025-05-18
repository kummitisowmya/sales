from django.contrib import admin
from sales.models import *

admin.site.register(SalesPerson)
admin.site.register(TrainingClass)
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(PendingPayment)
