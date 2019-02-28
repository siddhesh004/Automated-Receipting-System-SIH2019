from django.contrib import admin
from Finance.models import User, ReceiptData, Uploads, Customer, Items

admin.site.register(User)
admin.site.register(ReceiptData)
admin.site.register(Uploads)
admin.site.register(Customer)
admin.site.register(Items)
