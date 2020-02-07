from django.shortcuts import render
from django.http import HttpResponse

# Import your .models here...
from .models import Hello

# Create your views here.

def index(request):
    # return HttpResponse ('Hello Py-Django!')
    return render(request, "index.html")

def db(request):

    hello = Hello()
    hello.save()

    hellos = Hello.objects.all()

    return render(request, "db.html", {"hellos": hellos})