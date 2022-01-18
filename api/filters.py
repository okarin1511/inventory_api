from django_filters import rest_framework as filters
from .models import Box


class BoxFilter(filters.FilterSet):

    length_more_than = filters.NumberFilter(field_name="length", lookup_expr="mt")
    length_less_than = filters.NumberFilter(field_name="length", lookup_expr="lt")
    width_more_than = filters.NumberFilter(field_name="width", lookup_expr="mt")
    width_less_than = filters.NumberFilter(field_name="width", lookup_expr="lt")
    height_more_than = filters.NumberFilter(field_name="height", lookup_expr="mt")
    height_less_than = filters.NumberFilter(field_name="height", lookup_expr="lt")
    area_more_than = filters.NumberFilter(field_name="area", lookup_expr="mt")
    area_less_than = filters.NumberFilter(field_name="area", lookup_expr="lt")
    volume_more_than = filters.NumberFilter(field_name="volume", lookup_expr="mt")
    volume_less_than = filters.NumberFilter(field_name="volume", lookup_expr="lt")

    class Meta:
        model = Box
        fields = [
            "length_more_than",
            "length_less_than",
            "width_more_than",
            "width_less_than",
            "height_more_than",
            "height_less_than",
            "area_more_than",
            "area_less_than",
            "volume_more_than",
            "volume_less_than",
        ]

class BoxDateUsernameFilter(filters.FilterSet):

    length_more_than = filters.NumberFilter(field_name="length", lookup_expr="mt")
    length_less_than = filters.NumberFilter(field_name="length", lookup_expr="lt")
    width_more_than = filters.NumberFilter(field_name="width", lookup_expr="mt")
    width_less_than = filters.NumberFilter(field_name="width", lookup_expr="lt")
    height_more_than = filters.NumberFilter(field_name="height", lookup_expr="mt")
    height_less_than = filters.NumberFilter(field_name="height", lookup_expr="lt")
    area_more_than = filters.NumberFilter(field_name="area", lookup_expr="mt")
    area_less_than = filters.NumberFilter(field_name="area", lookup_expr="lt")
    volume_more_than = filters.NumberFilter(field_name="volume", lookup_expr="mt")
    volume_less_than = filters.NumberFilter(field_name="volume", lookup_expr="lt")
    created_after = filters.DateFilter(field_name="date_created", lookup_expr="mt")
    created_before = filters.DateFilter(field_name="date_created", lookup_expr="lt")

    username = filters.CharFilter(
        field_name="createdBy__username", lookup_expr="icontains"
    )

    class Meta:
        model = Box
        fields = [
            "length_more_than",
            "length_less_than",
            "width_more_than",
            "width_less_than",
            "height_more_than",
            "height_less_than",
            "area_more_than",
            "area_less_than",
            "volume_more_than",
            "volume_less_than",
            "created_after",
            "created_before",
            "username",
        ]