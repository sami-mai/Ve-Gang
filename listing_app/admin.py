from django.contrib import admin
from listing_app.models import Listing, Service, Contact, Review, Location, Veg_Category


# Register your models here.
admin.site.register(Listing)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(Location)
admin.site.register(Veg_Category)
