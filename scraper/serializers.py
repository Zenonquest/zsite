from rest_framework import serializers
from .models import Site, Link

class SiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Site

class LinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Link