from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models

'''
class ProjetAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'contenu',
        'cahier_de_charge',
        'progression',
        'isTermine',
        'date_debut',
        'date_fin',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'isTermine',
        'date_debut',
        'date_fin',
        'statut',
        'date_add',
        'date_update',
        'id',
        'titre',
        'description',
        'contenu',
        'cahier_de_charge',
        'progression',
        'isTermine',
        'date_debut',
        'date_fin',
        'statut',
        'date_add',
        'date_update',
    )


class Tache_projetAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'projet',
        'tache',
        'progrssion',
        'isTermine',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'projet',
        'isTermine',
        'statut',
        'date_add',
        'date_update',
        'id',
        'projet',
        'tache',
        'progrssion',
        'isTermine',
        'statut',
        'date_add',
        'date_update',
    )


class CommitAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'id_commit',
        'tache',
        'user',
        'commentaire',
        'description',
        'lien_git',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'tache',
        'user',
        'statut',
        'date_add',
        'date_update',
        'id',
        'id_commit',
        'tache',
        'user',
        'commentaire',
        'description',
        'lien_git',
        'statut',
        'date_add',
        'date_update',
    )


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'image',
        'fonction',
        'promotion',
        'adress',
        'contact',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'user',
        'statut',
        'date_add',
        'date_update',
        'id',
        'user',
        'image',
        'fonction',
        'promotion',
        'adress',
        'contact',
        'statut',
        'date_add',
        'date_update',
    )


class TacheUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'projet',
        'tache',
        'user',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'projet',
        'tache',
        'user',
        'statut',
        'date_add',
        'date_update',
        'id',
        'projet',
        'tache',
        'user',
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Projet, ProjetAdmin)
_register(models.Tache_projet, Tache_projetAdmin)
_register(models.Commit, CommitAdmin)
_register(models.Profile, ProfileAdmin)
_register(models.TacheUser, TacheUserAdmin)

'''
