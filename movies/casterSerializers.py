
from rest_framework import serializers
from .models import Caster

class CasterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Caster
		fields = ('name', 'date', 'did', 'do')
