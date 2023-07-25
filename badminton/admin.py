from django.contrib import admin
from .models import Match, Review

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass