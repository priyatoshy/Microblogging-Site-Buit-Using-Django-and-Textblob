from django.contrib import admin

# Register your models here.
from .models import Blog,Tags,Comment,ReactionHistory,Report,BlockedContent

#admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(ReactionHistory)
admin.site.register(BlockedContent)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','writer']
    list_filter=['writer','created_on']
    search_fields=['title']



@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display=['blog','reported_by','report','created_on']
    list_filter=['blog','created_on']
'''
@admin.register(Blog)



@admin.register(Blog)



@admin.register(Blog)
'''
