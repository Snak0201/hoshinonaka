from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from blog.models import Bureau


class BureauSerializer(ModelSerializer):
    class Meta:
        model = Bureau
        fields = "__all__"
