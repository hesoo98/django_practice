from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

#테이블 새로 만들때 model이랑 admin 둘다 건드려야함

'''
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    
admin.site.register(Bookmark, BookmarkAdmin)
이렇게 해두됨
'''