from rest_framework import serializers
from .models import NavigationSettings, NavigationItem, FooterSettings

class NavigationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationSettings
        fields = '__all__'

class NavigationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationItem
        fields = '__all__'

class FooterSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSettings
        fields = '__all__'
