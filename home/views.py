from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render



# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation

from home.models import *


def index(request):
    header = Header.objects.all().order_by('-id')[0:1]  
    slider = Web_Slider.objects.all().order_by('-id')[0:1]  

    context={
        'header':header,
        'slider':slider,
    }
    return render(request,'index.html',context)
