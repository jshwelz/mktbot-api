from rest_framework import serializers

from mktbot_api.models import Coupon, Redemption, User, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name"]


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "id",
            "name",
            "description",
            "price",
            "discount_amount",
            "expiration_date",
        ]


class RedeemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redemption
        fields = ["user_id", "coupon_id", "redemption_date"]


class ResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    response = serializers.CharField()


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "user_id",
            "coupon_id",
            "event_type",
            "event_date",
            "event_description",
        ]
