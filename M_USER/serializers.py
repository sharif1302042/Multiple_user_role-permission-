from rest_framework import serializers

from .models import UserProfile, Account, TopUP


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class TopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopUP
        fields = "__all__"
