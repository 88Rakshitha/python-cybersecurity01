
import secrets
import string

chars = string.ascii_letters + string.digits + "@#$%&*1234567"
password = ''.join(secrets.choice(chars) for _ in range(10))

print("Secure password:", password)