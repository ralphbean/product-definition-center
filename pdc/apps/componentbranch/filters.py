#
# Copyright (c) 2017 Red Hat
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import django_filters

from pdc.apps.common.filters import CaseInsensitiveBooleanFilter
from pdc.apps.componentbranch.models import (
    ComponentBranch, SLA, SLAToComponentBranch)


class ComponentBranchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    global_component__name = django_filters.CharFilter(
        name='global_component', lookup_type='iexact')
    type__name = django_filters.CharFilter(name='type', lookup_type='iexact')
    active = CaseInsensitiveBooleanFilter()
    critical_path = CaseInsensitiveBooleanFilter()

    class Meta:
        model = ComponentBranch
        # Specifies the exact lookups to allow
        fields = ('name', 'global_component', 'type')


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
    branch_active = CaseInsensitiveBooleanFilter(name='branch__active', lookup_type='iexact')
    eol_after = django_filters.DateFilter(name="eol", lookup_type='gte')
    eol_before = django_filters.DateFilter(name="eol", lookup_type='lte')

    class Meta:
        model = SLAToComponentBranch
        # Specifies the exact lookups to allow
        fields = ('sla', 'branch', 'global_component', 'branch_type', 'eol',
                  'eol_after', 'eol_before')
