import sqlite3
import hashlib

def process_database():
    conn = sqlite3.connect(r'users-challenge.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM users")
    data = cursor.fetchall()
    conn.close()

    hashes_list = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'md5']

    with open(r'worldlist.txt', 'r', encoding='utf-8') as file:
        for email, encrypted_password in data:
            password_found = False
            for row in file:
                password = row.strip()
                for i in hashes_list:
                    decrypt = hashlib.new(i, password.encode()).hexdigest()
                    if decrypt == encrypted_password:
                        print(f"{email}: {password} ok")
                        password_found = True
                        break
                if password_found:
                    break
            else:
                print(f"Could not decrypt password for {email}")

def main():
    process_database()

if __name__ == "__main__":
    main()
