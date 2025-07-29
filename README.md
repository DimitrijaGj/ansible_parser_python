# Server Inventory Report Generator

![ansible](https://img.shields.io/badge/Ansible-000000?style=for-the-badge&logo=ansible&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![git](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

This script uses Ansible to gather server IP addresses from an inventory file and generates a CSV report.

## Features

- Extracts server names, IP addresses, and environments (`prd`, `stg`, `dev`, `test`) from an Ansible inventory.
- Outputs a CSV file with columns: `servername`, `ip`, `env`, and `severity`.

## Prerequisites

- Python 3.6+
- Ansible
- Python packages: `ansible-runner`, `environs`

## Installation

1. Clone the repository and navigate to the directory:

2. (Optional) Create a virtual environment:
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root directory.
2. Add the path to your Ansible inventory file:
    ```
    INVENTORY_FILE=/path/toyour/file/inventory.yml
    ```

## Usage

Run the script to generate the CSV report:
```
python [srvr_inventory.py](http://_vscodecontentref_/0)
```