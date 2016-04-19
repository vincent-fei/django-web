# coding:utf-8
from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Person

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            obj_original = self.model.objects.get(pk=obj.pk)
        else:
            obj_original = None

        obj.user = request.user
        obj.save()
    def delete_model(self, request, obj):
        obj.delete()

    list_display = ('title','pub_date','update_date',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('name',)
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request,queryset,search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct

class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)

