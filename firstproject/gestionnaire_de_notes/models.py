from django.db import models
from django.utils.crypto import get_random_string

class Enseignant(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"Enseignant {self.prenom} {self.nom} (ID: {self.id})"
        return chaine

    def dico(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
        }

class UE(models.Model):
    code = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    semestre = models.CharField(max_length=30)
    credit_ects = models.CharField(max_length=50)

    def __str__(self):
        chaine = f"L'UE {self.nom} du semestre {self.semestre} ayant le code {self.code} et le crédit ECTS {self.credit_ects}"
        return chaine

    def dico(self):
        return {
            "code": self.code,
            "nom": self.nom,
            "semestre": self.semestre,
            "credit_ects": self.credit_ects
        }

class RessourceUE(models.Model):
    code_ressource = models.CharField(max_length=30, default='default_code_ressource')
    nom = models.CharField(max_length=100)
    descriptif = models.TextField()
    coefficient = models.DecimalField(max_digits=5, decimal_places=2)
    ue = models.ForeignKey('UE', on_delete=models.CASCADE, default=1)
    enseignant = models.ForeignKey('Enseignant', on_delete=models.CASCADE, default=1)

    def __str__(self):
        chaine = f"{self.code_ressource}"
        return chaine

    def dico(self):
        return {
            "code_ressource": self.code_ressource,
            "nom": self.nom,
            "descriptif": self.descriptif,
            "coefficient": self.coefficient,
            "ue": self.ue,
            "enseignant": self.enseignant,
        }

class Examen(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    date = models.DateField()
    coefficient = models.DecimalField(max_digits=5, decimal_places=2)
    ressource_ue = models.ForeignKey('RessourceUE', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.titre} - {self.date}"

    def dico(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "date": self.date,
            "coefficient": self.coefficient,
            "ressource_ue": self.ressource_ue,
        }

class Etudiant(models.Model):
    numero = models.CharField(max_length=30, unique=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    groupe = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='gestionnaire_de_notes/media/photo')
    email = models.EmailField(unique=True)

    def __str__(self):
        chaine = f"{self.prenom} {self.nom}"
        return self.nom
        return chaine

    def dico(self):
        return {
            "numero": self.numero,
            "nom": self.nom,
            "prenom": self.prenom,
            "groupe": self.groupe,
            "photo": self.photo,
            "email": self.email
        }

    def save(self, *args, **kwargs):
        if not self.numero:
            self.numero = self.generate_numero()
        super().save(*args, **kwargs)

    def generate_numero(self):
        return get_random_string(3)


class Note(models.Model):
    examen = models.ForeignKey("Examen", on_delete=models.CASCADE)
    etudiant = models.ForeignKey("Etudiant", on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)
    appreciation = models.TextField()

    def __str__(self):
        return f"{self.etudiant} - Note: {self.note}"

    def dico(self):
        return {
            "examen": self.examen,
            "etudiant": self.etudiant,
            "note": self.note,
            "appreciation": self.appreciation,
        }
