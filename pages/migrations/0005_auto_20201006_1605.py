# Generated by Django 3.1.2 on 2020-10-06 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200923_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promotionimg',
            old_name='image',
            new_name='image_379x188',
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='image',
            new_name='image_1920x358',
        ),
    ]
