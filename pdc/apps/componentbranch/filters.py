#
# Copyright (c) 2017 Red Hat
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import django_filters
from django.db.models import Q
from datetime import datetime

from pdc.apps.common.filters import CaseInsensitiveBooleanFilter
from pdc.apps.componentbranch.models import (
    ComponentBranch, SLA, SLAToComponentBranch)


def string_to_bool(item):
    try:
        # Check to see if a number was passed
        return bool(int(item))
    except ValueError:
        # If it's not a number, check the string contents
        if item.lower() == 'true':
            return True
        elif item.lower() == 'false':
            return False
        else:
            raise ValueError('"{0}" is not a valid bool'.format(item))


def filter_active(queryset, value):
    if not value:
        return queryset
    try:
        processed_value = string_to_bool(value)
    except ValueError:
        # If a ValueError is thrown, then the value was invalid
        return queryset

    today = datetime.utcnow().date()
    if processed_value is True:
        # Any branch that is active will have at least one SLA that has not
        # gone EOL
        return queryset.filter(slas__eol__gte=today).distinct()
    else:
        # Any branch that is inactive will not have an SLA that has not gone
        # EOL yet. This checks for any branches which contain no SLAs or SLAs
        # that have gone EOL. It then excludes the branches which contain at
        # least one SLA that hasn't gone EOL yet.
        return queryset.filter(Q(slas__isnull=True) | Q(slas__eol__lte=today))\
            .exclude(slas__eol__gte=today).distinct()


def filter_active_sla_to_branch(queryset, value):
    if not value:
        return queryset
    try:
        processed_value = string_to_bool(value)
    except ValueError:
        # If a ValueError is thrown, then the value was invalid
        return queryset

    today = datetime.utcnow().date()
    if processed_value is True:
        # Any branch that is active will have at least one SLA that has not
        # gone EOL
        return queryset.filter(branch__slas__eol__gte=today).distinct()
    else:
        # Any branch that is inactive will not have an SLA that has not gone
        # EOL yet. This checks for any branches which contain no SLAs or SLAs
        # that have gone EOL. It then excludes the branches which contain at
        # least one SLA that hasn't gone EOL yet.
        return queryset.\
            filter(Q(branch__slas__isnull=True) |
                   Q(branch__slas__eol__lte=today))\
            .exclude(branch__slas__eol__gte=today).distinct()


class ComponentBranchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    global_component = django_filters.CharFilter(
        name='global_component__name', lookup_type='iexact')
    type = django_filters.CharFilter(
        name='type__name', lookup_type='iexact')
    active = CaseInsensitiveBooleanFilter(action=filter_active)
    critical_path = CaseInsensitiveBooleanFilter()

    class Meta:
        model = ComponentBranch


class SLAFilter(django_filters.FilterSet):

    class Meta:
        model = SLA
        # Specifies the exact lookups to allow
        fields = ('name', 'description')


class SLAToComponentBranchFilter(django_filters.FilterSet):
    sla = django_filters.CharFilter(name='sla__name', lookup_type='iexact')
    branch = django_filters.CharFilter(name='branch__name', lookup_type='iexact')
    global_component = django_filters.CharFilter(name='branch__global_component__name', lookup_type='iexact')
    branch_type = django_filters.CharFilter(name='branch__type__name', lookup_type='iexact')
    branch_active = CaseInsensitiveBooleanFilter(name='branch__active', action=filter_active_sla_to_branch)
    branch_critical_path = CaseInsensitiveBooleanFilter(name='branch__critical_path', lookup_type='iexact')
    eol_after = django_filters.DateFilter(name="eol", lookup_type='gte')
    eol_before = django_filters.DateFilter(name="eol", lookup_type='lte')

    class Meta:
        model = SLAToComponentBranch
        # Specifies the exact lookups to allow
        fields = ('eol',)
