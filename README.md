# Solana Wallet Generator

A Python-based tool for generating multiple Solana wallets quickly and efficiently. This tool allows you to create any number of Solana wallets and saves them in a JSON file for easy access.

## Features

- Generate multiple Solana wallets simultaneously
- Save wallet information (public and private keys) to a JSON file
- Display wallet information in the console
- Track execution time for wallet generation

## Requirements

- Python 3.6+
- Required Python packages:
  - solana
  - base58

## Installation

1. Clone this repository or download the source code
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```bash
python solana_wallet_generator.py
```

The program will:
1. Prompt you to enter the number of wallets you want to generate
2. Generate the specified number of wallets
3. Save the wallets to a file named `solana_wallets.json`
4. Display the generated wallet information in the console
5. Show the total execution time

## Output Format

The generated wallets are saved in a JSON file with the following structure:

```json
[
    {
        "public_key": "public_key_string",
        "private_key": "private_key_string"
    },
    ...
]
```

## Security Notice

⚠️ **Important**: Keep your private keys secure and never share them. Anyone with access to a private key has complete control over that wallet.

## License

This project is open source and available under the MIT License. 