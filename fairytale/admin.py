from django.contrib import admin
from .models import Categories, Authors, Books, Stories, Chapters, Generals


# Register your models here.
admin.site.register(Categories)
admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Stories)
admin.site.register(Chapters)
admin.site.register(Generals)
