# Generated by Django 2.0.7 on 2018-07-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
