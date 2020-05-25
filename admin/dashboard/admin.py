from django.contrib import admin
from .models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'title')

    #use where the model fields is a date to make hierarchi
    date_hierarchy = 'birth_date' 

    #by default the actions are on the top
    actions_on_top = True 

    # if this is true the actions will be on the bottom
    actions_on_bottom = False 

    #Controls whether a selection counter is displayed next to the action dropdown
    actions_selection_counter = True 

    #This attribute overrides the default display value for record’s fields that are empty (None, empty string, etc.)
    empty_value_display = '-empty-' 


    #Set list_display to control which fields are displayed on the change list page of the admin.
    list_display = ('name', 'title')

# class AuthorAdmin(admin.ModelAdmin):
#     exclude = ('birth_date', )

class FlatPageAdmin(admin.ModelAdmin):
    fields = ('url', 'title', 'content')
