# Generated by Django 5.1.6 on 2025-03-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]
