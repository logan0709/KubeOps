# Generated by Django 3.0.4 on 2020-03-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0007_auto_20200316_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
