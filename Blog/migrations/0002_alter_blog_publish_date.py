# Generated by Django 4.0.3 on 2022-11-28 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
