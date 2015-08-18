import sys

sys.path.append("/vagrant/ctf-infrastructure/api")

import api

try:
    sid = api.shell_servers.add_server({
        "host": "192.168.2.3",
        "port": 22,
        "username": "vagrant",
        "password": "vagrant",
        "protocol": "HTTP"
    })

    api.shell_servers.load_problems_from_server(sid)
    [api.admin.set_problem_availability(p["pid"], False) for p in api.problem.get_all_problems(show_disabled=True)]
    [api.problem.set_bundle_dependencies_enabled(b["bid"], True) for b in api.problem.get_all_bundles()]
    print("Loaded problems successfully.")
except Exception as e:
    print(e)
    print("Failed to load or re-provisioning.")

