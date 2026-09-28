# Vigenere Cipher (Medium)
# Encode and decode text with a polyalphabetic Vigenere cipher, preserving
# case and passing non-letters through untouched.
# Time: O(n) | Space: O(n)

def _shifted(text, key, sign):
    key = [c for c in key.lower() if c.isalpha()]
    if not key:
        raise ValueError("key must contain at least one letter")
    result, ki = [], 0
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            shift = ord(key[ki % len(key)]) - ord("a")
            result.append(chr((ord(ch) - base + sign * shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return "".join(result)

def vigenere_encode(text, key):
    return _shifted(text, key, 1)

def vigenere_decode(text, key):
    return _shifted(text, key, -1)

# Tests
assert vigenere_encode("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
assert vigenere_decode("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"
assert vigenere_decode(vigenere_encode("Hello, World!", "key"), "key") == "Hello, World!"
print("All tests passed!")
