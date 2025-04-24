from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (
    Owner, Patient, Species, SpeciesTranslation, Sex, SexTranslation, Breed, BreedTranslation
)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    ordering = ('last_name', 'first_name')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'species', 'breed', 'sex', 'calculated_age', 'date_of_birth', 'weight')
    list_filter = ('species', 'sex', 'created_at')
    search_fields = ('name', 'owner__last_name', 'owner__first_name', 'species__code', 'breed__code', 'sex__code')
    ordering = ('owner__last_name', 'name')
    autocomplete_fields = ['owner', 'species', 'breed', 'sex']
    fields = ('owner', 'name', 'species', 'breed', 'sex', 'date_of_birth', 'weight')

# --- Lookup Table Admin Configs ---

class SpeciesTranslationInline(admin.TabularInline):
    model = SpeciesTranslation
    extra = 1 # Show one empty slot for adding a new translation

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code', 'translations__name')
    inlines = [SpeciesTranslationInline]

class SexTranslationInline(admin.TabularInline):
    model = SexTranslation
    extra = 1

@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code', 'translations__name')
    inlines = [SexTranslationInline]

class BreedTranslationInline(admin.TabularInline):
    model = BreedTranslation
    extra = 1

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('code', 'species')
    list_filter = ('species',)
    search_fields = ('code', 'species__code', 'translations__name')
    autocomplete_fields = ['species']
    inlines = [BreedTranslationInline]
