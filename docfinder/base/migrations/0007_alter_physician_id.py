# Generated by Django 5.0.1 on 2024-01-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_physician_taking_new_pts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physician',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
