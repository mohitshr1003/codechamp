# Generated by Django 4.0.5 on 2022-06-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_userinquery_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinquery',
            name='message',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]