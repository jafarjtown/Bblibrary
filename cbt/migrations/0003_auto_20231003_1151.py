# Generated by Django 3.2 on 2023-10-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbt', '0002_alter_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='option',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]