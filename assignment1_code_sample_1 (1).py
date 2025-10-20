import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123' #OWASP A07 - Identification and Authentication Failure
    # Vulnerability - Hardcoded credentials in source code
}

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input # OWASP A03 - Injection
    # Vulnerability: No input validation or sanitization

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}') # OWASP A03 - Command Injection
    # Vulnerability - Command injection via os.system()

def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data # OWASP A02 - Cryptographic Failures
    # Vulnerability - Insecure HTTP connection instead of HTTPS

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close() #OWASP A03 - SQL Injection
    # Vulnerability - SQL injection via string concatenation

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
