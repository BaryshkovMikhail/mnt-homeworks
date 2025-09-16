cat > ~/git/homework/ansible/mnt-homeworks/08-ansible-06-module/my_own_namespace/yandex_cloud_elk/README.md <<'EOF'
# my_own_namespace.yandex_cloud_elk

Custom Ansible collection containing:

- `my_own_module`: Creates a file with given content (idempotent)
- `my_own_role`: Role wrapper for easy reuse

## Requirements

- Ansible 2.9+
- Python 3.6+

## Installation

```bash
ansible-galaxy collection install my_own_namespace.yandex_cloud_elk
```

## Usage 

### Module Example 

```yaml
- name: Create file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "Hello from module!"
```

### Role Example

```yaml
- hosts: localhost
  roles:
    - my_own_namespace.yandex_cloud_elk.my_own_role
```

### Defaults: 

- my_own_module_path: /tmp/default_file.txt
- my_own_module_content: "Default content from role defaults."
     

### License 

GPL-3.0-or-later
EOF 

---