import requests
import base64
import datetime
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MpesaPayment

def get_access_token():
    """ Get OAuth token from Safaricom API """
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    response = requests.get(api_url, auth=(consumer_key, consumer_secret))
    return response.json().get("access_token")

def generate_password():
    """ Generate the base64 encoded password """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    data_to_encode = settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp
    password = base64.b64encode(data_to_encode.encode()).decode("utf-8")
    return password, timestamp

@api_view(["POST"])
def stk_push(request):
    """ Initiate M-Pesa STK Push """
    phone_number = request.data.get("phone_number")
    amount = request.data.get("amount")

    if not phone_number or not amount:
        return Response({"error": "Phone number and amount are required"}, status=400)

    access_token = get_access_token()
    password, timestamp = generate_password()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": settings.CALLBACK_URL,
        "AccountReference": "Healthxxx",
        "TransactionDesc": "Payment for Healthx services",
    }

    response = requests.post(api_url, json=payload, headers=headers)
    res_data = response.json()

    if res_data.get("ResponseCode") == "0":
        MpesaPayment.objects.create(
            phone_number=phone_number,
            amount=amount,
            merchant_request_id=res_data.get("MerchantRequestID"),
            checkout_request_id=res_data.get("CheckoutRequestID"),
            status="Pending",
        )

    return Response(res_data)

@api_view(["POST"])
def mpesa_callback(request):
    """ Handle M-Pesa callback response """
    callback_data = request.data.get("Body", {}).get("stkCallback", {})
    result_code = callback_data.get("ResultCode")
    merchant_request_id = callback_data.get("MerchantRequestID")
    checkout_request_id = callback_data.get("CheckoutRequestID")

    if result_code == 0:
        amount = callback_data["CallbackMetadata"]["Item"][0]["Value"]
        mpesa_receipt_number = callback_data["CallbackMetadata"]["Item"][1]["Value"]
        transaction_date = callback_data["CallbackMetadata"]["Item"][2]["Value"]

        MpesaPayment.objects.filter(merchant_request_id=merchant_request_id).update(
            status="Completed",
            mpesa_receipt_number=mpesa_receipt_number,
            transaction_date=datetime.datetime.strptime(str(transaction_date), "%Y%m%d%H%M%S"),
        )

        return Response({"message": "Payment successful"}, status=200)

    else:
        MpesaPayment.objects.filter(merchant_request_id=merchant_request_id).update(status="Failed")
        return Response({"message": "Payment failed"}, status=400)
