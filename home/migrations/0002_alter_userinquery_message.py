# Generated by Django 4.0.5 on 2022-06-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinquery',
            name='message',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]