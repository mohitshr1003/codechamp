# Generated by Django 4.0.5 on 2022-06-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_useraccountdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountdetails',
            name='rollno',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
