from solana.keypair import Keypair
import json
import base58
from pathlib import Path
import time

class SolanaWalletGenerator:
    def __init__(self):
        self.wallets = []
        
    def generate_wallets(self, number_of_wallets: int):
        """Generate the specified number of Solana wallets"""
        print(f"Generating {number_of_wallets} Solana wallets...")
        
        for _ in range(number_of_wallets):
            # Generate new keypair
            keypair = Keypair()
            
            wallet = {
                'public_key': str(keypair.public_key),
                'private_key': base58.b58encode(keypair.secret_key).decode('ascii'),
            }
            
            self.wallets.append(wallet)
            
    def save_to_file(self, filename: str = "solana_wallets.json"):
        """Save the generated wallets to a JSON file"""
        output_path = Path(filename)
        
        with open(output_path, 'w') as f:
            json.dump(self.wallets, f, indent=4)
            
        print(f"\nWallets saved to {output_path.absolute()}")
        
    def print_wallets(self):
        """Print all generated wallets to console"""
        for i, wallet in enumerate(self.wallets, 1):
            print(f"\nWallet #{i}")
            print(f"Public Key: {wallet['public_key']}")
            print(f"Private Key: {wallet['private_key']}")

def main():
    # Create generator instance
    generator = SolanaWalletGenerator()
    
    # Get number of wallets to generate from user
    while True:
        try:
            num_wallets = int(input("How many wallets do you want to generate? "))
            if num_wallets > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Record start time
    start_time = time.time()
    
    # Generate wallets
    generator.generate_wallets(num_wallets)
    
    # Save wallets to file
    generator.save_to_file()
    
    # Print wallets to console
    generator.print_wallets()
    
    # Print execution time
    execution_time = time.time() - start_time
    print(f"\nExecution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main() 