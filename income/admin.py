from django.contrib import admin
from .models import Income

# Register your models here.

@admin.register(Income)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id','owner','source','amount','date']
