# Generated by Django 3.2.4 on 2021-06-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=5, max_length=255),
            preserve_default=False,
        ),
    ]
