# Generated by Django 3.1.7 on 2021-05-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
