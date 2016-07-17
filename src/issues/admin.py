from django.contrib import admin
from .models import Issue, Story
from utilities.admin_shortcuts import inline_factory, single_page_admin


ISSUE_FIELDS = [
    'number',
    'pub_date'
]


admin.site.register(
    Issue,
    list_display=ISSUE_FIELDS,
    inlines=[inline_factory(Story)]
)
