# Generated by Django 4.2.1 on 2023-05-23 23:30

from django.db import migrations

def save_coupon(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Coupon = apps.get_model("mktbot_api", "Coupon")
    obj = Coupon(name = "prueba1",description = "10% Limit one per customer", price = 300, discount_amount= 10, expiration_date = '2023-10-10')    
    obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('mktbot_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(save_coupon),
    ]
