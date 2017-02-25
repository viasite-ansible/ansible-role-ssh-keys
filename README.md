## Example playbook
``` yaml
- hosts: all
  remote_user: root
  vars:
    ssh_keys_user: username
    ssh_keys_public_keys_dir: /ssh-public
    ssh_keys_public_keys_removed_dir: /ssh-public
  roles:
    - ssh-keys
```
