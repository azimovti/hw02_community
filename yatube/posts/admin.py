from django.contrib import admin

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    """Поля отобраэаемые в админке.
    Поиск по тексту постов, фильтрация по дате
    """
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = ('group',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
"""При регистрации модели Post
источником конфигурации для неё
назначаем класс PostAdmin"""
admin.site.register(Group)
