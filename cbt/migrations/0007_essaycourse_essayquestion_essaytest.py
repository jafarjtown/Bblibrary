# Generated by Django 3.2 on 2023-10-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbt', '0006_alter_option_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='EssayQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EssayTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('questions', models.ManyToManyField(blank=True, to='cbt.EssayQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='EssayCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('topic', models.ManyToManyField(blank=True, to='cbt.EssayTest')),
            ],
        ),
    ]
