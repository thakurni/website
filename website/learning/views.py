from django.shortcuts import render
from django.http import HttpResponse,request



# Create your views here.
def home(request):
    return render(request,'index.html')

def topics(request):
    data=['math','Datascience','web development']
    return render(request,'topics.html',{'topics':data})
