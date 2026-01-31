from django.db.models import DurationField
from django.utils.dateparse import parse_duration


def get_fields(qs):
    fields = {}
    for field in qs.model._meta.get_fields():
        if field.concrete and not field.many_to_many and not field.one_to_many:
            fields[field.name] = field
    for key, annotation in qs.query.annotations.items():
        fields[key] = annotation.output_field
    return fields


def get_options_lists(request, qs, keys):
    options_lists = {}
    for key in keys:
        options = qs.values_list(key, flat=True).distinct().order_by(key)
        options_lists[key + "_options"] = sorted(list(options))
    return options_lists


def filter(request, qs):
    fields = get_fields(qs)
    filters_fields = {}
    for key, value in request.GET.items():
        if value:
            field = key.split("__")[0]
            if field in fields:
                if isinstance(fields[field], DurationField):
                    filters_fields[key] = parse_duration(value)
                else:
                    filters_fields[key] = value
    return qs.filter(**filters_fields)


def order_by(request, qs, default=[]):
    fields = get_fields(qs)
    order_by_fields = []
    order_by_param = request.GET.get("order_by")
    if order_by_param:
        for field in order_by_param.split(","):
            field_name = field.lstrip("-").split("__")[0]
            if field_name in fields:
                order_by_fields.append(field)
    order_by_fields.extend(default)
    return qs.order_by(*order_by_fields)
