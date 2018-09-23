## EMC Unity Configuration and Management

#### Requires:
* Ansible 2.2 or newer
* Python module [dellemc-unity-sdk](https://github.com/ansible-dellemc-unity/dellemc-unity-sdk)

This package of Ansible modules provides access to configure and manage EMC Unity storage appliance.

#### Supported REST objects:

| REST object      | Create  | Modify  | Delete  | Others  |
|------------------|---------|---------|---------|---------|
| cifsServer       |    +    |    -    |    -    |    -    |
| cifsShare        |    +    |    -    |    -    |    -    |
| fileInterface    |    +    |    +    |    +    |    -    |
| host             |    +    |    +    |    +    |    -    |
| iscsiPortal      |    +    |    +    |    +    |    -    |
| lun (reference to storageResource)  |    +    |    +    |    +    |    -    |
| nasServer        |    +    |    +    |    +    |    -    |
| nfsServer        |    +    |    +    |    +    |    -    |
| pool             |    +    |    +    |    +    |    -    |
| storageResource  |         |         |         |    -    |

#### Folder hierarchy:

* folder `playbooks/rest_objects` contains simple actions with REST objects
* folder `playbooks/getters` demonstrates get action 
* folder `playbooks/complex` shows creating interconnected objects in a chain

#### How to run:

To run tasks, change the option values to fit your system in group_vars/all or add they into terminal command, and then run:

    ansible-playbook playbooks/rest_objects/pool/create.yml -e "password=qwerty123"
    ansible-playbook playbooks/getters/unity_get.yml -e "password=qwerty123"
    ansible-playbook playbooks/complex/demo_file_access.yml -e "password=qwerty123"
