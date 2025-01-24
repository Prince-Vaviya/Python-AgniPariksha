import re

def extract_email_addresses(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    email_addresses = re.findall(email_pattern, text)
    
    return email_addresses


sample_text = """
Here are some email addresses:
alice@example.com
bob.smith@company.org
charlie123@sub.domain.co.uk
invalid-email@.com
another.invalid@domain
"""

extracted_emails = extract_email_addresses(sample_text)

print("Extracted Email Addresses:")
for email in extracted_emails:
    print(email)