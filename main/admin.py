from django.contrib import admin
from .models import UserDetail, Slider, Contact, Cart, Disease
from saler.models import Product, ProductSize, SalerDetail, category, dow, SellerSlider, MyCart, WholeSaleProduct, \
    Orders, trend, WholeSaleProductOrders, ProductReview

admin.site.site_header = '"welcome Ayurveda Administrator....!!"'


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'date')


admin.site.register(UserDetail)
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(SalerDetail)
admin.site.register(Slider)
admin.site.register(category)
admin.site.register(dow)
admin.site.register(Disease)
admin.site.register(ProductReview)
admin.site.register(Contact, ContactAdmin)
admin.site.register(SellerSlider)
admin.site.register(MyCart)
admin.site.register(WholeSaleProduct)
admin.site.register(WholeSaleProductOrders)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(trend)
