# Fishing Rod

## What is it?
- It is a tool for detecting phising websites
- It uses two methods to formualte result:
    1. It uses services provided by VirusTotal to detect if URL is phising URL
    2. It extends it further by checking all the forwarding links against VirusTotal's database
    3. It uses a ML model that analyzes website's conent to further fine-tune the results

## Entrypoint
- `App.py` is the entrypoint
- run the command `streamlit run app.py` to start the execution