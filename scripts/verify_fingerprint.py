#!/usr/bin/env python3
"""
Quick SHA-256 Fingerprint Verification
=======================================

This script performs a fast verification that you have the correct
Q₅₉ value without needing to compute the full polynomial.

If you already have the decimal string of the number, this script
will verify its SHA-256 fingerprint.

Author: Ruqing Chen
License: CC-BY-4.0
"""

import sys
import hashlib

# Expected fingerprint
EXPECTED_SHA256 = "A462032F37DC907EDEF64A575696EC0B11C052B42B469C76F6A6577B841864EF"
EXPECTED_DIGITS = 109433938


def verify_from_file(filepath):
    """Verify SHA-256 from a file containing the decimal number."""
    print(f"Reading from: {filepath}")
    
    try:
        with open(filepath, 'r') as f:
            content = f.read().strip()
        
        # Remove any whitespace or formatting
        number_str = ''.join(content.split())
        
        if not number_str.isdigit():
            print("❌ File does not contain a valid decimal number")
            return False
        
        print(f"Digits read: {len(number_str):,}")
        
        # Calculate SHA-256
        sha256_hash = hashlib.sha256(number_str.encode('utf-8')).hexdigest().upper()
        
        print(f"SHA-256: {sha256_hash}")
        
        # Verify
        if sha256_hash == EXPECTED_SHA256:
            print("✅ VERIFIED! This is the correct Q₅₉(10^1886792 + 3)")
            return True
        else:
            print("❌ MISMATCH! This is NOT the correct number")
            print(f"Expected: {EXPECTED_SHA256}")
            return False
            
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def verify_from_string(number_str):
    """Verify SHA-256 from a string."""
    # Remove any whitespace
    number_str = ''.join(number_str.split())
    
    if not number_str.isdigit():
        print("❌ Invalid input: not a decimal number")
        return False
    
    print(f"Digits: {len(number_str):,}")
    
    # Calculate SHA-256
    sha256_hash = hashlib.sha256(number_str.encode('utf-8')).hexdigest().upper()
    print(f"SHA-256: {sha256_hash}")
    
    # Verify
    if sha256_hash == EXPECTED_SHA256:
        print("✅ VERIFIED! This is the correct Q₅₉(10^1886792 + 3)")
        return True
    else:
        print("❌ MISMATCH! This is NOT the correct number")
        print(f"Expected: {EXPECTED_SHA256}")
        return False


def verify_partial(head_60, tail_60, total_digits):
    """Verify using just the head, tail, and digit count."""
    EXPECTED_HEAD = "590000000000000000000000000000000000000000000000000000000000"
    EXPECTED_TAIL = "000000000000000000000000000000014130386091162273752461387579"
    
    print("Partial Verification:")
    print(f"  Digits: {total_digits:,}")
    print(f"  Head: {head_60}")
    print(f"  Tail: {tail_60}")
    print()
    
    all_match = True
    
    if total_digits == EXPECTED_DIGITS:
        print(f"✓ Digit count matches: {total_digits:,}")
    else:
        print(f"✗ Digit count mismatch (expected {EXPECTED_DIGITS:,})")
        all_match = False
    
    if head_60 == EXPECTED_HEAD:
        print("✓ First 60 digits match")
    else:
        print("✗ First 60 digits mismatch")
        all_match = False
    
    if tail_60 == EXPECTED_TAIL:
        print("✓ Last 60 digits match")
    else:
        print("✗ Last 60 digits mismatch")
        all_match = False
    
    if all_match:
        print("\n✅ Partial verification successful!")
        print("Note: For complete verification, compute the full SHA-256 hash")
    else:
        print("\n❌ Partial verification failed!")
    
    return all_match


def main():
    """Main verification interface."""
    print("=" * 70)
    print("Q₅₉ FINGERPRINT VERIFICATION TOOL")
    print("=" * 70)
    print()
    print("This tool verifies that a number matches the documented")
    print("Q₅₉(10^1886792 + 3) candidate.")
    print()
    print("Expected SHA-256:", EXPECTED_SHA256)
    print("Expected Digits: ", f"{EXPECTED_DIGITS:,}")
    print()
    print("=" * 70)
    print()
    
    print("Choose verification method:")
    print("  1. Verify from file")
    print("  2. Verify partial (head/tail/digits only)")
    print("  3. Exit")
    print()
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == '1':
        filepath = input("Enter file path: ").strip()
        verify_from_file(filepath)
    
    elif choice == '2':
        print("\nEnter the following:")
        try:
            total_digits = int(input("  Total digits: ").strip().replace(',', ''))
            head_60 = input("  First 60 digits: ").strip()
            tail_60 = input("  Last 60 digits: ").strip()
            verify_partial(head_60, tail_60, total_digits)
        except ValueError:
            print("❌ Invalid input")
    
    elif choice == '3':
        print("Exiting...")
    
    else:
        print("Invalid choice")
    
    print()
    print("For more information:")
    print("  DOI: 10.5281/zenodo.18140813")
    print("  GitHub: https://github.com/Ruqing1963/q59-prime-candidate")
    print()


if __name__ == "__main__":
    main()
