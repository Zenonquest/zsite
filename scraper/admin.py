from django.contrib import admin

# Register your models here.
from .models import Link, Site
admin.site.register(Site)
admin.site.register(Link)
