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
  ```

#### Example
python3 rsa_common_modulus.py 3233 17 13 855 820

### 3. 🧪 xor_cracker.py
- 📍 **Path**: `xor_cracker.py`
- 🔓 **Purpose**: Cracks single-byte XOR-encrypted strings using English frequency scoring.
- 🧰 **Usage**:
  ```bash
  python3 xor_cracker.py <hex_string>
  ```

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

### 5. 🔓 rsa_low_exponent.py
- 📍 **Path**: `rsa_low_exponent.py`
- 🧨 **Purpose**: Exploits small public exponents in RSA (typically e=3) when the message is small and unpadded.
- 📘 **Theory**: If `m^e < n`, then `c = m^e` and m = c^(1/e)
- 🧰 **Usage**:
  ```bash
  python3 rsa_low_exponent.py <ciphertext> <e> <n>
  ```

#### Purpose:
Cracks RSA when a small public exponent (e = 3) is used with no padding and the plaintext is small enough that:
c = m^e < n
#### Example 
python3 rsa_low_exponent.py 948221 3 13264529
<br>➜ Output:</br>
Recovered message (decimal): 453
ASCII message: E

### 6. 🧬 lfsr_solver.py
- 📍 **Path**: `lfsr_solver.py`
- ⚙️ **Purpose**: Uses the Berlekamp-Massey algorithm to reverse engineer a Linear Feedback Shift Register (LFSR) from a binary keystream.
- 🧰 **Usage**:
  ```bash
  python3 lfsr_solver.py <binary_string>
  ```

#### Example 
python3 lfsr_solver.py 100101100110111
<br>
➜ Output:</br>
[+] LFSR Length: 6 <br>
[+] Feedback Polynomial Coefficients: [1, 0, 1, 1, 0, 0, 1]</br>

### 7. 🔢 base_converter.py
- 📍 **Path**: `base_converter.py`
- 🧰 **Purpose**: Converts data between base64, hex, decimal, and binary. Useful in encoding/decoding challenges.
- 🧪 **Usage**:
  ```bash
  python3 base_converter.py <value> <from_base> <to_base>
  ```

#### Example
python3 base_converter.py TWF0aA== base64 hex
➜ 4d617468

python3 base_converter.py deadbeef hex base64
➜ 3q2+7w==

### 8. 🔏 rsa_factor_db.py
- 📍 **Path**: `rsa_factor_db.py`
- 🔓 **Purpose**: Uses FactorDB.com API to factor RSA modulus `n`, and optionally decrypt the ciphertext if `e` and `c` are provided.
- 📦 Requires: `requests` and `pycryptodome`
- 🧰 **Usage**:
  ```bash
  python3 rsa_factor_db.py <n>
  python3 rsa_factor_db.py <n> <e> <c>
  ```

#### Example
python3 rsa_factor_db.py 3233
➜ Factors of n: [61, 53]

python3 rsa_factor_db.py 3233 17 855
➜ Decrypted message: b'E'

### 9. 🔑 wiener_attack.py
- 📍 **Path**: `wiener_attack.py`
- 🕵️‍♂️ **Purpose**: Attempts Wiener's attack on RSA when the private exponent `d` is too small.
- 🧰 **Usage**:
  ```bash
  python3 wiener_attack.py <e> <n> <c>
  ```

#### Example 
python3 wiener_attack.py 17993 90581 77599 <br>
➜ Found d: 157<br>
➜ Decrypted message: FLAG{wiener_vuln}</br>

### 10. 🧾 ascii_to_int.py
- 📍 **Path**: `ascii_to_int.py`
- 📦 **Purpose**: Converts between ASCII, Hex, Decimal, and Binary. Great for encoding/decoding in Web, Crypto, and Reversing challenges.
- 🧰 **Usage**:
  ```bash
  python3 ascii_to_int.py <direction> <value>
  ```
  #### Example 
python3 ascii_to_int.py ascii2hex Hello
➜ 48656c6c6f

python3 ascii_to_int.py hex2ascii 48656c6c6f
➜ Hello


### 11. 🖼 image_lsb_extractor.py
- 📍 **Path**: `image_lsb_extractor.py`
- 🔍 **Purpose**: Extracts hidden LSB (Least Significant Bit) data from images — great for Stego and Forensics CTFs.
- 📦 Requires: `Pillow` (install via `pip install pillow`)
- 🧰 **Usage**:
  ```bash
  python3 image_lsb_extractor.py <image_path> [--bits <1-8>] [--ascii]

