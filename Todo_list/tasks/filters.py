from django_filters import rest_framework as filters
from tasks.models import Tasks
from distutils.util import strtobool


BOOLEAN_CHOICES = (
    ("false", "False"),
    ("true", "True"),
)

CHOICES = [
    ["title", "задачи - по алфавиту"],
    ["id", "ID - по нарастанию"],
    ["-id", "ID - убыванию"],
]


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class FilterSet(filters.FilterSet):
    title = filters.CharFilter(label="task", field_name="title", lookup_expr="contains")
    is_active = filters.TypedChoiceFilter(choices=BOOLEAN_CHOICES, coerce=strtobool)
    ordering = filters.OrderingFilter(
        choices=CHOICES,
        required=False,
        empty_label="-------",
    )

    class Meta:
        model = Tasks
        fields = ["title", "is_active"]
