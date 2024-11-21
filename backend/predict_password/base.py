max_characters = 60

def extract_features(password):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "~!@#$%^&*()_-=+\\/|?.<>,;:"

    lowercase_count = sum(1 for c in password if c in lowercase)
    uppercase_count = sum(1 for c in password if c in uppercase)
    digits_count = sum(1 for c in password if c in digits)
    special_count = sum(1 for c in password if c in special_characters)

    security_score = (1.1 ** lowercase_count) * (1.2 ** uppercase_count) * (1.3 ** digits_count) * (1.5 ** special_count)

    return [lowercase_count, uppercase_count, digits_count, special_count, security_score]