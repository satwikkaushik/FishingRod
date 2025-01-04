import requests
import json
import base64

# load the API_KEY file
API_KEY = ""
THRESHOLD = 0.0

with open("config.json", "r") as file:
    config = json.load(file)
    API_KEY = config.get("api_key")
    THRESHOLD = config.get("threshold")

REQ_HEADER = {
    "accept": "application/json",
        "x-apikey": API_KEY
}

def check(url):
    if(not API_rate_limiter()):
        return -1

    url = encode_url(url)

    try:
        VIRUSTOTAL_URL = f"https://www.virustotal.com/api/v3/urls/{url}"
        response = requests.get(VIRUSTOTAL_URL, headers = REQ_HEADER)

        # check for response status, auto generates exception if not 200
        response.raise_for_status()

        # parsing response
        parsed_response = response.json()["data"]["attributes"]["last_analysis_stats"]
        
        analysis_details = {
            "malicious_count" : parsed_response["malicious"],
            "suspicious_count" : parsed_response["suspicious"],
            "undetected_count" : parsed_response["undetected"],
            "harmless_count" : parsed_response["harmless"],
            "timeout_count" : parsed_response["timeout"]
        }

        return determine_result(analysis_details)
    
    except Exception as e:
        print(e)
        return -1

def encode_url(url):
    # base64 url encoding is required by virusTotal API
    return base64.urlsafe_b64encode(url.encode()).decode().strip('=')

def determine_result(analysis_details):
    if(analysis_details["malicious_count"] > 1):
        return 1

    return 0

def API_rate_limiter():
    from datetime import datetime

    config = ""
    with open("config.json", "r") as file:
        config = json.load(file)
    
    prev_timestamp = config.get("prev_timestamp")
    current_timestamp = datetime.now().timestamp()

    if(round(current_timestamp - prev_timestamp) > 60):
        config["prev_timestamp"] = current_timestamp
        config["API_call_count"] = 1

        with open("config.json", "w") as file:
            json.dump(config, file, indent=4)

        return True
    elif(config.get("API_call_count") < 4):
        config["API_call_count"] += 1
        config["prev_timestamp"] = current_timestamp
        
        with open("config.json", "w") as file:
            json.dump(config, file, indent=4)

        return True
    else:
        return False