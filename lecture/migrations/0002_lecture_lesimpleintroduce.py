# Generated by Django 2.0.9 on 2018-10-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='leSimpleIntroduce',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
