from django.shortcuts import render
from django.http import HttpResponse

# Import your .models here...
from .models import Hello

# Create your views here.

def index(request):
    # return HttpResponse ('Hello Py-Django!')
    return render(request, "index.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})