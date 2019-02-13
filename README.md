# docker

Master: [![Build Status](https://travis-ci.org/sansible/docker.svg?branch=master)](https://travis-ci.org/sansible/docker)  
Develop: [![Build Status](https://travis-ci.org/sansible/docker.svg?branch=develop)](https://travis-ci.org/sansible/docker)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This role installs Docker and optional sets up a user for sudo-less usage.


## Installation and Dependencies

To install run `ansible-galaxy install sansible.docker` or add this to your
`roles.yml`.

```YAML
- name: sansible.docker
  version: v3.0.x
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses tags: **build** and **configure**

* `build` - Installs Docker and supporting tools
* `configure` - Configures Docker Daemon


## Examples

Simply include this role in your playbook, options for Docker's daemon.json 
file can be specified via the ```sansible_docker_daemon_config``` variable:

```YAML
- name: Install and configure docker
  hosts: "somehost"

  roles:
    - role: sansible.docker
      sansible_docker_daemon_config:
        bip: 10.8.0.0/25
        storage-driver: overlay2
```

Setup user for sudo-less access:

```YAML
- name: Install and configure docker
  hosts: "somehost"

  roles:
    - role: sansible.docker
      sansible_docker_workspace_user: some_user
```

Note that if you want to make use of Docker via this user within the same
Ansible run then you will need to be aware of this issue:
[https://github.com/ansible/ansible-modules-core/issues/921]().

This role supports DeviceMapper via LVM as well:

```YAML
- name: Install and configure docker
  hosts: "somehost"

  roles:
    - role: sansible.docker
      storage-driver: devicemapper
      storage-opts:
        - "dm.directlvm_device=/dev/sdb"
```
