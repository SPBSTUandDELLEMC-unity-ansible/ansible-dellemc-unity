#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from dellemc_unity_sdk import runner
from dellemc_unity_sdk import supportive_functions
from dellemc_unity_sdk import constants

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['unstable'],
                    'supported_by': 'community'}

parameters_all = {
    'create': {
        'nasServer': dict(required=True, type=dict),
        'name': dict(type=str),
        'description': dict(type=str)
    }
}

template = {
    constants.REST_OBJECT: 'cifsServer',
    constants.ACTIONS: {
        'create': {
            constants.ACTION_TYPE: constants.ActionType.UPDATE,
            constants.PARAMETER_TYPES: parameters_all.get('create')
        }
    }
}


def main():
    arguments = supportive_functions.create_arguments_for_ansible_module(template)
    ansible_module = AnsibleModule(arguments, supports_check_mode=True)
    runner.run(ansible_module, template)


if __name__ == '__main__':
    main()
