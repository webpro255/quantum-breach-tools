#!/bin/bash

# Quantum Crypto Toolkit Launcher

logo() {
cat << "EOF"
      ____                  _                 
     / __ \____ ___________(_)___  ____  _____
    / / / / __ `/ ___/ ___/ / __ \/ __ \/ ___/
   / /_/ / /_/ (__  |__  ) / /_/ / /_/ (__  ) 
  /_____/\__,_/____/____/_/ .___/\____/____/  
                         /_/   Quantum Crypto Tools

EOF
}

check_deps() {
    command -v python3 >/dev/null 2>&1 || {
        echo "[!] Python3 not found. Please install it."
        exit 1
    }
}

menu() {
    echo "Choose a Quantum Crypto Tool to run:"
    echo " 01) ROT-N Brute Forcer"
    echo " 02) BaseN Auto Decoder"
    echo " 03) Python Escape Parser"
    echo " 04) ASCII to Hex/Bin/Dec"
    echo " 05) Image LSB Extractor"
    echo " 06) Audio LSB Extractor"
    echo " 07) Morse Code Decoder"
    echo " 08) OTP Reuse XOR Solver"
    echo " 09) RSA CRT Optimized"
    echo " 10) RSA Common Modulus Attack"
    echo " 11) RSA Low Exponent Attack"
    echo " 12) RSA FactorDB Lookup"
    echo " 13) Modular Inverse Solver"
    echo " 14) Chinese Remainder Theorem"
    echo " 15) LFSR Solver"
    echo " 16) XOR Cracker"
    echo " 17) Repeating-Key XOR Solver"
    echo " 18) Substitution Solver"
    echo " 19) Caesar Encrypt/Decrypt"
    echo " 20) Polybius Decoder"
    echo " 21) Rail Fence Decoder"
    echo " 22) Vigenère Cipher Solver"
    echo " 23) A1Z26 Decoder"
    echo " 24) Wordlist Generator"
    echo " 25) ASCII/Base Converter"
    echo " 26) Prime Factorizer"
    echo "  0) Exit"
    echo -n ">>> "
}

run_tool() {
    case $1 in
        1)  read -p "Ciphertext: " ct
            python3 ../tools/quantum-crypto/rot_cipher_tool.py "$ct" ;;
        2)  read -p "Encoded string: " s
            python3 ../tools/quantum-crypto/base_n_decoder.py "$s" ;;
        3)  read -p "Escaped string: " esc
            python3 ../tools/quantum-crypto/python_escape_parser.py "$esc" ;;
        4)  read -p "Direction (ascii2hex/ascii2bin/ascii2dec): " d
            read -p "Value: " v
            python3 ../tools/quantum-crypto/ascii_to_int.py "$d" "$v" ;;
        5)  read -p "Image path: " img
            read -p "Use --ascii? (y/n): " a
            [[ "$a" == "y" ]] && python3 ../tools/quantum-crypto/image_lsb_extractor.py "$img" --ascii \
                              || python3 ../tools/quantum-crypto/image_lsb_extractor.py "$img" ;;
        6)  read -p "Audio path (.wav): " audio
            read -p "Use --ascii? (y/n): " a
            [[ "$a" == "y" ]] && python3 ../tools/quantum-crypto/signal_lsb_decoder.py "$audio" --ascii \
                              || python3 ../tools/quantum-crypto/signal_lsb_decoder.py "$audio" ;;
        7)  read -p "Morse string: " m
            python3 ../tools/quantum-crypto/morse_decoder.py "$m" ;;
        8)  read -p "Hex1: " h1; read -p "Hex2: " h2
            python3 ../tools/quantum-crypto/otp_solver.py "$h1" "$h2" ;;
        9)  read -p "Ciphertext: " c; read -p "d: " d; read -p "p: " p; read -p "q: " q
            python3 ../tools/quantum-crypto/rsa_crt_recover.py "$c" "$d" "$p" "$q" ;;
       10)  python3 ../tools/quantum-crypto/rsa_common_modulus.py ;;
       11)  python3 ../tools/quantum-crypto/rsa_low_exponent.py ;;
       12)  read -p "Modulus (n): " n
            python3 ../tools/quantum-crypto/rsa_factor_db.py "$n" ;;
       13)  read -p "a: " a; read -p "mod m: " m
            python3 ../tools/quantum-crypto/modinv.py "$a" "$m" ;;
       14)  python3 ../tools/quantum-crypto/chinese_remainder.py ;;
       15)  python3 ../tools/quantum-crypto/lfsr_solver.py ;;
       16)  read -p "Hex-encoded ciphertext: " x
            python3 ../tools/quantum-crypto/xor_cracker.py "$x" ;;
       17)  read -p "Hex-encoded ciphertext: " x
            python3 ../tools/quantum-crypto/repeating_xor_solver.py "$x" ;;
       18)  read -p "Ciphertext: " ct
            python3 ../tools/quantum-crypto/substitution_solver.py "$ct" ;;
       19)  read -p "Text: " t; read -p "Shift: " s
            python3 ../tools/quantum-crypto/caesar_tool.py "$t" "$s" ;;
       20)  read -p "Polybius encoded (e.g., '11 21 31'): " p
            python3 ../tools/quantum-crypto/polybius_decoder.py "$p" ;;
       21)  read -p "Ciphertext: " c; read -p "Rails: " r
            python3 ../tools/quantum-crypto/rail_fence_decoder.py "$c" "$r" ;;
       22)  read -p "Ciphertext: " c; read -p "Key: " k
            python3 ../tools/quantum-crypto/vigenere_solver.py "$c" "$k" ;;
       23)  read -p "Numbers (e.g., '1 2 3 20'): " n
            python3 ../tools/quantum-crypto/a1z26_decoder.py "$n" ;;
       24)  read -p "Prefix (optional): " p
            python3 ../tools/quantum-crypto/wordlist_gen.py "$p" ;;
       25)  read -p "Direction (base2hex, hex2ascii, etc): " d; read -p "Value: " v
            python3 ../tools/quantum-crypto/base_converter.py "$d" "$v" ;;
       26)  read -p "Integer to factor: " n
            python3 ../tools/quantum-crypto/prime_factorizer.py "$n" ;;
        0)  echo "Goodbye, Operator."; exit 0 ;;
        *)  echo "Invalid option." ;;
    esac
}

# ---------------------- Main Execution ----------------------
clear
logo
check_deps

while true; do
    echo
    menu
    read choice
    run_tool "$choice"
    echo
done
