from django.contrib import admin

from .models import Invoice1, LineItem1, Invoice2, LineItem2

admin.site.register(Invoice1)
admin.site.register(LineItem1)

admin.site.register(Invoice2)
admin.site.register(LineItem2)
# Register your models here.
