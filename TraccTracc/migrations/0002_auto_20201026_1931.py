# Generated by Django 3.1.2 on 2020-10-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracctracc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='year_released',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
