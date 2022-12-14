# Generated by Django 4.0.3 on 2022-11-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_venue_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='book',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='venue',
            name='owner',
            field=models.PositiveIntegerField(default=1, verbose_name='Venue Owner'),
        ),
    ]
