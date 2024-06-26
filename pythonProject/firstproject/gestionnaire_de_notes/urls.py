from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('etudiants/', views.etudiant_list, name='etudiant_list'),
    path('etudiants/add/', views.etudiant_create, name='etudiant_create'),
    path('etudiants/update/<int:pk>/', views.etudiant_update, name='etudiant_update'),
    path('etudiants/delete/<int:pk>/', views.etudiant_delete, name='etudiant_delete'),


    
    path('etudiants/relever_de_notes/<int:pk>/', views.etudiant_relever_de_notes, name='etudiant_relever'),



    path('ues/', views.ue_list, name='ue_list'),
    path('ues/add/', views.ue_create, name='ue_create'),
    path('ues/update/<int:pk>/', views.ue_update, name='ue_update'),
    path('ues/delete/<int:pk>/', views.ue_delete, name='ue_delete'),
    path('ressources/', views.ressourceue_list, name='ressourceue_list'),
    path('ressources/add/', views.ressourceue_create, name='ressourceue_create'),
    path('ressources/update/<int:pk>/', views.ressourceue_update, name='ressourceue_update'),
    path('ressources/delete/<int:pk>/', views.ressourceue_delete, name='ressourceue_delete'),
    path('enseignants/', views.enseignant_list, name='enseignant_list'),
    path('enseignants/add/', views.enseignant_create, name='enseignant_create'),
    path('enseignants/update/<int:pk>/', views.enseignant_update, name='enseignant_update'),
    path('enseignants/delete/<int:pk>/', views.enseignant_delete, name='enseignant_delete'),
    path('examens/', views.examen_list, name='examen_list'),
    path('examens/add/', views.examen_create, name='examen_create'),
    path('examens/update/<int:pk>/', views.examen_update, name='examen_update'),
    path('examens/delete/<int:pk>/', views.examen_delete, name='examen_delete'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/add/', views.note_create, name='note_create'),
    path('notes/update/<int:pk>/', views.note_update, name='note_update'),
    path('notes/delete/<int:pk>/', views.note_delete, name='note_delete'),
    path('upload_notes/', views.upload_notes, name='upload_notes'),
    path('notes/', views.note_list, name='note_list'),
]
