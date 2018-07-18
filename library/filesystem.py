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
        'name': dict(required=True, type=str),
        'fsParameters': dict(required=True),
        'description': dict(type=str),
        'replicationParameters': dict(type=dict),
        'snapScheduleParameters': dict(type=dict),
        'cifsFsParameters': dict(type=dict),
        'nfsShareCreate': dict(type=list),
        'cifsShareCreate': dict(type=list)
    }
}

template = {
    constants.REST_OBJECT: 'storageResource',
    constants.REST_OBJECT_FOR_GET_REQUEST: "filesystem",
    constants.ACTIONS: {
        'create': {
            constants.ACTION_TYPE: constants.ActionType.UPDATE,
            constants.PARAMETER_TYPES: parameters_all.get('create'),
            constants.DO_ACTION: 'createFilesystem'
        }
    }
}


def main():
    arguments = supportive_functions.create_arguments_for_ansible_module(template)
    ansible_module = AnsibleModule(arguments, supports_check_mode=True)
    runner.run(ansible_module, template)


if __name__ == '__main__':
    main()
