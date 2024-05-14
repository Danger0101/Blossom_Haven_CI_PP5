# Generated by Django 5.0.4 on 2024-05-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('S', 'Shipped'), ('D', 'Delivered'), ('C', 'Cancelled')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
