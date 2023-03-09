from django.shortcuts import render, redirect
from main.models import Post


def index(req):
    return render(req, 'index.html')
