from django.db.models.fields import AutoField, CharField, TextField
from django.contrib import admin
from django import forms


def single_page_admin(model_cls):
    '''Return dict of admin options to configure a spreadsheet-like single page
       admin for the model_cls. All fields are editable within the list, and
       text fields are searchable. A __unicode__ method is assumed to be
       present.'''

    list_editable = []
    search_fields = []

    for field in model_cls._meta.fields:
        if field.editable and not isinstance(field, AutoField):
            list_editable.append(field.name)
        if isinstance(field, CharField) or isinstance(field, TextField):
            search_fields.append(field.name)

    list_display = ['__str__'] + list_editable

    return {
        'search_fields': search_fields,
        'list_display': list_display,
        'list_editable': list_editable
    }


def rich_text_form_factory(model_cls, fields):
    """Creates a ModelForm with rich text widgets for the given fields. Fields
       should be of the form [field1,field2] or
       [(field1, class1), (field2, class2)]

       It seems Django sometimes tries to initialise the admin (including
       forms) before models are properly set up, if strings have been used for
       foreign key relationships. In this case, this helper doesn't work.   """

    if not (isinstance(fields, list) or isinstance(fields, tuple)):
        fields = [fields]

    class_map = []
    for f in fields:
        if isinstance(f, list) or isinstance(f, tuple):
            class_map.append(f)
        else:
            class_map.append((f, 'html'))

    class RichTextForm(forms.ModelForm):

        class Meta:
            model = model_cls
            exclude = []
            widgets = dict([(f, forms.Textarea(attrs={'class': classes}))
                            for f, classes in class_map])

    return RichTextForm


def inline_factory(model_cls, base_cls=admin.TabularInline, **kwargs):
    class Inline(base_cls):
        model = model_cls
        extra = 1

    for k, v in kwargs.items():
        setattr(Inline, k, v)
    return Inline


def get_readonly_fields(model_cls, exclude=[]):
    readonly_fields = []

    for field in model_cls._meta.fields + model_cls._meta.many_to_many:
        if not isinstance(field, AutoField) and field.name not in exclude:
            readonly_fields.append(field.name)

    return readonly_fields


def readonly_admin(model_cls, exclude=[]):
    list_display = []
    search_fields = []

    for field in model_cls._meta.fields + model_cls._meta.many_to_many:
        if not isinstance(field, AutoField):
            if len(list_display) < 5 and not isinstance(field, TextField):
                list_display.append(field.name)
            if isinstance(field, (CharField, TextField)):
                search_fields.append(field.name)

    return {
        'search_fields': search_fields,
        'list_display': list_display,
        'readonly_fields': get_readonly_fields(model_cls, exclude),
    }


def readonly_inline_factory(model_cls, exclude=[]):
    opts = {
        'readonly_fields': get_readonly_fields(model_cls, exclude),
        'extra': 0,
        'max_num': 0,
        'can_delete': False,
    }
    return inline_factory(model_cls, **opts)
