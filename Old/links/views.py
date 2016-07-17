from django.shortcuts import render
from django.views.generic import ListView
from .models import Link, Vote

# Create your views here.
def links_page(request):
	return render(request, 'links/index.html')