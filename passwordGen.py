import secrets
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password


print("=" * 45)
print("       🔐 PASSWORD GENERATOR")
print("=" * 45)

try:
    length = int(input("\nEnter password length: "))

    if length < 4:
        print("\n❌ Password should be at least 4 characters.")
    else:
        password = generate_password(length)

        print("\n✅ Your secure password:")
        print("\n" + password)
        print("\n🔐 Keep it private!")

except ValueError:
    print("\n❌ Please enter a valid number.")
