from django.shortcuts import render

def dashboard(request):
    return render(request, 'transactions/index.html') # Added 'transactions/'