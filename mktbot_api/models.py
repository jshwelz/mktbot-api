from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.TextField()


class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    discount_amount = models.FloatField()
    expiration_date = models.DateField()


class Redemption(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    coupon_id = models.ForeignKey("Coupon", on_delete=models.CASCADE)
    redemption_date = models.DateField()


class UserCoupon(models.Model):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    coupon_id = models.ForeignKey("Coupon", on_delete=models.CASCADE)


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
    coupon_id = models.ForeignKey("Coupon", on_delete=models.CASCADE, null=True)
    event_type = models.CharField(max_length=200)
    event_date = models.DateField()
    event_description = models.CharField(max_length=200)
