from django.contrib import admin

from .models import TrainingQuestion
from .models import Intent


# Register your models here.
class TrainingQuestionInline(admin.TabularInline):
    model = TrainingQuestion
    extra = 1


class IntentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['intent']}),
    ]
    inlines = [TrainingQuestionInline]


admin.site.register(Intent, IntentAdmin)