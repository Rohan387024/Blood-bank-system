# Generated by Django 2.1.5 on 2019-03-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='pincode',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]