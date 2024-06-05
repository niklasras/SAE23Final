from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant, UE, RessourceUE, Enseignant, Examen, Note
from django.http import HttpResponse
from .forms import EtudiantForm, UEForm, RessourceUEForm, EnseignantForm, ExamenForm, NoteForm

def accueil(request):
    notes = Note.objects.select_related('etudiant', 'examen__ressource_ue__ue', 'examen__ressource_ue__enseignant').all()
    return render(request, 'gestionnaire_de_notes/accueil.html', {'notes': notes})

# Etudiant views
def generate_report_txt(request, etudiant_id):
    etudiant = Etudiant.objects.get(pk=etudiant_id)
    notes = Note.objects.filter(etudiant=etudiant)

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="releve_notes_{etudiant.nom}_{etudiant.prenom}.txt"'

    lines = [
        f"Relevé de notes pour {etudiant.nom} {etudiant.prenom}\n",
        f"N° Étudiant: {etudiant.numero}\n",
        f"Groupe: {etudiant.groupe}\n",
        f"Email: {etudiant.email}\n\n",
        "Notes:\n"
    ]

    for note in notes:
        lines.append(f"{note.examen.titre}: {note.note} ({note.appreciation})\n")

    response.writelines(lines)
    return response

def etudiant_list(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'gestionnaire_de_notes/Etudiants/liste.html', {'etudiants': etudiants})

def etudiant_create(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('etudiant_list')
    else:
        form = EtudiantForm()
    return render(request, 'gestionnaire_de_notes/Etudiants/ajout.html', {'form': form})

def etudiant_update(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiant_list')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'gestionnaire_de_notes/Etudiants/update.html', {'form': form})

def etudiant_delete(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('etudiant_list')
    return render(request, 'gestionnaire_de_notes/Etudiants/delete.html', {'etudiant': etudiant})

# UE views
def ue_list(request):
    ues = UE.objects.all()
    return render(request, 'gestionnaire_de_notes/Ue/liste.html', {'ues': ues})

def ue_create(request):
    if request.method == 'POST':
        form = UEForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ue_list')
    else:
        form = UEForm()
    return render(request, 'gestionnaire_de_notes/Ue/ajout.html', {'form': form})

def ue_update(request, pk):
    ue = get_object_or_404(UE, pk=pk)
    if request.method == 'POST':
        form = UEForm(request.POST, instance=ue)
        if form.is_valid():
            form.save()
            return redirect('ue_list')
    else:
        form = UEForm(instance=ue)
    return render(request, 'gestionnaire_de_notes/Ue/update.html', {'form': form})

def ue_delete(request, pk):
    ue = get_object_or_404(UE, pk=pk)
    if request.method == 'POST':
        ue.delete()
        return redirect('ue_list')
    return render(request, 'gestionnaire_de_notes/Ue/delete.html', {'ue': ue})

# RessourceUE views
def ressourceue_list(request):
    ressources = RessourceUE.objects.all()
    return render(request, 'gestionnaire_de_notes/RA_UE/liste.html', {'ressources': ressources})

def ressourceue_create(request):
    if request.method == 'POST':
        form = RessourceUEForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ressourceue_list')
    else:
        form = RessourceUEForm()
    return render(request, 'gestionnaire_de_notes/RA_UE/ajout.html', {'form': form})

def ressourceue_update(request, pk):
    ressource = get_object_or_404(RessourceUE, pk=pk)
    if request.method == 'POST':
        form = RessourceUEForm(request.POST, instance=ressource)
        if form.is_valid():
            form.save()
            return redirect('ressourceue_list')
    else:
        form = RessourceUEForm(instance=ressource)
    return render(request, 'gestionnaire_de_notes/RA_UE/update.html', {'form': form})

def ressourceue_delete(request, pk):
    ressource = get_object_or_404(RessourceUE, pk=pk)
    if request.method == 'POST':
        ressource.delete()
        return redirect('ressourceue_list')
    return render(request, 'gestionnaire_de_notes/RA_UE/delete.html', {'ressource': ressource})

# Enseignant views
def enseignant_list(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'gestionnaire_de_notes/Enseignant/liste.html', {'enseignants': enseignants})

def enseignant_create(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enseignant_list')
    else:
        form = EnseignantForm()
    return render(request, 'gestionnaire_de_notes/Enseignant/ajout.html', {'form': form})

def enseignant_update(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('enseignant_list')
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'gestionnaire_de_notes/Enseignant/update.html', {'form': form})

def enseignant_delete(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    if request.method == 'POST':
        enseignant.delete()
        return redirect('enseignant_list')
    return render(request, 'gestionnaire_de_notes/Enseignant/delete.html', {'enseignant': enseignant})

# Examen views
def examen_list(request):
    examens = Examen.objects.all()
    return render(request, 'gestionnaire_de_notes/Examen/liste.html', {'examens': examens})

def examen_create(request):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('examen_list')
    else:
        form = ExamenForm()
    return render(request, 'gestionnaire_de_notes/Examen/ajout.html', {'form': form})

def examen_update(request, pk):
    examen = get_object_or_404(Examen, pk=pk)
    if request.method == 'POST':
        form = ExamenForm(request.POST, instance=examen)
        if form.is_valid():
            form.save()
            return redirect('examen_list')
    else:
        form = ExamenForm(instance=examen)
    return render(request, 'gestionnaire_de_notes/Examen/update.html', {'form': form})

def examen_delete(request, pk):
    examen = get_object_or_404(Examen, pk=pk)
    if request.method == 'POST':
        examen.delete()
        return redirect('examen_list')
    return render(request, 'gestionnaire_de_notes/Examen/delete.html', {'examen': examen})

# Note views
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'gestionnaire_de_notes/Notes/liste.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'gestionnaire_de_notes/Notes/ajout.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'gestionnaire_de_notes/Notes/update.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'gestionnaire_de_notes/Notes/delete.html', {'note': note})
