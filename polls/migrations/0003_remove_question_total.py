# Generated by Django 3.2.8 on 2021-10-27 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='total',
        ),
    ]
