# Generated by Django 4.0.3 on 2022-10-16 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_venue_options_alter_event_venue_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venue',
            options={'ordering': ('name',)},
        ),
    ]
