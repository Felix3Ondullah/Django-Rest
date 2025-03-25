from django.db import models

class MpesaPayment(models.Model):
    phone_number = models.CharField(max_length=13)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    merchant_request_id = models.CharField(max_length=100, null=True, blank=True)
    checkout_request_id = models.CharField(max_length=100, null=True, blank=True)
    mpesa_receipt_number = models.CharField(max_length=50, null=True, blank=True)
    transaction_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"
