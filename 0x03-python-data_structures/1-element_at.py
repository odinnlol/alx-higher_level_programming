import re

def extract_ips(filename):
    # Regular expression pattern for matching IP addresses
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    with open(filename, 'r') as file:
        for line in file:
            # Find all IP addresses in the line
            ips = re.findall(ip_pattern, line)
            
            for ip in ips:
                print(ip)

# Using the provided filename
extract_ips('ips.txt')
