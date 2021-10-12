# likes/api/serializers.py

from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class FanSerializer(serializers.ModelSerializer):
    # email = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name'
        )

