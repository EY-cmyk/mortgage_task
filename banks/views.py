from django.shortcuts import render


# Create your views here.

def banks_main(request):
    return render(request, 'banks/banks_main.html')
