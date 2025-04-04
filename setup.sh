#!/bin/bash

# Setup script for Quantum Crypto Tools and Other Tools

echo "[*] Setting up Quantum Breach Tools..."

# Ensure we have Python3 and pip installed
command -v python3 >/dev/null 2>&1 || {
    echo "[!] Python3 is not installed. Please install Python3."
    exit 1
}

command -v pip3 >/dev/null 2>&1 || {
    echo "[!] pip3 is not installed. Please install pip3."
    exit 1
}

# Install required dependencies for both sets of tools
echo "[*] Installing required Python packages..."
pip3 install -r requirements.txt

# Make sure all Python scripts are executable
chmod +x ../tools/quantum-crypto/*.py

# Ensure the launchers are executable
chmod +x ../scripts/quantum_crypto_launcher.sh


# Success message
echo "[+] Setup Complete!"
echo "[*] You can now run the Quantum Crypto launcher with ./scripts/quantum_crypto_launcher.sh"

