from rest_framework.generics import (
    GenericAPIView,
)
from mktbot_api.models import Coupon, Redemption, Transaction, User
from chatbot_model.chatbot_model import MktBotModel
from rest_framework.response import Response
from mktbot_api.serializers import (
    RedeemSerializer,
    ResponseSerializer,
    UserSerializer,
    TransactionSerializer,
)
from rest_framework import status
from datetime import date


class ChatbotResponse(GenericAPIView):
    serializer_class = ResponseSerializer

    def post(self, request):
        mkt = MktBotModel()
        mkt.preprocessing()
        response = mkt.compute_prediction(request.data["query_input"])
        user_id = None

        if request.data["user_id"] is not None and request.data["user_id"] != "":
            usr = User.objects.get(id=request.data["user_id"])
            user_id = usr.id
        else:
            user = UserSerializer(data={"name": request.data["username"]})
            if user.is_valid():
                userobj = user.save()
                user_id = userobj.id

        data = {
            "user_id": user_id,
            "name": response["tag"],
            "response": response["response"],
        }

        serializer = ResponseSerializer(data=data)
        if serializer.is_valid():
            coupon = Coupon.objects.get(id=1)
            trans = TransactionSerializer(
                data={
                    "user_id": user_id,
                    "coupon_id": coupon.id,
                    "event_type": data["name"],
                    "event_date": date.today(),
                    "event_description": "loggin",
                }
            )
            if trans.is_valid():
                trans.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RevealCoupon(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        coupon = Coupon.objects.get(id=1)
        redeem = RedeemSerializer(
            data={
                "user_id": request.data["user_id"],
                "coupon_id": coupon.id,
                "redemption_date": date.today(),
            }
        )
        if redeem.is_valid():
            redeem.save()
            return Response(
                {"status": "success", "data": redeem.data}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "error", "data": redeem.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ChatStats(GenericAPIView):
    def get(self, request):
        coupons = Redemption.objects.count()
        turndowns = Transaction.objects.filter(event_type="turndown").count()
        return Response(
            {
                "status": "success",
                "data": {"coupons_redeem": coupons, "turndown": turndowns},
            },
            status=status.HTTP_200_OK,
        )
