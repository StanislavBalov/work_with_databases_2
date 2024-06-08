from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Tag, Article, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags = sum([1 for form in self.forms if form.cleaned_data.get('is_main')])
        if main_tags == 0:
            raise ValidationError('Specify one main tag.')
        elif main_tags > 1:
            raise ValidationError('Only one main tag is allowed.')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Scope)