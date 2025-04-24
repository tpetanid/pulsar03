from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from dateutil.relativedelta import relativedelta # Need this for age calculation

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        return self.last_name
    
    class Meta:
        ordering = ['last_name', 'first_name']

# --- New Lookup Tables ---

# Species
class Species(models.Model):
    code = models.CharField(_("Code"), max_length=50, unique=True, help_text=_("Unique code, e.g., 'canine', 'feline'"))
    
    def __str__(self):
        # Try to return the name in the current language, fallback to code
        from django.utils.translation import get_language
        current_lang = get_language()
        translation = self.translations.filter(language=current_lang).first()
        return translation.name if translation else self.code

    class Meta:
        verbose_name = _("Species")
        verbose_name_plural = _("Species")
        ordering = ['code']

class SpeciesTranslation(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(_("Language"), max_length=10, choices=settings.LANGUAGES)
    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        verbose_name = _("Species Translation")
        verbose_name_plural = _("Species Translations")
        unique_together = ('species', 'language')
        ordering = ['language', 'name']

    def __str__(self):
        return f"{self.species.code} ({self.language}): {self.name}"

# Sex
class Sex(models.Model):
    code = models.CharField(_("Code"), max_length=10, unique=True, help_text=_("Unique code, e.g., 'M', 'F', 'MN', 'FS'"))

    def __str__(self):
        from django.utils.translation import get_language
        current_lang = get_language()
        translation = self.translations.filter(language=current_lang).first()
        return translation.name if translation else self.code
        
    class Meta:
        verbose_name = _("Sex")
        verbose_name_plural = _("Sexes")
        ordering = ['code']

class SexTranslation(models.Model):
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(_("Language"), max_length=10, choices=settings.LANGUAGES)
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("Sex Translation")
        verbose_name_plural = _("Sex Translations")
        unique_together = ('sex', 'language')
        ordering = ['language', 'name']

    def __str__(self):
        return f"{self.sex.code} ({self.language}): {self.name}"

# Breed
class Breed(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='breeds')
    code = models.CharField(_("Code"), max_length=100, unique=True, help_text=_("Unique code for the breed, e.g., 'golden_retriever'"))

    def __str__(self):
        from django.utils.translation import get_language
        current_lang = get_language()
        translation = self.translations.filter(language=current_lang).first()
        return f"{self.species} - {translation.name}" if translation else f"{self.species} - {self.code}"

    class Meta:
        verbose_name = _("Breed")
        verbose_name_plural = _("Breeds")
        ordering = ['species', 'code']

class BreedTranslation(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(_("Language"), max_length=10, choices=settings.LANGUAGES)
    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        verbose_name = _("Breed Translation")
        verbose_name_plural = _("Breed Translations")
        unique_together = ('breed', 'language')
        ordering = ['language', 'name']

    def __str__(self):
         return f"{self.breed.code} ({self.language}): {self.name}"

# Patient Model (Updated)
class Patient(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(_("Name"), max_length=100)
    species = models.ForeignKey(Species, on_delete=models.PROTECT, related_name='patients', verbose_name=_("Species")) 
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, related_name='patients', blank=True, null=True, verbose_name=_("Breed"))
    sex = models.ForeignKey(Sex, on_delete=models.PROTECT, related_name='patients', blank=True, null=True, verbose_name=_("Sex"))
    date_of_birth = models.DateField(_("Date of Birth"), blank=True, null=True)
    weight = models.DecimalField(_("Weight"), max_digits=5, decimal_places=2, blank=True, null=True, help_text=_("Weight (e.g., in kg)")) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def calculated_age(self):
        if not self.date_of_birth:
            return _("Unknown")
        
        today = timezone.now().date()
        # Use relativedelta for accurate age calculation considering months/days
        delta = relativedelta(today, self.date_of_birth)
        
        years = delta.years
        months = delta.months
        days = delta.days

        if years >= 1:
            # Translators: Age display format for years
            return _("%(years)d years") % {'years': years}
        elif months >= 1:
            # Translators: Age display format for months
            return _("%(months)d months") % {'months': months}
        else:
            # Translators: Age display format for days
            return _("%(days)d days") % {'days': days}
    calculated_age.fget.short_description = _("Age") # Column header in Admin

    def __str__(self):
        return f"{self.name} ({self.species}) - {self.owner.last_name}"

    class Meta:
        verbose_name = _("Patient")
        verbose_name_plural = _("Patients")
        ordering = ['owner__last_name', 'name']
