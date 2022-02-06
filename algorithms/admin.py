from django.contrib import admin

from .models import Test, AlgorithmType, DataSet

admin.site.register(Test)
admin.site.register(AlgorithmType)
admin.site.register(DataSet)
