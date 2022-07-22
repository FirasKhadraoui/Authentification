from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Theme(models.Model):
    ThemeId = models.AutoField(primary_key=True)
    ThemeName = models.CharField(max_length=255)

class Project(models.Model):
    ProjectId = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=255)
    ProjectClass = models.CharField(max_length=255)
    ProjectDescription = models.CharField(max_length=1500)
    Theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

class Tuteur(models.Model):
    TuteurId = models.AutoField(primary_key= True)
    TuteurFirstName = models.CharField(max_length=255)
    TuteurLastName = models.CharField(max_length=255)
    TuteurEmail = models.EmailField
    TuteurPassword = models.CharField(max_length=255)
    isAdmin = models.BooleanField(default=False)
    isCoordinator = models.BooleanField(default=False)
    
class Equipe(models.Model):
    EquipeId = models.AutoField(primary_key=True)
    EquipeName = models.CharField(max_length=255)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Tuteur = models.ForeignKey(Tuteur, on_delete=models.CASCADE)

class Etudiant(models.Model):
    EtudiantId = models.AutoField(primary_key= True)
    EtudiantName = models.CharField(max_length=255)
    # EtudiantFirstName = models.CharField(max_length=255)
    # EtudiantLastName = models.CharField(max_length=255)
    # EtudiantEmail = models.CharField(max_length=255,unique=True)
    EtudiantClass = models.CharField(max_length=255)
    Equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

class Option(models.Model):
    OptionId = models.AutoField(primary_key= True)
    OptionName = models.CharField(max_length=255)
    Etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

# class Level(models.Model):
#     LevelId = models.AutoField(primary_key= True)
#     LevelName = models.CharField(max_length=255)
#     Etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)