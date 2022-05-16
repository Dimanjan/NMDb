from django.contrib import admin

# Register your models here.
from .models import Movie, Actor, Director,Genre, Review

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review)

