from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from recipe_app.models import Veg_Status, Recipe
from listing_app.models import Listing, Location, Review


class Profile(models.Model):
    '''
    Profile model class
    '''
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    bio = models.TextField()
    birthdate = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    veg_status = models.ForeignKey(Veg_Status, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    # Create Profile when creating a User
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # Save Profile when saving a User
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    '''
    Class methods:
    update_profile:
    find_profile: allows us to search for a user using their profile name.
    get_profile_by_id: allows us to get profile by id.
    '''
    @classmethod
    def update_profile(cls, id, bio):
        update = cls.objects.filter(id=id).update(bio=bio)
        return update

    @classmethod
    def find_profile(cls, search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
