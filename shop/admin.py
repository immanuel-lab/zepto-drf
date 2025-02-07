from django.contrib import admin
# from .models import Book,Author,Department,Employee,Department1,Employee1,BookNew

from .models import ProductCategories
from import_export.admin import ImportExportModelAdmin


# Register your models here.

# admin.site.register(Person)


# class ProfileAdmin(admin.ModelAdmin):
#     fields = ['bio', 'person']  # Specify the order of fields you want in the admin panel

# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Book)
# admin.site.register(Author)



# admin.site.register(Department)
# admin.site.register(Employee)


# admin.site.register(Department1)
# admin.site.register(Employee1)


# admin.site.register(BookNew)


# admin.site.register(Product)


class ProductsCategoriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(ProductCategories,ProductsCategoriesAdmin)


