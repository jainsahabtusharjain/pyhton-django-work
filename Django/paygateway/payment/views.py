from django.shortcuts import render

# Create your views here.
price = 80
def home(request):
    return render(request, 'payment/index.html',{'pz' : price})

def paypal(request):
    return render(request, 'payment/payment.html', {'pz' : price})