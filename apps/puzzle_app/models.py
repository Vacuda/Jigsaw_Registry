from django.db import models
from datetime import datetime
from apps.log_and_reg_app.models import User
import re

class Brand(models.Model):
    name                = models.CharField(max_length=30)
    belongs_to          = models.ForeignKey(User, related_name="brands")
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    #puzzles

class Category(models.Model):
    name                = models.CharField(max_length=30)
    belongs_to          = models.ForeignKey(User, related_name="categories")
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    #puzzles

class PuzzleImage(models.Model):
    image               = models.ImageField(upload_to='puzzle_images')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    #puzzle

class Puzzle(models.Model):
    title               = models.CharField(max_length=30)
    brand               = models.ForeignKey(Brand, related_name="puzzles", null=True)
    picture             = models.OneToOneField(PuzzleImage, on_delete=models.CASCADE, related_name="puzzle", null=True)
    desc                = models.TextField(max_length=100, blank=True)
    categories          = models.ManyToManyField(Category, related_name="puzzles")

    pieces_labeled      = models.PositiveSmallIntegerField()
    pieces_actual       = models.PositiveSmallIntegerField()
    width               = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    height              = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    belongs_to          = models.ForeignKey(User, related_name="puzzles")
    missing_pieces      = models.PositiveSmallIntegerField(default=0)
    notes               = models.TextField(max_length=100, blank=True)
    owned               = models.BooleanField(default=True)
    completed           = models.BooleanField(default=False)
    completions         = models.PositiveSmallIntegerField(default=0)
    initial_complete    = models.DateTimeField(null=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    #projects
