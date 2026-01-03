#!/usr/bin/env python3
"""
Q₅₉ Polynomial Computation Script
==================================

Computes the 109-million-digit candidate: Q₅₉(10^1886792 + 3)

Formula: Q_n(q) = q^n - (q-1)^n
Parameters: n=59, q=10^1886792 + 3

Author: Ruqing Chen
Date: January 3, 2026
License: CC-BY-4.0
DOI: 10.5281/zenodo.18140813
"""

import sys
import hashlib
import time
import os

# CRITICAL: Remove Python's default limit for integer to string conversion
sys.set_int_max_str_digits(0)

# Parameters
Q_EXPONENT = 1886792
N_POLYNOMIAL = 59
OFFSET = 3

# Expected results for verification
EXPECTED_SHA256 = "A462032F37DC907EDEF64A575696EC0B11C052B42B469C76F6A6577B841864EF"
EXPECTED_DIGITS = 109433938
EXPECTED_HEAD_60 = "590000000000000000000000000000000000000000000000000000000000"
EXPECTED_TAIL_60 = "000000000000000000000000000000014130386091162273752461387579"


def compute_q59():
    """
    Compute Q₅₉(q) = q^59 - (q-1)^59 where q = 10^1886792 + 3
    
    Returns:
        tuple: (computed_value, computation_time)
    """
    print("=" * 70)
    print("Q₅₉ POLYNOMIAL COMPUTATION")
    print("=" * 70)
    print(f"Formula: Q_{N_POLYNOMIAL}(q) = q^{N_POLYNOMIAL} - (q-1)^{N_POLYNOMIAL}")
    print(f"Base (q): 10^{Q_EXPONENT} + {OFFSET}")
    print("=" * 70)
    
    # Stage 1: Construct the base
    print("\n[Stage 1/4] Constructing base q...")
    start_time = time.time()
    q = 10**Q_EXPONENT + OFFSET
    print(f"✓ Base constructed in {time.time() - start_time:.2f}s")
    
    # Stage 2: Polynomial evaluation
    print("\n[Stage 2/4] Computing polynomial expansion...")
    stage_start = time.time()
    q_power = q**N_POLYNOMIAL
    q_minus_1_power = (q - 1)**N_POLYNOMIAL
    print(f"✓ Powers computed in {time.time() - stage_start:.2f}s")
    
    # Stage 3: Final calculation
    print("\n[Stage 3/4] Computing final difference...")
    stage_start = time.time()
    result = q_power - q_minus_1_power
    print(f"✓ Result computed in {time.time() - stage_start:.2f}s")
    
    total_time = time.time() - start_time
    return result, total_time


def analyze_result(value, computation_time):
    """
    Analyze the computed value and generate identity certificate.
    
    Args:
        value: The computed integer
        computation_time: Time taken for computation
    """
    print("\n[Stage 4/4] Generating identity certificate...")
    stage_start = time.time()
    
    # Convert to string
    print("  Converting to decimal string...")
    value_str = str(value)
    total_digits = len(value_str)
    
    # Calculate SHA-256
    print("  Calculating SHA-256 fingerprint...")
    sha256_hash = hashlib.sha256(value_str.encode('utf-8')).hexdigest().upper()
    
    # Extract head and tail
    head_60 = value_str[:60]
    tail_60 = value_str[-60:]
    
    analysis_time = time.time() - stage_start
    
    print(f"✓ Analysis complete in {analysis_time:.2f}s")
    
    # Display results
    print("\n" + "=" * 70)
    print("COMPUTATION COMPLETE - IDENTITY CERTIFICATE")
    print("=" * 70)
    print(f"\nTotal Decimal Digits: {total_digits:,}")
    print(f"SHA-256 Fingerprint:  {sha256_hash}")
    print(f"\nFirst 60 digits: {head_60}")
    print(f"Last 60 digits:  {tail_60}")
    print(f"\nComputation Time: {computation_time:.2f}s")
    print(f"Analysis Time:    {analysis_time:.2f}s")
    print(f"Total Time:       {computation_time + analysis_time:.2f}s")
    
    # Verification
    print("\n" + "=" * 70)
    print("VERIFICATION")
    print("=" * 70)
    
    verified = True
    
    if total_digits == EXPECTED_DIGITS:
        print(f"✓ Digit count matches: {total_digits:,}")
    else:
        print(f"✗ Digit count mismatch: {total_digits:,} (expected {EXPECTED_DIGITS:,})")
        verified = False
    
    if sha256_hash == EXPECTED_SHA256:
        print(f"✓ SHA-256 matches: {sha256_hash}")
    else:
        print(f"✗ SHA-256 mismatch!")
        print(f"  Got:      {sha256_hash}")
        print(f"  Expected: {EXPECTED_SHA256}")
        verified = False
    
    if head_60 == EXPECTED_HEAD_60:
        print(f"✓ First 60 digits match")
    else:
        print(f"✗ First 60 digits mismatch!")
        verified = False
    
    if tail_60 == EXPECTED_TAIL_60:
        print(f"✓ Last 60 digits match")
    else:
        print(f"✗ Last 60 digits mismatch!")
        verified = False
    
    print("=" * 70)
    if verified:
        print("🎉 VERIFICATION SUCCESSFUL!")
        print("You have independently verified the computation of Q₅₉(10^1886792 + 3)")
        print("\nThis confirms you are working with the exact same number documented in:")
        print("DOI: 10.5281/zenodo.18140813")
    else:
        print("⚠️  VERIFICATION FAILED!")
        print("The computed value does not match the expected fingerprint.")
        print("Please check your Python version and system configuration.")
    print("=" * 70)
    
    return verified


