# Generated by Django 2.2.12 on 2020-04-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(max_length=32, primary_key=True, serialize=False, unique=True),
        ),
    ]