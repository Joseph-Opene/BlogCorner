# Generated by Django 3.1.7 on 2021-05-15 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210515_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='quote',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]