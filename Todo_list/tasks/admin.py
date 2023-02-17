from django.contrib import admin
from .models import Tasks

# admin.site.register(Tasks)


@admin.register(Tasks)
class TestAdmin(admin.ModelAdmin):
    def time_create(self, obj):
        return obj.created_time.strftime("%m-%d-%Y %H:%M:%S")

    def time_complete(self, obj):
        try:
            return obj.completed_time.strftime("%m-%d-%Y %H:%M:%S")
        except:
            return None

    time_create.admin_order_field = "timefield"
    time_create.short_description = "created_time"
    time_complete.admin_order_field = "timefield"
    time_complete.short_description = "completed_time"

    readonly_fields = ("created_time", "completed_time")
    list_display = (
        "title",
        "time_create",
        "time_complete",
        "is_active",
    )
    search_fields = ["title"]
    list_filter = ("is_active",)
    ordering = ("title", "created_time")
