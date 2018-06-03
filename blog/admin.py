from django.contrib import admin
from blog.models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	#fields = ('title','desc','content')
    list_display = ('title', 'desc', 'click_count',)
    list_display_links = ('title', 'desc',)
    list_editable = ('click_count',)


    fieldsets = (
        ('基本信息',{'fields':('title','desc','content')}),
        ('高级设置',{'classes':('collapse',),
                    'fields':('click_count','is_recommend'),
                    }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
            )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)