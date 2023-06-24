from django.contrib import admin

from exam_web.web.models import Profile, Fruit


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Fruit)
class GameAdmin(admin.ModelAdmin):
    pass
