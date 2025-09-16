#!/usr/bin/env python3

# Copyright: (c) 2025, Your Name <your.email@example.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create a file with given content on remote host

version_added: "1.0.0"

description:
    - This module creates a text file at the specified path with the provided content.
    - If the file already exists and content is unchanged, it does nothing (idempotent).
    - Supports check mode.

options:
    path:
        description:
            - Full path to the file to be created.
        required: true
        type: str
    content:
        description:
            - Content to write into the file.
        required: true
        type: str

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a test file
  my_namespace.my_collection.my_own_module:
    path: /tmp/testfile.txt
    content: "Hello from my custom Ansible module!"

- name: Create configuration file
  my_namespace.my_collection.my_own_module:
    path: /etc/myapp/config.ini
    content: |
      [server]
      host = localhost
      port = 8080
'''

RETURN = r'''
path:
    description: The full path of the created/modified file.
    type: str
    returned: always
    sample: "/tmp/testfile.txt"
content:
    description: The content that was written to the file.
    type: str
    returned: always
    sample: "Hello from my custom Ansible module!"
changed:
    description: Whether the file was created or modified.
    type: bool
    returned: always
    sample: true
'''

import sys
import json
import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    # Если есть аргумент командной строки — читаем его как файл JSON
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
        try:
            with open(json_file, 'r') as f:
                raw_data = json.load(f)
        except Exception as e:
            result = dict(
                failed=True,
                msg=f"Failed to read or parse JSON file {json_file}: {str(e)}"
            )
            print(json.dumps(result))
            sys.exit(1)

        # Ansible ожидает структуру: { "ANSIBLE_MODULE_ARGS": { ... } }
        if "ANSIBLE_MODULE_ARGS" in raw_data:
            params = raw_data["ANSIBLE_MODULE_ARGS"]
        else:
            # На случай, если передали просто объект (для совместимости)
            params = raw_data
    else:
        # Fallback: читаем из ANSIBLE_MODULE_ARGS (стандартный Ansible режим)
        from ansible.module_utils.basic import _load_params
        params = _load_params()

    # Определяем параметры модуля
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # Создаём модуль
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Получаем параметры
    path = params.get('path')
    content = params.get('content')

    result = dict(
        changed=False,
        path=path,
        content=content
    )

    # Проверка на идемпотентность
    if os.path.exists(path):
        with open(path, 'r') as f:
            if f.read() == content:
                module.exit_json(**result)

    # Check mode
    if module.check_mode:
        result['changed'] = True
        module.exit_json(**result)

    # Создание файла
    try:
        dir_name = os.path.dirname(path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

        with open(path, 'w') as f:
            f.write(content)

        result['changed'] = True

    except Exception as e:
        module.fail_json(msg=f"Failed to create file {path}: {str(e)}", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()