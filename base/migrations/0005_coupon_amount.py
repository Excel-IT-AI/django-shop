# Generated by Django 4.0.1 on 2022-02-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_user_coupon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(blank=True, default=20),
            preserve_default=False,
        ),
    ]
