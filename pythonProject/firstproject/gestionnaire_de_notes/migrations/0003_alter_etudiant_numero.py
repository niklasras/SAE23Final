# Generated by Django 3.2.12 on 2024-06-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire_de_notes', '0002_remove_examen_ue_remove_ressourceue_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='numero',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
