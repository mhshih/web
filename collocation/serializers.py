from .models import Collocation
from rest_framework import serializers


class CollocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Collocation
        fields=('url','keyword','collocate')
