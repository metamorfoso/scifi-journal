from django.contrib import admin
from .models import Issue, Story, Author
from utilities.admin_shortcuts import inline_factory, single_page_admin


ISSUE_FIELDS = [
    'number',
    'pub_date'
]


admin.site.register(
    Author,
    list_display=("last_name", "first_name"),
    search_fields=("last_name", "first_name")
)

admin.site.register(
    Story,
    list_display=("title", "author", "content", "issue"),
    search_fields=("title", "content", "author__first_name", "author__last_name", "issue__number")
    # **single_page_admin(Story)
)

admin.site.register(
    Issue,
    inlines=[inline_factory(Story)],
    **single_page_admin(Issue)
)
