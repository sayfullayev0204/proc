from django.contrib import admin
from .models import Tashkilot,Tuman, Axoli, Xizmatlar, Mahalla,Users

admin.site.register(Tashkilot)
admin.site.register(Tuman)
admin.site.register(Xizmatlar)
admin.site.register(Axoli)
admin.site.register(Mahalla)
admin.site.register(Users)