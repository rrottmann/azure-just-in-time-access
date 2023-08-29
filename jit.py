import os
import uuid
import requests
import argparse

def jit(vm, rg, sub, ip="0.0.0.0/0", port=22, ssl_verify=True, showmyip="https://ifconfig.me/ip"):
    if ip == None:
        ip = requests.get(showmyip, verify=ssl_verify).text.strip()
    vm_details = os.popen(f'az vm show -g {rg} -n {vm} --subscription {sub} -o tsv --query "[id, location]"').read().split()
    vm_id = vm_details[0]
    location = vm_details[1]
    endpoint = f"https://management.azure.com/subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Security/locations/{location}/jitNetworkAccessPolicies/default/initiate?api-version=2015-06-01-preview"

    body = f'''
        {{
            "requests":[
                {{
                    "content":{{
                        "virtualMachines":[
                            {{
                                "id":"{vm_id}",
                                "ports":[
                                    {{
                                        "number":{port},
                                        "duration":"PT3H",
                                        "allowedSourceAddressPrefix":"{ip}"
                                    }}
                                ],
                                "justification": "Need Just-In-Time-Access to the VM."
                            }}
                        ]
                    }},
                    "httpMethod":"POST",
                    "name":"{str(uuid.uuid4())}",
                    "requestHeaderDetails":{{"commandName":"Microsoft_Azure_Compute."}},
                    "url":"{endpoint}"
                }}
            ]
        }}
    '''

    url = "https://management.azure.com/batch?api-version=2015-11-01"

    cmd = f'az rest --verbose --method post --uri "{url}" --body \'{body}\''
    os.system(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='JIT access for given Azure VM')
    parser.add_argument('--vm', type=str, required=True,
                        help='Name of the virtual machine')
    parser.add_argument('--rg', type=str, required=True,
                        help='Name of the Resource Group')
    parser.add_argument('--sub', type=str, required=True,
                        help='ID of the Subscription')
    parser.add_argument('--port', type=str, required=False,
                        help='Port to open', default="22")
    args = parser.parse_args()

    # Login to Azure
    os.system("az login --scope https://management.core.windows.net//.default")
    # Set Azure Subscription
    os.system(f"az account set --subscription {args.sub}")
    # Request Just-In-Time-Access
    jit(vm=args.vm, rg=args.rg, sub=args.sub, ip=None, port=args.port)
