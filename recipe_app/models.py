from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    '''
    comments model class
    '''
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-post_date']

    @classmethod
    def get_comments(cls, image_id):
        comments = cls.objects.filter(image=image_id)
        return comments


class Veg_Status(models.Model):
    pass


class Recipe(models.Model):
    pass


class Cuisine(models.Model):
    '''
    cuisine nodel class that defines categories of posts and cuisines on posts
    '''
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def save_cuisine(self):
        self.save()

    def delete_cuisine(self):
        self.delete()

    @classmethod
    def get_cuisines(cls):
        cuisines = Cuisine.objects.all()
        return cuisines


class Category(models.Model):
    '''
    Category nodel class that defines categories of cuisine and categorys on recipes
    '''
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def get_category(cls):
        category = Category.objects.all()
        return category
