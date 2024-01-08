# Generated by Django 5.0.1 on 2024-01-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_physician_about_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='physician',
            name='us_city',
            field=models.CharField(default='Austin', max_length=250),
        ),
        migrations.AddField(
            model_name='physician',
            name='us_state',
            field=models.CharField(choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('NC', 'New Hampshire'), ('ND', 'North Dakota'), ('NE', 'Colorado'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New Hampshire'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'New Hampshire'), ('SD', 'Oklahoma'), ('TN', 'Oregon'), ('TX', 'Texas'), ('UT', 'Rhode Island'), ('VA', 'Virginia'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], default='TX', max_length=2),
        ),
        migrations.AlterField(
            model_name='physician',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='physician',
            name='last_name',
            field=models.CharField(max_length=250),
        ),
    ]
