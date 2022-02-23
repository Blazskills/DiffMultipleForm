from django.contrib import admin
# from django.contrib.auth.models import User
# Register your models here.
from .models import Members, Profession, Snippet, Startup,Approved_Sector,Investor,Profile
# Register your models here.




admin.site.register(Startup)
# admin.site.register(User)
admin.site.register(Approved_Sector)
admin.site.register(Profile)
admin.site.register(Investor)
admin.site.register(Snippet)
admin.site.register(Profession)
admin.site.register(Members)



# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email','startup_name','startup_sector','account_type', 'created_on')