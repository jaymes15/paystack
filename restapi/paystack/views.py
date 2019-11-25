from django.shortcuts import render
import json
import requests

# Create your views here.
def banklist(request):
    response = requests.get("https://api.paystack.co/bank?gateway=emandate&pay_with_bank=true")
    if response.status_code == 200:
    	result = response.json()
    	banks = result['data']
    	context = {'banks':banks}
    	return render(request,'paystack/banklist.html',context)

def bankdetail(request, bank_id):
    response = requests.get("https://api.paystack.co/bank?gateway=emandate&pay_with_bank=true")
    if response.status_code == 200:
    	result = response.json()
    	banks = result['data']
    	for bank in banks:
    		if bank['id'] == bank_id:
    			bank_detail = bank
    		else:
    			error = 'bank not found'	
    	context = {'bank_detail':bank_detail,'error':error}
    	return render(request,'paystack/bankdetail.html',context)    	