from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class EtudiantForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ('nom', 'prenom', 'groupe', 'photo', 'email')
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'groupe': _('Groupe'),
            'photo': _('Photo'),
            'email': _('@Email')
        }

class UEForm(ModelForm):
    class Meta:
        model = models.UE
        fields = ('code', 'nom', 'semestre', 'credit_ects')
        labels = {
            'code': _('Code'),
            'nom': _('Nom'),
            'semestre': _('Semestre'),
            'credit_ects': _('Crédit ECTS'),
        }

class RessourceUEForm(ModelForm):
    class Meta:
        model = models.RessourceUE
        fields = ('code_ressource', 'nom', 'descriptif', 'coefficient', 'ue', 'enseignant')
        labels = {
            'code_ressource': _('Code Ressource'),
            'nom': _('Nom'),
            'descriptif': _('Descriptif'),
            'coefficient': _('Coefficient'),
            'ue': _('UE'),
            'enseignant': _('Enseignant')
        }

class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('id', 'nom', 'prenom')
        labels = {
            'id': _('ID'),
            'nom': _('Nom'),
            'prenom': _('Prénom'),
        }

class ExamenForm(ModelForm):
    class Meta:
        model = models.Examen
        fields = ('titre', 'date', 'coefficient', 'ressource_ue')
        labels = {
            'titre': _('Titre'),
            'date': _('Date'),
            'coefficient': _('Coefficient'),
            'ressource_ue': _("Ressource associée à l'examen")
        }

class NoteForm(ModelForm):
    class Meta:
        model = models.Note
        fields = ('examen', 'etudiant', 'note', 'appreciation')
        labels = {
            'examen': _('Examen'),
            'etudiant': _('Étudiant'),
            'note': _('Note'),
            'appreciation': _('Appréciation'),
        }
