from django.shortcuts import render

# Create your views here.
def page_login(request):
    return render(request, 'login/pages/login.html')