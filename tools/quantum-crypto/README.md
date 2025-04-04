# 🔐 Quantum Crypto Toolkit

A custom, modular toolkit for solving cryptography challenges in Capture The Flag (CTF) competitions.  
This toolkit is maintained by the **Quantum Breach** CTF team and built from the ground up for flexibility, clarity, and hacking speed.

---

### Usage Notes

- This toolkit is designed for manual use and scripting in CTF environments.
- Each tool is standalone and easy to edit for specific challenge scenarios.
- Python 3+ is required.
- Pull requests are welcome from Quantum Breach team members.

## 📦 Included Tools

### 1. 🔢 modinv.py
- 📍 **Path**: `modinv.py`
- 🧮 **Purpose**: Calculates the modular inverse of two integers using the Extended Euclidean Algorithm.
- 🧪 **Use Case**: Common in RSA and Chinese Remainder Theorem (CRT) problems.
- 🧰 **Usage**:
  ```bash
  python3 modinv.py <a> <modulus>
  ```

  python3 modinv.py 3 11
➜ Modular inverse of 3 mod 11 is: 4

### 2. 🧩 rsa_common_modulus.py
- 📍 **Path**: `rsa_common_modulus.py`
- 🔐 **Purpose**: Recovers the original plaintext when the same RSA modulus is used with two different, co-prime exponents.
- ⚠️ **Condition**: `gcd(e1, e2) == 1`
- 🧰 **Usage**:
  ```bash
  python3 rsa_common_modulus.py <n> <e1> <e2> <c1> <c2>

#### Example
python3 rsa_common_modulus.py 3233 17 13 855 820






---