#### Example
python3 image_lsb_extractor.py secret.png --ascii<br>
➜ Hidden message: "FLAG{pixels_hide_truth}"</br>

### 12. 🔑 otp_solver.py
- 📍 **Path**: `otp_solver.py`
- 🔐 **Purpose**: XORs two ciphertexts encrypted with the same One-Time Pad key to recover XORed plaintext. Common vulnerability when OTP is reused.
- 🧰 **Usage**:
  ```bash
  python3 otp_solver.py <hex_cipher1> <hex_cipher2>

#### Example
python3 otp_solver.py 6c73d5240a948c86981bc294814d 3b101c091d53320c000910<br>
➜ XOR result (ASCII): W..R.C...B...Y.</br>

### 13. 🐍 python_escape_parser.py
- 📍 **Path**: `python_escape_parser.py`
- 🧠 **Purpose**: Decodes Python-style escaped strings like `\\x41`, `\\u0042`, etc. Great for reversing obfuscated payloads or memory strings.
- 🧰 **Usage**:
  ```bash
  python3 python_escape_parser.py "\\\\x66\\\\x6c\\\\x61\\\\x67"
  ➜ [+] Decoded: flag
  ```
### 14. 🎭 morse_decoder.py
- 📍 **Path**: `morse_decoder.py`
- 🪙 **Purpose**: Converts Morse code (using `.`, `-`, and `/`) into readable ASCII text. Great for forensics and stego-style challenges.
- 🧰 **Usage**:
  ```bash
  python3 morse_decoder.py "... --- ..."
  ➜ [+] Decoded message: SOS
  ```

  ### 15. 🔁 rot_cipher_tool.py
- 📍 **Path**: `rot_cipher_tool.py`
- 🌀 **Purpose**: Brute-force Caesar ciphers by rotating letters 1–25 positions. Essential for quick wins in classic crypto problems.
- 🧰 **Usage**:
  ```bash
  python3 rot_cipher_tool.py "Uifsf jt b gmbh!"
  ```

  ### 16. 🧬 repeating_xor_solver.py
- 📍 **Path**: `repeating_xor_solver.py`
- 🔑 **Purpose**: Detects and breaks repeating-key XOR (e.g., Vigenère). Tries top 3 key lengths and prints partial plaintexts.
- 🧰 **Usage**:
  ```bash
  python3 repeating_xor_solver.py <hex_encoded_cipher>
  ```
  #### Example
  python3 repeating_xor_solver.py 2b31342b31342b7a6d73636e<br>
➜ Key guess: FLAG<br>
➜ Decrypted: The quick brown fox jumps over...</br>


### 17. 🧠 substitution_solver.py
- 📍 **Path**: `substitution_solver.py`
- 🧩 **Purpose**: Aids in solving monoalphabetic substitution ciphers using frequency analysis and auto key mapping.
- 🧰 **Usage**:
  ```bash
  python3 substitution_solver.py "<ciphertext>"
  ```
#### Example 
python3 substitution_solver.py "XLMW MW E XST!"<br>
➜ Mapping: X→T, L→H, M→E, W→R...<br>
➜ Decrypted: "THIS IS A TOP!"</br>

### 18. 🔐 rsa_crt_recover.py
- 📍 **Path**: `rsa_crt_recover.py`
- ⚡ **Purpose**: Uses Chinese Remainder Theorem (CRT) for efficient RSA decryption when `p`, `q`, and `d` are known.
- 🧰 **Usage**:
  ```bash
  python3 rsa_crt_recover.py <c> <d> <p> <q>
  ```
#### Example 
python3 rsa_crt_recover.py 855 157 61 53<br>
➜ Recovered message (decimal): 69<br>
➜ ASCII message: E</br>


### 19. 📜 base_n_decoder.py
- 📍 **Path**: `base_n_decoder.py`
- 🔍 **Purpose**: Automatically detects and decodes data encoded in base64, hex, binary, or decimal — useful for quick triage of payloads in forensics and web CTFs.
- 🧰 **Usage**:
  ```bash
  python3 base_n_decoder.py "48656c6c6f"
  ➜ [+] Detected hex → Hello
  ```



  


















---






