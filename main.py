import sqlite3
import hashlib
import sys

sys.stdout.reconfigure(encoding='utf-8')

def database():
    conn = sqlite3.connect(r'users-challenge.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM users")
    data = cursor.fetchall()
    conn.close()
    return data

def decryption(encrypted_password):
    hashes_list = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'md5']

    with open(r'worldlist.txt', 'r', encoding='utf-8') as file:
        for row in file:
            password = row.strip()
            for i in hashes_list:
                decrypt = hashlib.new(i, password.encode()).hexdigest()
                if decrypt == encrypted_password:
                    return password
    return None

def main():
    db = database()

    for email, encrypted_password in db:
        decrypt_password =  decryption(encrypted_password)
        if decrypt_password:
            print(f"{email}: {decrypt_password} ok")
        else:
            print("Something went wrong")

if __name__ == "__main__":
    main()