# Generated by Django 2.0.7 on 2022-02-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(default='new', max_length=10000),
            preserve_default=False,
        ),
    ]
