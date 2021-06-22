from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(People)
admin.site.register(Studio)
admin.site.register(Movie)
admin.site.register(MovieGenre)
admin.site.register(MovieCast)
admin.site.register(MovieCredit)
admin.site.register(Certificate)
admin.site.register(ReleaseData)