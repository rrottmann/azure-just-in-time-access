# azure-just-in-time-access
Small Python script to request JIT-access for a virtual machine.

## Usage

```bash
./jit.py --vm myazurevm --rg myazurerg --sub d3ace655-9212-42db-83ca-ce031717d945
```
### Output
```
{
  "responses": [
    {
      "content": {
        "requestor": "***@***.**",
        "startTimeUtc": "2023-08-29T11:04:48.2696623Z",
        "virtualMachines": [
          {
            "id": "/subscriptions/***/resourceGroups/***/providers/Microsoft.Compute/virtualMachines/***",
            "ports": [
              {
                "allowedSourceAddressPrefix": "1xx.1xx.2xx.1xx",
                "endTimeUtc": "2023-08-29T14:04:48.2696623Z",
                "number": 22,
                "status": "Initiating",
                "statusReason": "UserRequested"
              }
            ]
          }
        ]
      },
      "contentLength": 428,
      "headers": {
        "Cache-Control": "no-cache",
        "Date": "Tue, 29 Aug 2023 11:04:48 GMT",
        "Pragma": "no-cache",
        "Server": "Kestrel",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "X-Content-Type-Options": "nosniff",
        "x-ms-correlation-request-id": "1f8b***",
        "x-ms-ratelimit-remaining-subscription-writes": "1199",
        "x-ms-request-id": "",
        "x-ms-routing-request-id": "GERMANYWESTCENTRAL:20230829T110448Z:c2071***"
      },
      "httpStatusCode": 202,
      "name": "b8e***"
    }
  ]
}
Command ran in 1.276 seconds (init: 0.061, invoke: 1.215)
```
