#julian Pena
#https://www.analyticsvidhya.com/blog/2024/01/ways-to-convert-python-scripts-to-exe-files/
#https://hackerbase.pro/blog/1950
#second part sources
#https://www.geeksforgeeks.org/md5-hash-python/
#https://www.youtube.com/watch?v=CGvZLlaEvAE
#https://stackoverflow.com/questions/68454119/generate-md5-hash-of-file-and-compare-to-md5-hash-value-from-import-txt-file
#i have to used chatgbt for the final touches.
import os
import hashlib
import requests  
from datetime import datetime

def generate_md5(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def get_virustotal_report(md5_hash, api_key):
    url = f"https://www.virustotal.com/api/v3/files/{md5_hash}"
    headers = {
        "x-apikey": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def search_files(api_key):
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")
    files_searched = hits_found = total_positives = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            md5_hash = generate_md5(full_path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file_size = os.path.getsize(full_path)
            
            print(f"Timestamp: {timestamp}, File Path: {full_path}, File Size: {file_size} bytes, MD5 Hash: {md5_hash}")
            files_searched += 1
            
            if file == file_name:
                hits_found += 1
            
            report = get_virustotal_report(md5_hash, api_key)
            if report and 'data' in report and 'attributes' in report['data']:
                positives = report['data']['attributes']['last_analysis_stats']['malicious']
                total_positives += positives
                print(f"VirusTotal Positives: {positives}")
            else:
                print("No report available from VirusTotal for this file.")
    
    print(f"\nSearch completed. Total files searched: {files_searched}, Total hits found: {hits_found}, Total positives detected: {total_positives}")

if __name__ == "__main__":
    api_key = os.getenv('API_KEY_VIRUSTOTAL')
    if not api_key:
        print("Error: API key for VirusTotal not found. Please set it as an environment variable 'API_KEY_VIRUSTOTAL'.")
    else:
        search_files(api_key)
