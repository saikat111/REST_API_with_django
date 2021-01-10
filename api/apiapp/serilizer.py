from rest_framework import serializers
from .models import Categories


class categoriesSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'