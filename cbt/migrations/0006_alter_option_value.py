# Generated by Django 3.2 on 2023-10-03 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbt', '0005_auto_20231003_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='value',
            field=models.CharField(max_length=500),
        ),
    ]
