from django.contrib import admin
from .models import MpesaPayment

@admin.register(MpesaPayment)
class MpesaPaymentAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'amount', 'mpesa_receipt_number', 'transaction_date', 'status')
    search_fields = ('phone_number', 'mpesa_receipt_number', 'merchant_request_id', 'checkout_request_id')
    list_filter = ('status', 'transaction_date')
    ordering = ('-transaction_date',)
