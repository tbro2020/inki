from django.contrib import admin
from django.utils.safestring import mark_safe
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.shortcuts import reverse
from core.models import *


class ResponseTabularInline(NestedStackedInline):
    model = Response
    extra = 1


class QuestionTabularInline(NestedStackedInline):
    model = Question
    extra = 1
    inlines = [ResponseTabularInline]


class CampaignAdmin(NestedModelAdmin):
    list_display = ('name', 'campaign', 'report', 'created')
    search_fields = ('name',)
    list_filter = ('updated', 'created')
    date_hierarchy = "created"
    inlines = [QuestionTabularInline]

    def campaign(self, obj):
        return mark_safe(
            f"<a href=\'{reverse('core:campaign', kwargs={'pk': obj.id})}\'>{self.campaign.short_description}</a>")

    campaign.short_description = 'Campagne'

    def report(self, obj):
        return mark_safe(
            f"<a target='_blank' href=\'{reverse('core:report', kwargs={'pk': obj.id})}\'>{self.report.short_description}</a>")

    report.short_description = 'Rapport'

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.search_fields_hint = ''


admin.site.register(Campaign, CampaignAdmin)
