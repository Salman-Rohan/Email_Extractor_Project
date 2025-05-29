import re
import csv

def extract_emails_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regex দিয়ে email match
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', content)

    # Duplicate remove করে set বানালাম
    unique_emails = list(set(emails))

    # CSV তে সেভ
    with open('emails.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Email'])  # Header
        for email in unique_emails:
            writer.writerow([email])
    
    print(f"✅ {len(unique_emails)} email(s) found and saved to 'emails.csv'.")

# চালানোর অংশ
if __name__ == "__main__":
    filename = input("📁 Enter the .txt file path: ")
    extract_emails_from_file(filename)

