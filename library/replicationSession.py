#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from dellemc_unity_sdk import runner
from dellemc_unity_sdk import supportive_functions

from dellemc_unity_sdk import constants

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['unstable'],
                    'supported_by': 'community'}

parameters_all = {
    "create":
        {
            "srcResourceId": dict(required=True, type=str),
            "dstResourceId": dict(required=True, type=str),
            "maxTimeOutOfSync": dict(required=True, type=int),
            "remoteSystem": dict(type=object),
            "srcSPAInterface": dict(type=object),
            "srcSPBInterface": dict(type=object),
            "dstSPAInterface": dict(type=object),
            "dstSPBInterface": dict(type=object),
            "autoInitiate": dict(type=bool),
            "name": dict(type=str),
            "members": dict(type=list),
            "hourlySnapReplicationPolicy": dict(type=object),
            "dailySnapReplicationPolicy": dict(type=object),
            "replicateExistingSnaps": dict(type=bool)
        },
    "modify":
        {
            "id": dict(required=True, type=str),
            "maxTimeOutOfSync": dict(type=int),
            "name": dict(type=str),
            "srcSPAInterface": dict(type=object),
            "srcSPBInterface": dict(type=object),
            "dstSPAInterface": dict(type=object),
            "dstSPBInterface": dict(type=object),
            "hourlySnapReplicationPolicy": dict(type=object),
            "dailySnapReplicationPolicy": dict(type=object)
        },
    "delete":
        {
            "id": dict(required=True, type=str)
        },
    "resume":
        {
            "id": dict(required=True, type=str),
            "srcSPAInterface": dict(type=object),
            "srcSPBInterface": dict(type=object),
            "dstSPAInterface": dict(type=object),
            "dstSPBInterface": dict(type=object),
            "forceFullCopy": dict(type=bool)
        },
    "pause":
        {
            "id": dict(required=True, type=str)
        },
    "sync":
        {
            "id": dict(required=True, type=str)
        }
}

template = {
    constants.REST_OBJECT: "replicationSession",
    constants.ACTIONS: {
        "create":
            {
                constants.ACTION_TYPE: constants.ActionType.UPDATE,
                constants.PARAMETER_TYPES: parameters_all.get("create")
            },
        "modify":
            {
                constants.ACTION_TYPE: constants.ActionType.UPDATE,
                constants.PARAMETER_TYPES: parameters_all.get("modify")
            },
        "delete":
            {
                constants.ACTION_TYPE: constants.ActionType.UPDATE,
                constants.PARAMETER_TYPES: parameters_all.get("delete")
            },
        "resume":
            {
                constants.ACTION_TYPE: constants.ActionType.UPDATE,
                constants.PARAMETER_TYPES: parameters_all.get("resume")
            },
        "pause":
            {
                constants.ACTION_TYPE: constants.ActionType.UPDATE,
                constants.PARAMETER_TYPES: parameters_all.get("pause")
            },
        "sync":
            {
                constants.ACTION_TYPE: constants.ActionType.UPDATE,
                constants.PARAMETER_TYPES: parameters_all.get("sync")
            }

    }
}


def main():
    arguments = supportive_functions.create_arguments_for_ansible_module(template)

    ansible_module = AnsibleModule(arguments, supports_check_mode=True)
    runner.run(ansible_module, template)


if __name__ == '__main__':
    main()
