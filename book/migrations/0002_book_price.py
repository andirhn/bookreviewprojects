# Generated by Django 4.1.3 on 2022-12-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
    ]
