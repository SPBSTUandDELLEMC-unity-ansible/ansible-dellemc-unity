#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from dellemc_unity_sdk import runner
from dellemc_unity_sdk import supportive_functions
from dellemc_unity_sdk import constants
from dellemc_unity_sdk import validator
from dellemc_unity_sdk.unity import Unity

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['unstable'],
                    'supported_by': 'community'}
parameters_all = {
    'create': {
        'name': dict(required=True, type=str),
        'fsParameters': dict(required=True, type=dict),
        'description': dict(type=str),
        'replicationParameters': dict(type=dict),
        'snapScheduleParameters': dict(type=dict),
        'cifsFsParameters': dict(type=dict),
        'nfsShareCreate': dict(type=list),
        'cifsShareCreate': dict(type=list)
    },
    'modify': {
        "storageResource": dict(required=True, type=dict),
        'fsParameters': dict(type=dict),
        'description': dict(type=str),
        'replicationParameters': dict(type=dict),
        'snapScheduleParameters': dict(type=dict),
        'cifsFsParameters': dict(type=dict),
        'nfsShareCreate': dict(type=list),
        'nfsShareModify': dict(type=list),
        'nfsShareDelete': dict(type=list),
        'cifsShareCreate': dict(type=list),
        'cifsShareModify': dict(type=list),
        'cifsShareDelete': dict(type=list)

    },
    'delete': {
        "storageResource": dict(required=True, type=dict)
    }
}


def delete(params, unity):
    parameters_check = validator.check_parameters(params, parameters_all.get("delete"))

    if not parameters_check.get(constants.VALIDATOR_RESULT):
        supportive_functions.raise_exception_about_parameters(parameters_check.get(constants.VALIDATOR_MESSAGE))

    return unity.update("delete", "storageResource", params.get("storageResource"))


def modify(params, unity: Unity):
    parameters_check = validator.check_parameters(params, parameters_all.get("modify"))
    if not parameters_check.get(constants.VALIDATOR_RESULT):
        supportive_functions.raise_exception_about_parameters(parameters_check.get(constants.VALIDATOR_MESSAGE))

    resource_id_dict = params.pop("storageResource")
    params.update(resource_id_dict)
    return unity.update("modifyFilesystem", "storageResource", params)


template = {
    constants.REST_OBJECT: 'storageResource',
    constants.REST_OBJECT_FOR_GET_REQUEST: "filesystem",
    constants.ACTIONS: {
        'create': {
            constants.ACTION_TYPE: constants.ActionType.UPDATE,
            constants.PARAMETER_TYPES: parameters_all.get('create'),
            constants.DO_ACTION: 'createFilesystem'
        },
        'modify': {
            constants.EXECUTED_BY: modify
        },
        'delete': {
            constants.EXECUTED_BY: delete
        }
    }
}


def main():
    arguments = supportive_functions.create_arguments_for_ansible_module(template)
    ansible_module = AnsibleModule(arguments, supports_check_mode=True)
    runner.run(ansible_module, template)


if __name__ == '__main__':
    main()
