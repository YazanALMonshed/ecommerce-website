# Generated by Django 3.0 on 2020-03-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
