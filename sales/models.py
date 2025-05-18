from django.db import models
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.utils.timezone import now

# Salesperson Model (User model will act as Salesperson)
class SalesPerson(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name() or self.user.username

# Class Model
class TrainingClass(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    joined_date = models.DateField(auto_now_add=True)
    training_class = models.ForeignKey("TrainingClass", on_delete=models.CASCADE)
    salesperson = models.ForeignKey("SalesPerson", on_delete=models.SET_NULL, null=True, blank=True)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_status = models.CharField(
        max_length=20,
        choices=[('paid', 'Paid'), ('pending', 'Pending'), ('not_updated', 'Not Updated')],
        default='not_updated'
    )
    is_enrolled = models.BooleanField(default=False)  # Track enrollment status

    def __str__(self):
        return self.name

# Payment Model
class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    collected_by = models.ForeignKey(SalesPerson, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.amount_paid}"

class PendingPayment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Ensure `total_fees` is not None
        total_fees = self.student.total_fees if self.student.total_fees is not None else 0

        # Calculate total amount paid by the student
        total_paid = Payment.objects.filter(student=self.student).aggregate(total_paid=Sum('amount_paid'))['total_paid'] or 0

        # Calculate due amount
        self.due_amount = total_fees - total_paid

        # Save the instance
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - ₹{self.due_amount} Pending"


