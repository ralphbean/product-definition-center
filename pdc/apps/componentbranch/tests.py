#
# Copyright (c) 2017 Red Hat
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from pdc.apps.component.models import GlobalComponent
from pdc.apps.componentbranch.models import ComponentBranch


class SLAAPITestCase(APITestCase):
    fixtures = ['pdc/apps/componentbranch/fixtures/tests/sla.json']

    def test_create_sla(self):
        url = reverse('sla-list')
        data = {
            'name': 'features',
            'description': 'A wonderful description'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_rv = {
            'name': 'features',
            'description': 'A wonderful description',
            'id': 3
        }
        self.assertEqual(response.data, expected_rv)

    def test_get_sla(self):
        url = reverse('sla-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['results'][0]['id'], 2)
        self.assertEqual(response.data['results'][0]['name'], 'bug_fixes')
        self.assertEqual(response.data['results'][0]['description'],
                         'Bug fixes are applied')

    def test_patch_sla(self):
        url = reverse('sla-detail', args=[1])
        data = {
            'description': 'A new description'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], 'security_fixes')
        self.assertEqual(response.data['description'], 'A new description')

    def test_patch_sla_change_name_error(self):
        url = reverse('sla-detail', args=[1])
        data = {
            'name': 'some_new_name'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = {'name': ["You may not modify the SLA's name due to policy"]}
        self.assertEqual(response.data, error)

    def test_put_sla(self):
        url = reverse('sla-detail', args=[1])
        data = {
            'name': 'security_fixes',
            'description': 'A new description'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], 'security_fixes')
        self.assertEqual(response.data['description'], 'A new description')

    def test_put_sla_change_name_error(self):
        url = reverse('sla-detail', args=[1])
        data = {
            'name': 'some_new_name',
            'description': 'A new description'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = {'name': ["You may not modify the SLA's name due to policy"]}
        self.assertEqual(response.data, error)

    def test_delete_sla(self):
        url = reverse('sla-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ComponentBranchAPITestCase(APITestCase):
    fixtures = ['pdc/apps/componentbranch/fixtures/tests/global_component.json',
                'pdc/apps/componentbranch/fixtures/tests/sla.json',
                'pdc/apps/componentbranch/fixtures/tests/componentbranch.json']

    def test_create_branch(self):
        url = reverse('componentbranch-list')
        data = {
            'name': '3.6',
            'global_component': 'python',
            'type': 'rpm',
            'active': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_rv = {
            'name': '3.6',
            'slas': [],
            'global_component': 'python',
            'active': False,
            'type': 'rpm',
            'id': 3
        }
        self.assertEqual(response.data, expected_rv)

    def test_create_branch_active_default(self):
        url = reverse('componentbranch-list')
        data = {
            'name': '3.6',
            'global_component': 'python',
            'type': 'rpm'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        branch = ComponentBranch.objects.filter(id=1).first()
        self.assertEqual(branch.active, True)

    def test_create_branch_bad_name(self):
        url = reverse('componentbranch-list')
        data = {
            'name': 'epel7',
            'global_component': 'python',
            'type': 'rpm',
            'active': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_rv = {'name': ['The branch name is not allowed based on the regex "^epel\\d+$"']}
        self.assertEqual(response.data, expected_rv)

    def test_get_branch(self):
        url = reverse('componentbranch-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['results'][0]['id'], 2)
        self.assertEqual(response.data['results'][0]['name'], '2.6')
        self.assertEqual(response.data['results'][0]['global_component'],
                         'python')
        self.assertEqual(response.data['results'][0]['type'], 'rpm')
        self.assertFalse(response.data['results'][0]['active'])

    def test_patch_branch(self):
        gc2 = GlobalComponent(name='pythonx')
        gc2.save()
        url = reverse('componentbranch-detail', args=[2])
        data = {
            'global_component': 'pythonx'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 2)
        self.assertEqual(response.data['name'], '2.6')
        self.assertEqual(response.data['global_component'],
                         'pythonx')
        self.assertEqual(response.data['type'], 'rpm')
        self.assertFalse(response.data['active'])

    def test_patch_branch_change_name_error(self):
        url = reverse('componentbranch-detail', args=[1])
        data = {
            'name': '3.6'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_msg = {
            'name': ["You may not modify the branch's name due to policy"]}
        self.assertEqual(response.data, error_msg)

    def test_put_branch(self):
        gc2 = GlobalComponent(name='pythonx')
        gc2.save()
        url = reverse('componentbranch-detail', args=[2])
        data = {
            'name': '2.6',
            'global_component': 'pythonx',
            'type': 'rpm',
            'active': False
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 2)
        self.assertEqual(response.data['name'], '2.6')
        self.assertEqual(response.data['global_component'],
                         'pythonx')
        self.assertEqual(response.data['type'], 'rpm')
        self.assertFalse(response.data['active'])

    def test_put_branch_change_name_error(self):
        url = reverse('componentbranch-detail', args=[1])
        data = {
            'name': '3.6',
            'global_component': 'python',
            'type': 'rpm',
            'active': False
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_msg = {
            'name': ["You may not modify the branch's name due to policy"]}
        self.assertEqual(response.data, error_msg)

    def test_delete_branch(self):
        url = reverse('componentbranch-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SLAToBranchAPITestCase(APITestCase):
    fixtures = ['pdc/apps/componentbranch/fixtures/tests/global_component.json',
                'pdc/apps/componentbranch/fixtures/tests/sla.json',
                'pdc/apps/componentbranch/fixtures/tests/componentbranch.json',
                'pdc/apps/componentbranch/fixtures/tests/slatocomponentbranch.json']

    def test_create_sla_to_branch_branch_exists(self):
        url = reverse('slatocomponentbranch-list')
        data = {
            'sla': 'bug_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': '2.7',
                'global_component': 'python',
                'type': 'rpm',
                'active': True
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_rv = {
            'sla': 'bug_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': '2.7',
                'global_component': 'python',
                'type': 'rpm',
                'active': True,
                'id': 1
            },
            'id': 2
        }
        self.assertEqual(response.data, expected_rv)

    def test_create_sla_to_branch_branch_exists_active_wrong(self):
        url = reverse('slatocomponentbranch-list')
        data = {
            'sla': 'bug_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': '2.7',
                'global_component': 'python',
                'type': 'rpm',
                'active': False
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = \
            "The found branch's active field did not match the supplied value"
        error_msg = {'branch.active': [error]}
        self.assertEqual(response.data, error_msg)

    def test_create_sla_to_branch(self):
        url = reverse('slatocomponentbranch-list')
        data = {
            'sla': 'bug_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': '2.7',
                'global_component': 'python',
                'type': 'rpm',
                'active': True,
                'id': 1
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_rv = {
            'sla': 'bug_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': '2.7',
                'global_component': 'python',
                'type': 'rpm',
                'active': True,
                'id': 1
            },
            'id': 2
        }
        self.assertEqual(response.data, expected_rv)

    def test_create_sla_to_branch_branch(self):
        url = reverse('slatocomponentbranch-list')
        data = {
            'sla': 'security_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': '3.6',
                'global_component': 'python',
                'type': 'rpm',
                'active': False
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_rv = {
            'sla': 'security_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': '3.6',
                'global_component': 'python',
                'type': 'rpm',
                'active': False,
                'id': 3
            },
            'id': 2
        }
        self.assertEqual(response.data, expected_rv)

    def test_create_sla_to_branch_branch_active_default(self):
        url = reverse('slatocomponentbranch-list')
        data = {
            'sla': 'security_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': '3.6',
                'global_component': 'python',
                'type': 'rpm',
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_rv = {
            'sla': 'security_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': '3.6',
                'global_component': 'python',
                'type': 'rpm',
                'active': True,
                'id': 3
            },
            'id': 2
        }
        self.assertEqual(response.data, expected_rv)

    def test_create_sla_to_branch_bad_branch_name(self):
        url = reverse('slatocomponentbranch-list')
        data = {
            'sla': 'security_fixes',
            'eol': '2020-01-01',
            'branch': {
                'name': 'epel7',
                'global_component': 'python',
                'type': 'rpm',
                'active': True,
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_rv = {'branch': {'name': ['The branch name is not allowed based on the regex "^epel\\d+$"']}}
        self.assertEqual(response.data, expected_rv)

    def test_get_sla_to_branch(self):
        url = reverse('slatocomponentbranch-list')
        response = self.client.get(url)
        expected_branch = {
            'name': '2.7',
            'global_component': 'python',
            'type': 'rpm',
            'active': True,
            'id': 1
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['id'], 1)
        self.assertEqual(response.data['results'][0]['sla'], 'security_fixes')
        self.assertEqual(response.data['results'][0]['eol'], '2020-01-01')
        self.assertEqual(response.data['results'][0]['branch'], expected_branch)

    def test_patch_sla_to_branch(self):
        url = reverse('slatocomponentbranch-detail', args=[1])
        data = {
            'eol': '2020-03-01'
        }
        response = self.client.patch(url, data, format='json')
        expected_branch = {
            'name': '2.7',
            'global_component': 'python',
            'type': 'rpm',
            'active': True,
            'id': 1
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['sla'], 'security_fixes')
        self.assertEqual(response.data['eol'], '2020-03-01')
        self.assertEqual(response.data['branch'], expected_branch)

    def test_patch_sla_to_branch_change_branch_error(self):
        url = reverse('slatocomponentbranch-detail', args=[1])
        data = {
            'branch': {
                'name': '3.6',
                'global_component': 'python',
                'type': 'rpm',
                'active': True
            }
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_msg = {'branch': ['The branch cannot be modified using this API']}
        self.assertEqual(response.data, error_msg)

    def test_put_sla_to_branch(self):
        url = reverse('slatocomponentbranch-detail', args=[1])
        branch = {
            'name': '2.7',
            'global_component': 'python',
            'type': 'rpm',
            'active': True
        }
        data = {
            'sla': 'security_fixes',
            'eol': '2020-03-01',
            'branch': branch,
        }
        response = self.client.put(url, data, format='json')
        branch['id'] = 1
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['sla'], 'security_fixes')
        self.assertEqual(response.data['eol'], '2020-03-01')
        self.assertEqual(response.data['branch'], branch)

    def test_put_sla_to_branch_change_branch_error(self):
        url = reverse('slatocomponentbranch-detail', args=[1])
        branch = {
            'name': '3.5',
            'global_component': 'python',
            'type': 'rpm',
            'active': True
        }
        data = {
            'sla': 'security_fixes',
            'eol': '2020-03-01',
            'branch': branch,
        }
        response = self.client.put(url, data, format='json')
        branch['id'] = 1
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = {'branch': ['The branch cannot be modified using this API']}
        self.assertEqual(response.data, error)

    def test_delete_sla_to_branch(self):
        url = reverse('slatocomponentbranch-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
