from rest_framework import serializers
from sayfayapisi.models import Transaction


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
