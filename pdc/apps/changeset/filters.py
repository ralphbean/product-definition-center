#
# Copyright (c) 2015 Red Hat
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#
import django.forms.widgets as widgets

import django_filters

from pdc.apps.common.filters import value_is_not_empty
from . import models


SelectMultiple = widgets.SelectMultiple


class ChangesetFilterSet(django_filters.FilterSet):
    author = django_filters.CharFilter(method='filter_author',
                                       widget=SelectMultiple)
    resource = django_filters.CharFilter(method='filter_resource',
                                         widget=SelectMultiple)
    changed_since = django_filters.CharFilter(method='filter_committed_since',
                                              widget=widgets.DateTimeInput)
    changed_until = django_filters.CharFilter(method='filter_committed_until',
                                              widget=widgets.DateTimeInput)
    comment = django_filters.CharFilter(name="comment", lookup_expr="contains")

    @value_is_not_empty
    def filter_author(self, qs, name, value):
        return qs.filter(author__username__in=value).distinct()

    @value_is_not_empty
    def filter_resource(self, qs, name, value):
        return qs.filter(change__target_class__in=value).distinct()

    @value_is_not_empty
    def filter_committed_since(self, qs, name, value):
        return qs.filter(committed_on__gte=value).distinct()

    @value_is_not_empty
    def filter_committed_until(self, qs, name, value):
        return qs.filter(committed_on__lte=value).distinct()

    class Meta:
        model = models.Changeset
        fields = ('author', 'resource', 'changed_since', 'changed_until', 'comment')
