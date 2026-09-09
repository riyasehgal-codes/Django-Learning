from django.contrib import admin
from .models import ChaiReview, ChaiVariety
from .models import Store, ChaiCertificate

# Register your models here.

class ChaiReviewAdmin(admin.TabularInline):
    model = ChaiReview
    extra = 2 
    
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    search_fields = ('name', 'type')
    list_filter = ('type',)
    inlines = [ChaiReviewAdmin]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date', 'valid_until')


admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)