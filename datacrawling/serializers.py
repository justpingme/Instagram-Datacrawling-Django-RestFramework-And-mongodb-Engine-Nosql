from rest_framework_mongoengine.serializers import DocumentSerializer

from .models import Brand, Influencer

class BrandSerializer(DocumentSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class InfluencerSerializer(DocumentSerializer):
    class Meta:
        model = Influencer
        fields = '__all__'