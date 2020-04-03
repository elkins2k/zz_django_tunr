from django.contrib import admin

from .models import Artist, Song
# from .models import Artist
admin.site.register(Artist)
# from .models import Song
admin.site.register(Song)
