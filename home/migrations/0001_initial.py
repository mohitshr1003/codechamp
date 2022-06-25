# Generated by Django 4.0.5 on 2022-06-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail_id', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]