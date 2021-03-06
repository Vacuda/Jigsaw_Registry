from django.db import models
from datetime import datetime
from apps.log_and_reg_app.models import User
from apps.puzzle_app.models import Puzzle
import re

class Helper(models.Model):
    name                = models.CharField(max_length=30)
    belongs_to          = models.ForeignKey(User, related_name="helpers")
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    #projects

class Project(models.Model):
    name                = models.CharField(max_length=30)
    helpers             = models.ManyToManyField(Helper, related_name="projects")
    puzzles             = models.ManyToManyField(Puzzle, related_name="projects")
    belongs_to          = models.ForeignKey(User, related_name="projects")
    started_at          = models.DateTimeField(null=True)
    finished_at         = models.DateTimeField(null=True)
    finished            = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    #project_images

class ProjectImage(models.Model):
    caption             = models.CharField(max_length=100)
    project             = models.ForeignKey(Project, related_name="pictures")            
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)











