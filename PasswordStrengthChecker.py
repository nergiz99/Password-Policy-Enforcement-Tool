"""
Password Strength Checker Tool
Includes entropy calculation, common password checking, and Secure Password Generator module.
"""

import getpass
import math
import string
import random


def calculate_entropy(password):
    """
    Calculate the Shannon Entropy of a password.
    
    Args:
        password (str): The password to analyze
        
    Returns:
        float: Entropy value in bits
    """
    if not password:
        return 0.0
    
    L = len(password)  # Password length
    
    # Determine character space
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    # Character set sizes
    N = 0
    if has_lower:
        N += 26  # lowercase letters
    if has_upper:
        N += 26  # uppercase letters
    if has_digit:
        N += 10  # digits
    if has_special:
        N += 32  # special symbols (approximately)
    
    # Calculate entropy: H = L * log2(N)
    if N == 0:
        return 0.0
    
    entropy = L * math.log2(N)
    return entropy


def check_common_password(password, common_list_file):
    """
    Check if the password is in the common passwords list.
    
    Args:
        password (str): The password to check
        common_list_file (str): Path to the file containing common passwords
        
    Returns:
        bool: True if password is found in the list, False otherwise
    """
    try:
        with open(common_list_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Strip whitespace and check for exact match
                if line.strip() == password:
                    return True
        return False
    except FileNotFoundError:
        print(f"Warning: Common passwords file '{common_list_file}' not found.")
        return False
    except Exception as e:
        print(f"Error reading common passwords file: {e}")
        return False


def get_strength_rating(entropy):
    """
    Get a strength rating based on entropy value.
    
    Args:
        entropy (float): Entropy value in bits
        
    Returns:
        tuple: (rating, suggestions)
    """
    if entropy < 40:
        rating = "Very Weak"
        suggestions = [
            "Increase password length (aim for at least 12-16 characters)",
            "Add uppercase letters",
            "Add lowercase letters",
            "Add numbers",
            "Add special characters (!@#$%^&*, etc.)"
        ]
    elif entropy < 60:
        rating = "Medium"
        suggestions = [
            "Consider increasing password length further",
            "Ensure you're using a mix of all character types",
            "Avoid dictionary words or common patterns"
        ]
    else:
        rating = "Strong"
        suggestions = [
            "Your password has good entropy",
            "Consider using a password manager for even stronger unique passwords",
            "Make sure this password is unique and not reused elsewhere"
        ]
    
    return rating, suggestions


def ctf_secure_generator():
    """
    CTF Solution Module: Secure Password Generator
    
    This function generates a secure password that meets enterprise security policy:
    - Minimum 10 characters length
    - At least one uppercase letter
    - At least one number (digit)
    - At least one special character
    
    This is the solution to the weak password problem identified in Option 1.
    """
    print("\n" + "="*60)
    print("CTF SOLUTION: Secure Password Generated")
    print("="*60)
    
    # Policy requirements
    min_length = 10
    
    # Character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure we have at least one of each required type
    password_chars = []
    
    # Add one of each required character type
    password_chars.append(random.choice(uppercase))
    password_chars.append(random.choice(digits))
    password_chars.append(random.choice(special_chars))
    
    # Fill the rest with random characters from all sets
    all_chars = uppercase + lowercase + digits + special_chars
    
    # Generate remaining characters to reach minimum length
    remaining_length = max(0, min_length - len(password_chars))
    for _ in range(remaining_length):
        password_chars.append(random.choice(all_chars))
    
    # Add some additional random characters for better entropy (12-16 chars total)
    additional_length = random.randint(2, 6)
    for _ in range(additional_length):
        password_chars.append(random.choice(all_chars))
    
    # Shuffle to randomize positions
    random.shuffle(password_chars)
    
    # Generate final password
    secure_password = ''.join(password_chars)
    
    # Verify the generated password meets all requirements
    has_upper = any(c in uppercase for c in secure_password)
    has_digit = any(c in digits for c in secure_password)
    has_special = any(c in special_chars for c in secure_password)
    has_min_length = len(secure_password) >= min_length
    
    # Display the generated password
    print(f"\nGenerated Secure Password: {secure_password}")
    print(f"\nPassword Length: {len(secure_password)} characters")
    
    # Calculate and display entropy
    entropy = calculate_entropy(secure_password)
    print(f"Entropy: {entropy:.2f} bits")
    
    print("\n" + "-"*60)
    print("Policy Compliance Check:")
    print("-"*60)
    print(f"  ✓ Minimum Length (≥10): {'PASS' if has_min_length else 'FAIL'} ({len(secure_password)} chars)")
    print(f"  ✓ Contains Uppercase: {'PASS' if has_upper else 'FAIL'}")
    print(f"  ✓ Contains Number: {'PASS' if has_digit else 'FAIL'}")
    print(f"  ✓ Contains Special Character: {'PASS' if has_special else 'FAIL'}")
    print(f"  ✓ Entropy ≥ 40 bits: {'PASS' if entropy >= 40 else 'FAIL'} ({entropy:.2f} bits)")
    
    print("\n" + "="*60)
    print("This auto-generated password meets all enterprise security standards.")
    print("It is safe to use and complies with organizational password policy.")
    print("="*60)
    
    return secure_password


def main():
    """
    Main function to run the password strength checker.
    Prompts user for password input and runs all checks.
    """
    print("="*60)
    print("Password Strength Checker")
    print("="*60)
    print("\nOptions:")
    print("1. Check password strength")
    print("2. Secure Password Generator")
    print("3. Exit")
    
    choice = input("\nSelect an option (1-3): ").strip()
    
    if choice == "1":
        # Securely prompt for password using getpass
        password = getpass.getpass("\nEnter password to check (characters will be hidden): ")
        
        if not password:
            print("Error: No password entered.")
            return
        
        print("\n" + "="*60)
        print("Password Strength Analysis")
        print("="*60)
        
        # Calculate entropy
        entropy = calculate_entropy(password)
        print(f"\nPassword Length: {len(password)} characters")
        print(f"Entropy: {entropy:.2f} bits")
        
        # Check against common passwords
        is_common = check_common_password(password, 'common_passwords.txt')
        
        # Recalculate Mandatory Character Booleans
        # Determine the presence of required character sets using string constants
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        # Check for Policy Violation
        # Policy Violation: found in common_passwords.txt OR entropy < 40 bits
        # OR missing mandatory character types (uppercase, digit, special)
        policy_violation = False
        violation_reasons = []
        
        if is_common:
            policy_violation = True
            violation_reasons.append("Password found in common passwords list")
            print("\n⚠️  DANGER! This is a known, widely used password.")
            print("   Using this password puts your account at high risk of compromise.")
        
        if entropy < 40:
            policy_violation = True
            violation_reasons.append(f"Entropy ({entropy:.2f} bits) is below minimum threshold (40 bits)")
        
        # Add Explicit Policy Violation Checks for mandatory characters
        if not has_upper:
            policy_violation = True
            violation_reasons.append("Missing required Uppercase letter")
        
        if not has_digit:
            policy_violation = True
            violation_reasons.append("Missing required Number (Digit)")
        
        if not has_special:
            policy_violation = True
            violation_reasons.append("Missing required Special Character")
        
        # If policy violation detected, refuse the password
        if policy_violation:
            print("\n" + "="*60)
            print("⚠️  POLICY VIOLATION: This password fails the enterprise security")
            print("   standard and cannot be set.")
            print("="*60)
            print("\nViolation Reasons:")
            for reason in violation_reasons:
                print(f"  • {reason}")
            print("\nPlease try a new password, or use Option 2 for an auto-generated")
            print("secure password.")
            print("="*60)
            return  # Return to main menu
        
        # If password passes policy check, show approval and details
        print("\n✓ Password Policy Compliance: PASSED")
        
        # Get strength rating and suggestions
        rating, suggestions = get_strength_rating(entropy)
        print(f"\nStrength Rating: {rating}")
        
        print("\nRecommendations:")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"  {i}. {suggestion}")
        
        # Additional security tips
        print("\n" + "-"*60)
        print("Security Tips:")
        print("  • Never reuse passwords across different accounts")
        print("  • Use a password manager to generate and store strong passwords")
        print("  • Enable two-factor authentication when available")
        print("  • Avoid using personal information in passwords")
        print("="*60)
        
    elif choice == "2":
        ctf_secure_generator()
    elif choice == "3":
        print("\nExiting. Stay secure!")
        return
    else:
        print("Invalid option. Please run the program again.")


if __name__ == "__main__":
    main()
