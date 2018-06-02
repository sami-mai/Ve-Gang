from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.text import slugify
import misaka


class Location(models.Model):
    continent = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = CountryField(blank_label='(select country)')
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    st_address = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class Contact(models.Model):
    pass


class Review(models.Model):
    '''
    reviews model class
    '''
    review = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

    class Meta:
        ordering = ['-post_date']

    @classmethod
    def get_reviews(cls, image_id):
        reviews = cls.objects.filter(image=image_id)
        return reviews


class Service(models.Model):
    '''
    Service nodel class that defines categories of posts and services on posts
    '''
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def save_service(self):
        self.save()

    def delete_service(self):
        self.delete()

    @classmethod
    def get_services(cls):
        services = Service.objects.all()
        return services


class Veg_Category(models.Model):
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
        category = Veg_Category.objects.all()
        return category


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bussiness_name = models.CharField(max_length=50, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    manager_name = models.CharField(max_length=50, blank=True)
    contact_info = models.ForeignKey(Contact, on_delete=models.CASCADE)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE)
    veg_category = models.ForeignKey(Veg_Category, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bussiness_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.bussiness_name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-post_date']

    @classmethod
    def get_listings(cls, image_id):
        listings = cls.objects.filter(image=image_id)
        return listings
