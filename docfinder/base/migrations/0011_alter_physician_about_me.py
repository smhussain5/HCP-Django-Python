# Generated by Django 5.0.1 on 2024-01-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_physician_about_me_alter_physician_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physician',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
    ]