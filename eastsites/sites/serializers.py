from rest_framework import serializers
from sites.models import Sites

#sites serializers
class SiteSerializers (serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = '__all__'