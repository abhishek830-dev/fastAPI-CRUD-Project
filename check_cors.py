import urllib.request
import urllib.parse
import json

url = "https://fastapi-crud-project-2-2sm8.onrender.com/products"
headers = {
    "Origin": "https://fast-api-crud-project.vercel.app",
    "Access-Control-Request-Method": "GET"
}

req = urllib.request.Request(url, method="OPTIONS", headers=headers)

output = []

try:
    output.append(f"Sending OPTIONS request to {url}...")
    with urllib.request.urlopen(req) as response:
        output.append(f"Status Code: {response.status}")
        output.append("Headers:")
        
        headers_dict = dict(response.getheaders())
        for k, v in headers_dict.items():
            if "access-control" in k.lower():
                output.append(f"{k}: {v}")
                
        allow_origin = headers_dict.get("access-control-allow-origin") or headers_dict.get("Access-Control-Allow-Origin")
        allow_creds = headers_dict.get("access-control-allow-credentials") or headers_dict.get("Access-Control-Allow-Credentials")
        
        output.append("\n--- Analysis ---")
        output.append(f"Access-Control-Allow-Origin: {allow_origin}")
        output.append(f"Access-Control-Allow-Credentials: {allow_creds}")
        
        if allow_origin == "*" and (allow_creds is None or allow_creds.lower() == 'false'):
             output.append("SUCCESS: Backend seems to be updated correctly (Wildcard origin, credentials disabled/missing).")
        elif allow_origin == "*" and allow_creds == "true":
             output.append("FAILURE: Backend NOT updated yet (Still has credentials=true).")
        else:
             output.append("UNCERTAIN: unexpected verification result.")

except urllib.error.HTTPError as e:
    output.append(f"HTTP Error: {e.code} {e.reason}")
    output.append("Headers:")
    output.append(str(e.headers))
except Exception as e:
    output.append(f"Error: {e}")

with open("cors_result.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print("Done writing to cors_result.txt")
