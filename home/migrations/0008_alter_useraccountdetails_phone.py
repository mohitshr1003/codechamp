# Generated by Django 4.0.5 on 2022-06-26 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_userinquery_mail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountdetails',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
