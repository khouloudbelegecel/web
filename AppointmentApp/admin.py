from django.contrib import admin
from .models import Appointment

@admin.action(description="make them confirmed")
def confirm_appointment(model, req, queryset):
    queryset.update(status='Confirmed')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    actions = [confirm_appointment]
    list_display = (
        "rason",
        "status",
        "duration_minutes",
        "appointment_date",
    )
    list_filter = ("status", "appointment_date")
    list_editable = ("status",)
    search_fields = ("rason", "status")
    ordering = ("-appointment_date",)
    fieldsets = (
        ("Description", {
            "fields": ("rason", "prescription", "status"),
        }),
        ("Date and Duration", {
            "fields": ("appointment_date", "duration_minutes"),
        }),
        ("Doctor and Patient", {
            "fields": ("doctor", "patient"),
        }),
        ("Planning", {
            "fields": ("created_at", "updated_at"),
        }),
    )
    readonly_fields = ("created_at", "updated_at")

