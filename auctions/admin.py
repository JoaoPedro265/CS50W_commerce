from django.contrib import admin

# Register your models here.
from .models import User, Bid, Listing, Categorie, Comment, Watchlist

admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Listing)
admin.site.register(Categorie)
admin.site.register(Comment)
admin.site.register(Watchlist)
