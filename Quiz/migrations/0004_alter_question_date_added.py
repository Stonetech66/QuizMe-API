# Generated by Django 4.0.5 on 2022-09-01 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_question_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
