from django.contrib import admin

# Register your models here.


from accounting.models import  Document, Balance_Sheet, Accounting




admin.site.register(Document)
admin.site.register(Balance_Sheet)
admin.site.register(Accounting)
#admin.site.register(Books)

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person, Books

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass



@admin.register(Books)
class BooksAdmin(ImportExportModelAdmin):
    pass
#from accounting.models import Accounting


# class AccountingAdmin(admin.ModelAdmin):
#     list_display =["__str__","company","conta_devedora","conta_credora","amount","date"]
#     search_fields = ["conta_devedora","date","conta_devedora","conta_credora","amount"]
#     list_filter = ["conta_devedora", "conta_credora","date"]
#     list_editable = ["amount"]
#     class Meta:
#         model = Accounting

#admin.site.register(Accounting, AccountingAdmin)
#admin.site.register(Accounting)

# company = models.CharField(max_length=200)
# history = models.CharField(max_length=200)
# date = models.DateTimeField()
# debit = models.CharField(max_length=100)
# credit = models.CharField(max_length=100)
# amount = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
# conta_devedora = models.CharField(max_length=200)
# conta_credora = models.CharField(max_length=200)
# objects = models.Manager()
# pdobjects = DataFrameManager()  # Pandas-Enabled Manager
