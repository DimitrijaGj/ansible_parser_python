import csv
import ansible_runner
from environs import Env

env = Env()
env.read_env()
INVENTORY_FILE = env.str("INVENTORY_FILE")
CSV_OUTPUT = 'server_inventory_report.csv'

result = ansible_runner.run(
    private_data_dir='.',
    inventory=INVENTORY_FILE,
    module='command',
    module_args='hostname -I',
    host_pattern='all'
)

rows = []
for host_event in result.events:
    if host_event.get('event') == 'runner_on_ok':
        host = host_event['event_data']['host']
        ip_output = host_event['event_data']['res'].get('stdout', '').strip()
        # Check for environment keyword in hostname
        env = ''
        name_lower = host.lower()
        if 'prd' in name_lower:
            env = 'prd'
        elif 'stg' in name_lower:
            env = 'stg'
        elif 'dev' in name_lower:
            env = 'dev'
        elif 'test' in name_lower:
            env = 'test'
        rows.append({
            'servername': host,
            'ip': ip_output,
            'env': env,
            'severity': ''
        })

with open(CSV_OUTPUT, mode='w', newline='') as csvfile:
    fieldnames = ['servername', 'ip', 'env', 'severity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ CSV file '{CSV_OUTPUT}' created with {len(rows)} servers.")
