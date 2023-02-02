from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Employees)
admin.site.register(Branch)
admin.site.register(Payment)
admin.site.register(Message)
admin.site.register(Department)

