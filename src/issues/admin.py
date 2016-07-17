from django.contrib import admin
from .models import Issue, Story
from utilities.admin_shortcuts import inline_factory, single_page_admin


admin.site.register(
    Issue,
    inlines=[inline_factory(Story)]
)
