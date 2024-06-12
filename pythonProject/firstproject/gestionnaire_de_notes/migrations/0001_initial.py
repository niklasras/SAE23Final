# Generated by Django 5.0.6 on 2024-06-02 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10, unique=True)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('groupe', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('coefficient', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('semestre', models.CharField(max_length=10)),
                ('credit_ects', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.FloatField()),
                ('appreciation', models.TextField()),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='gestionnaire_de_notes.etudiant')),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='gestionnaire_de_notes.examen')),
            ],
        ),
        migrations.CreateModel(
            name='RessourceUE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('descriptif', models.TextField()),
                ('coefficient', models.FloatField()),
                ('ue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ressources', to='gestionnaire_de_notes.ue')),
            ],
        ),
        migrations.AddField(
            model_name='examen',
            name='ue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examens', to='gestionnaire_de_notes.ue'),
        ),
    ]
