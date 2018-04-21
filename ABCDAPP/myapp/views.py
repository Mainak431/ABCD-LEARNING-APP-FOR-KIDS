from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect, get_object_or_404

from .models import *

from django.utils import timezone

from django.contrib.auth import logout, update_session_auth_hash

from django.contrib import messages

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth import authenticate, login

from django.contrib.auth.models import Group, User

from django.urls import reverse

from django.db.models import Q
from random import shuffle
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    return render(request, 'start.html', {})


def letter(request, pk):
    try:
        pk = str(int(pk) + 1)
        d = letters.objects.get(id=pk)
        di = letters.objects.get(id=pk).correct
        di1 = letters.objects.get(id=pk).incorrect1
        di2 = letters.objects.get(id=pk).incorrect2
        di3 = letters.objects.get(id=pk).incorrect3
        list = []
        list.append(di)
        list.append(di1)
        list.append(di2)
        list.append(di3)
        shuffle(list)
        for i in range(len(list)):
            if list[i] == di:
                index = i
                break
        return render(request, 'a.html', {'d': d, 'c': list[0], 'e': list[1], 'f': list[2], 'g': list[3], 'index': index})
    except:
        return render(request, 'start.html', {})

def check(request, pk, pkl, ind):
    d = letters.objects.get(id=pk)
    if pkl == ind:
        return render(request, 'right.html', {'d': d,})
    else:
        return render(request, 'wrong.html', {'d': d})


def redirect(request,pk):
    d = letters.objects.get(id=pk)
    di = letters.objects.get(id=pk).correct
    di1 = letters.objects.get(id=pk).incorrect1
    di2 = letters.objects.get(id=pk).incorrect2
    di3 = letters.objects.get(id=pk).incorrect3
    list = []
    list.append(di)
    list.append(di1)
    list.append(di2)
    list.append(di3)
    shuffle(list)
    for i in range(len(list)):
        if list[i] == di:
            index = i
            break
    return render(request, 'a.html', {'d': d, 'c': list[0], 'e': list[1], 'f': list[2], 'g': list[3], 'index': index})
