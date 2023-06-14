from django.http import HttpResponse
from django.shortcuts import render

def Appli_web1(request) :
    # return HttpResponse('App ProLine')
    return render(request, 'Appli_web1.html')

def Appli_web2(request) :
    #return HttpResponse('App Web Proline')
    return render(request, 'Appli_web2.html')

def Appli_web_Admin(request) :
    #return HttpResponse('Welcome Adminisatrateur')
    return render(request, 'Appli_web_Admin.html')