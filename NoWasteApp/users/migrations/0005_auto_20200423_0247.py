# Generated by Django 3.0.5 on 2020-04-23 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200423_0239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='website',
            new_name='site',
        ),
    ]