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

### 3. 🧪 xor_cracker.py
- 📍 **Path**: `xor_cracker.py`
- 🔓 **Purpose**: Cracks single-byte XOR-encrypted strings using English frequency scoring.
- 🧰 **Usage**:
  ```bash
  python3 xor_cracker.py <hex_string>

#### Example
python3 xor_cracker.py 1b37373331363f78151b7f2b783431333d78397828372d36

### 4. 🔁 chinese_remainder.py
- 📍 **Path**: `chinese_remainder.py`
- 📚 **Purpose**: Solves systems of modular congruences using the Chinese Remainder Theorem (CRT).
- 🧰 **Usage**:
  ```bash
  python3 chinese_remainder.py

#### Example Input:
n = 3 5
a = 2 3
<br>➜ Output: x ≡ 8 mod 15</br>













---






