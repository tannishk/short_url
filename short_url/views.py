from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def create(request):
    content = {

    }
    return render(request,'short_url/create.html',{})