def save_certificate(value):
    """Save the identity certificate to a file."""
    value_str = str(value)
    sha256_hash = hashlib.sha256(value_str.encode('utf-8')).hexdigest().upper()
    
    certificate = f"""
==================================================
   Q₅₉ POLYNOMIAL IDENTITY CERTIFICATE
==================================================
Formula        : Q₅₉(10^{Q_EXPONENT} + {OFFSET})
Decimal Digits : {len(value_str):,}
SHA-256 Hash   : {sha256_hash}

[First 60 Digits]
{value_str[:60]}

[Last 60 Digits]
{value_str[-60:]}

Computation Date : {time.ctime()}
Verified Against : DOI 10.5281/zenodo.18140813
Status          : Computation Verified ✓
==================================================

This certificate confirms the independent verification of the
computation documented in:

Chen, R. (2026). Computation and Cryptographic Fingerprinting
of a 109-Million-Digit Integer in the Q₅₉ Polynomial Family.
Zenodo. https://doi.org/10.5281/zenodo.18140813

For primality verification status and collaboration opportunities:
https://github.com/Ruqing1963/q59-prime-candidate
==================================================
"""
    
    filename = "q59_verification_certificate.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(certificate)
    
    print(f"\n✓ Certificate saved to: {filename}")


def main():
    """Main execution function."""
    print("\n")
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║  Q₅₉ Polynomial Computation - 109-Million-Digit Prime Candidate   ║")
    print("║                                                                    ║")
    print("║  Author: Ruqing Chen                                              ║")
    print("║  DOI: 10.5281/zenodo.18140813                                     ║")
    print("║  License: CC-BY-4.0                                               ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    print("\n")
    
    # System check
    print("System Information:")
    print(f"  Python version: {sys.version}")
    print(f"  Platform: {sys.platform}")
    print(f"  Max string digits: {'UNLIMITED' if sys.get_int_max_str_digits() == 0 else sys.get_int_max_str_digits()}")
    print()
    
    # Warning
    print("⚠️  WARNING: This computation will take approximately 15-20 minutes")
    print("   and will consume ~200MB of RAM during string conversion.")
    print()
    
    response = input("Proceed with computation? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("Computation cancelled.")
        return
    
    print("\nStarting computation...\n")
    
    # Compute
    result, comp_time = compute_q59()
    
    # Analyze
    verified = analyze_result(result, comp_time)
    
    # Save certificate
    if verified:
        save_certificate(result)
    
    print("\nComputation complete!")
    print("\nFor more information:")
    print("  Paper: https://doi.org/10.5281/zenodo.18140813")
    print("  GitHub: https://github.com/Ruqing1963/q59-prime-candidate")
    print("  Contact: ruqing@hotmail.com")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nComputation interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ ERROR: {str(e)}")
        print("\nIf you encounter issues, please report them at:")
        print("https://github.com/Ruqing1963/q59-prime-candidate/issues")
        sys.exit(1)
