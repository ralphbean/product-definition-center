#
# Copyright (c) 2015 Red Hat
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import django_filters

from pdc.apps.common.filters import CaseInsensitiveBooleanFilter, MultiValueFilter
from .models import UnreleasedVariant


class UnreleasedVariantFilter(django_filters.FilterSet):
    variant_id          = django_filters.CharFilter(name='variant_id', lookup_expr='iexact')
    variant_uid         = django_filters.CharFilter(name='variant_uid', lookup_expr='iexact')
    variant_name        = django_filters.CharFilter(name='variant_name', lookup_expr='iexact')
    variant_type        = django_filters.CharFilter(name='variant_type', lookup_expr='iexact')
    variant_version     = django_filters.CharFilter(name='variant_version', lookup_expr='iexact')
    variant_release     = django_filters.CharFilter(name='variant_release', lookup_expr='iexact')
    variant_context     = django_filters.CharFilter(name='variant_context', lookup_expr='iexact')
    active              = CaseInsensitiveBooleanFilter()
    koji_tag            = django_filters.CharFilter(name='koji_tag', lookup_expr='iexact')
    runtime_dep_name    = MultiValueFilter(name='runtime_deps__dependency', distinct=True)
    runtime_dep_stream  = MultiValueFilter(name='runtime_deps__stream', distinct=True)
    build_dep_name      = MultiValueFilter(name='build_deps__dependency', distinct=True)
    build_dep_stream    = MultiValueFilter(name='build_deps__stream', distinct=True)
    component_name      = MultiValueFilter(name='rpms__srpm_name', distinct=True)
    component_branch    = MultiValueFilter(name='rpms__srpm_commit_branch', distinct=True)

    class Meta:
        model = UnreleasedVariant
        fields = ('variant_id', 'variant_uid', 'variant_name', 'variant_type',
                  'variant_version', 'variant_release', 'variant_context', 'koji_tag',
                  'modulemd', 'runtime_dep_name', 'runtime_dep_stream',
                  'build_dep_name', 'build_dep_stream', 'component_name',
                  'component_branch')
