
from django.contrib import admin

# Register your models here.

from finpy.models import Stock, test, UserProfile, savedScreener

admin.site.register(Stock)
admin.site.register(UserProfile)
admin.site.register(test)
admin.site.register(savedScreener)
