import re

def count_valid_emails(emails):
    if not isinstance(emails, list):
        return 0
    
 
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    count = 0
    for email in emails:
        if isinstance(email, str) and email_pattern.match(email):
            count += 1
    
    return count
