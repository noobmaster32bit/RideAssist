from rest_framework import serializers

from api.models import Customer



class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer

        fileds = "__all__"

        read_only_fields=["id", "created_date", "updated_date", "is_active"]
        