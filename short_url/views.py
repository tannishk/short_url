from django.shortcuts import render,redirect
from django.http import HttpResponse
from short_url.forms import OneForm
from short_url.models import One
# Create your views here.

def ma(a):
    ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ALPHABET[a]

def create(request):
    if request.method == 'POST':
        form = OneForm(request.POST)
        if form.is_valid():
            #form.save(commit=True)
            temp = One()
            temp.absolute_url = form.cleaned_data['absolute_url']
            temp.save()
            temp = One.objects.get(absolute_url = form.cleaned_data['absolute_url'])
            id = temp.pk
            li = []
            while(id>0):
                li.append(id%62)
                id = id/62
            li.reverse()
            ur = ""
            for i in li:
                ur = ur+ma(i)
            temp.relative_url = ur
            temp.save()
            return saved(request,ur)
        else:
            print form.errors
    else:
        form = OneForm()
    content = {
        'form':form
    }
    return render(request,'short_url/create.html',content)


def saved(request,ur):

    return HttpResponse('<h1> saved </h1>'+ur)

def re(request,ur):
    text = One.objects.get(relative_url=ur)
    ##text=One()
    a = "https://"+text.absolute_url
    return redirect(a)

def list(request):
    li = One.objects.all()
    context = {
        'li':li
    }
    return render(request,'short_url/list.html',context)