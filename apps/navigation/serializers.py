from rest_framework import serializers
from .models import NavigationSettings, NavigationItem, FooterSettings, FooterLink

class NavigationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationSettings
        fields = '__all__'

class NavigationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationItem
        fields = '__all__'

class FooterLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = '__all__'

class FooterSettingsSerializer(serializers.ModelSerializer):
    quick_links = FooterLinkSerializer(many=True, read_only=True)
    
    class Meta:
        model = FooterSettings
        fields = '__all__'
