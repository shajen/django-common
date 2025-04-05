import datetime
from django.db.models import DurationField


def get_fields(qs):
    fields = {}
    for field in qs.model._meta.get_fields():
        if field.concrete and not field.many_to_many and not field.one_to_many:
            fields[field.name] = field
    for key, annotation in qs.query.annotations.items():
        fields[key] = annotation.output_field
    return fields


def filter(request, qs):
    fields = get_fields(qs)
    filters_fields = {}
    for key, value in request.GET.items():
        field = key.split("__")[0]
        if field in fields:
            if isinstance(fields[field], DurationField):
                filters_fields[key] = datetime.timedelta(seconds=int(value))
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
