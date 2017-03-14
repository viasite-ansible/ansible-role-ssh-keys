## Example playbook

You can define public keys via files or via variables:
``` yaml
- hosts: all
  remote_user: root
  vars:
    ssh_keys_user: username # default remote_user
    ssh_keys_public_keys_dir: files/ssh-public-keys
    ssh_keys_public_keys_removed_dir: files/ssh-public-keys-removed
    ssh_keys_public_keys:
      - "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGbiz1ZE5wjPUYvn1z/Ba5w3lQcohyBFbhxBVHNLIWw89ypNTkSLkQi3QRTAXipNanBxEMxaQys7Um/kNuf3z8sZKE84CNdwFH5IGOpvb1sNVac0UfMfGsP5hB7hU3XnoLx4TtkC5tbi4/zAaBxsaU2IgLaa0zkgs7E4QCYz5eDua6FyY7sQWYfcWsx99qB4vqit2XymUamH4bedYe3n8un3P5xTszUQdLiO5T5230pSosO9pPxoJUdQExQEWnP8i5jny2KkaZXBXmjz3XfCvNj71jH3k49006bIsI70KUyiMSEt3RipG0Vk3VBrUs9bys+YkzF+k0IJF2q46Wx01n test3@example.com"
    ssh_keys_public_keys_removed:
      - "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDejO8qBRoXMYj9XzrY+13E3qCGTyLEiEGsZiiXwv4jcwyXG7cqJMyZGYlYlWvZr2ySceftkP/HFHddkeY0MvKwuf2zyd1+Za+2TCrXMjUgClkX25RKHWmTeMMifldl6YfWrmYOWb2IiukQ5W2DWKdJz47fJP/SsDEefy7wnfmntUPpKX+28+uokEo5Bzo4xWseNSmdh4zBSLUZi2i64FTbCZTTgcMuPXAixKw5onMYHZV4LiC7IBbqj4aYMa1ZFCcj7eWiK699Qpjc69qQefRgH8YXFfDC+nYO54zimA2Z4It6eJUCXDQPcx/aU+HdZbXepHvzrjbgwwP0LX5Bd235 test4@example.com"
  roles:
    - ssh-keys
```

Directories path is relative to role path. For example, directory scructure:
```
project
- roles
- - ssh-keys

- vars
- - ssh-public-keys
- - ssh-public-keys-removed

- playbook.yml
```

You should define vars:
``` yaml
    ssh_keys_public_keys_dir: ../../vars/ssh-public-keys
    ssh_keys_public_keys_removed_dir: ../../vars/ssh-public-keys-removed
```
