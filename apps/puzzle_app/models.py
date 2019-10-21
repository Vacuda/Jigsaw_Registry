from django.db import models
from datetime import datetime
from apps.log_and_reg_app.models import User
import re

class Brand(models.Model):
    name                = models.CharField(max_length=30)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    #puzzles

class Category(models.Model):
    name                = models.CharField(max_length=30)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    #puzzles

class Puzzle(models.Model):
    title               = models.CharField(max_length=30)
    brand               = models.ForeignKey(Brand, related_name="puzzles")
    picture             = models.ImageField()
    desc                = models.TextField(max_length=100)
    category            = models.ManyToManyField(Category, related_name="puzzles")

    pieces_labeled      = models.PositiveSmallIntegerField()
    pieces_actual       = models.PositiveSmallIntegerField()
    length              = models.DecimalField(max_digits=4, decimal_places=2)
    height              = models.DecimalField(max_digits=4, decimal_places=2)

    owned_by            = models.ForeignKey(User, related_name="puzzles")
    missing_pieces      = models.PositiveSmallIntegerField()
    notes               = models.TextField(max_length=100)
    owned               = models.BooleanField(default=False)
    completions         = models.PositiveSmallIntegerField()
    initial_complete    = models.DateTimeField()
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    #projects
