from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(shopmodel)
admin.site.register(usermodel)
admin.site.register(cartmodel)

