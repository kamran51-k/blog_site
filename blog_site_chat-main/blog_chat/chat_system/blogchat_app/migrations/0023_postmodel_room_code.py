# Generated by Django 4.0.1 on 2022-01-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogchat_app', '0022_alter_postmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='room_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
