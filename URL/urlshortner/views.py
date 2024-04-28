from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import Rawform
from .models import url
import pyshorteners
from pyshorteners.exceptions import BadURLException
def home(request):
    s =''
    form = Rawform()
    if request.method == "POST":
        form  = Rawform(request.POST)
        if form.is_valid():
            url.objects.create(**form.cleaned_data)
            print('Data Inserted')
            s = form.cleaned_data['url1']
            # print(url_data)
    form = Rawform()
    x = shorten_url(s)
    if x:
        print("Shortened URL:", x)
        
    context = {
        'form' : form,
        'shortenurl'  : x
    } 
    return render(request,  'home.html' , context)
def shorten_url(s):
    try:
        # Validate the URL
        if not s.startswith(('http://', 'https://')):
            raise ValueError("Invalid URL format")

        # Shorten the URL
        shortener = pyshorteners.Shortener()
        x = shortener.tinyurl.short(s)
        return x
    except BadURLException as e:
        print("Error:", e)
        return None
    except ValueError as e:
        print("Error:", e)
        return None



