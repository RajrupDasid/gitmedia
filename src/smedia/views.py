from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    #return HttpResponse("Hello world")
    user=request.user
    message='hello world'
    context={
        'user':user,
        'message':message,
    }
    return render(request,'home.html',context)