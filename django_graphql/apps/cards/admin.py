from django.contrib import admin
from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'deck', 'question', 'bucket')


admin.site.register(Card, CardAdmin)