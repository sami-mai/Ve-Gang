from django.contrib import admin
from recipe_app.models import Recipe, Category, Cuisine, Veg_Status, Comment


# Register your models here.
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Veg_Status)
admin.site.register(Comment)
