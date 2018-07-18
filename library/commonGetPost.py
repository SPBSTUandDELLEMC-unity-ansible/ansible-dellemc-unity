#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

from dellemc_unity_sdk import runner
from dellemc_unity_sdk import constants
from dellemc_unity_sdk import validator
from dellemc_unity_sdk import supportive_functions

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['unstable'],
                    'supported_by': 'community'}

parameters_all = {
    'get': {
        'required': {'resource_type'},
        'optional': {'id', 'fields'}
    },
    'post': {
        'required': {'resource_type', 'action'}
    }
}


def post(params, unity):
    params_types = parameters_all['post'].get('required')
    for key in params_types:
        if key not in params:
            supportive_functions.raise_exception_about_parameters(params_types)
    rest_object = params.pop('resource_type', None)
    action = params.pop('action', None)
    reply = unity.update(action, rest_object, params)
    return reply


template = {
    constants.ACTIONS: {
        'post':
            {constants.EXECUTED_BY: post},
        'get':
            {constants.ACTION_TYPE: constants.ActionType.QUERY,
             constants.PARAMETER_TYPES: parameters_all.get('get')}
    }
}


def main():
    arguments = runner.create_arguments_for_ansible_module(template)
    ansible_module = AnsibleModule(arguments, supports_check_mode=True)
    if ansible_module.params.get('get'):
        template[constants.REST_OBJECT] = ansible_module.params['get'].get('resource_type')
    if ansible_module.params.get('post'):
        template[constants.REST_OBJECT] = ansible_module.params['post'].get('resource_type')
    runner.run(ansible_module, template)


if __name__ == '__main__':
    main()
