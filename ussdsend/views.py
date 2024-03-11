from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def ussd_handler(request):
    if request.method == 'POST':
        user_input = request.POST['name']
        response_text = f"You enetered {user_input}"
        return HttpResponse(response_text)


def sendussd(request):
    return render(request, "ssd.html")
