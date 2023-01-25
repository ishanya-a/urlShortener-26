from django.contrib import admin
from .models import LongToShort
from .models import History
# Register your models here.
admin.site.register(LongToShort)
admin.site.register(History)