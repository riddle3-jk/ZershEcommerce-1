# Generated by Django 3.1.2 on 2020-10-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_payment_pay_on_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
