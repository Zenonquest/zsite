from django import forms

from .models import Site, SiteLink

class LocationForm(forms.ModelForm):
	class Meta:
		model = Site
		fields = "site_text"

