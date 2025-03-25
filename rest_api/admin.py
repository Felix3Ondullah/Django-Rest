from django.contrib import admin
from .models import Post, Customer, Product, Order, Category, Review, Payment

# Register the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'author')
    search_fields = ('title', 'email')
    list_filter = ('author',)

# Register the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")
    search_fields = ("name",)
    list_filter = ("price", "stock")

# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_price", "created_at")
    filter_horizontal = ("product",)
    list_filter = ("created_at",)

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

# Register the Review model
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "customer", "rating", "created_at")
    list_filter = ("rating", "created_at")

# Register the Payment model
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "payment_method", "status", "created_at")
    list_filter = ("status", "payment_method")
