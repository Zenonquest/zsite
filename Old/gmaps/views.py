from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from .forms import LocationForm
from .models import Coordinates

# Create your views here.
def maps_page(request):
	#form
	form = LocationForm(request.POST or None)
	if form.is_valid():
		new_coords = form.save(commit=False)
		name = form.cleaned_data['name']
		longi = form.cleaned_data['longitude']
		lati = form.cleaned_data['latitude']
		new_coords_old, created = Coordinates.objects.get_or_create(name = name, longitude = longi, latitude = lati, pub_date = timezone.now())
	
	#objects
	latest_coord_list = Coordinates.objects.order_by('-pub_date')[:1]
	context = {"form":form, "latest_coord_list":latest_coord_list}
	return render(request, 'index.html', context)




	

# class IndexView(generic.ListView):
#     template_name = 'gmaps/index.html'
#     context_object_name = 'latest_coord_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Coordinates.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]