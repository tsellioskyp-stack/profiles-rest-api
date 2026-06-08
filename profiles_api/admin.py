from django.contrib import admin
from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
# This code registers the UserProfile and ProfileFeedItem models with the Django admin site, allowing you to manage these models through the admin interface. By registering the models, you can perform CRUD (Create, Read, Update, Delete) operations on the user profiles and profile feed items directly from the admin dashboard. This is a convenient way to manage your application's data without having to interact with the database directly.
