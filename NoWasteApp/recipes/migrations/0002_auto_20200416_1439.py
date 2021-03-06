# Generated by Django 2.2.12 on 2020-04-16 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('plural', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('unit_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='recipes',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='course',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.CreateModel(
            name='Tag_set',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipes')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient_set',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('quantity', models.FloatField()),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Ingredients')),
                ('measure_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Measure')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipes')),
            ],
        ),
    ]
