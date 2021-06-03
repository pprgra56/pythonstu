from django.contrib import admin

# Register your models here.
from django.contrib import admin
from login.models import BookInfo,HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender']



admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)



