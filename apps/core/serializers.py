from rest_framework import serializers
from .models import GlobalStyles

class GlobalStylesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalStyles
        fields = '__all__'
