# Verification Guide

## How to Verify the Q₅₉ Computation

This guide explains how to independently verify that the documented 109-million-digit candidate is correctly computed.

---

## Quick Verification (5 minutes)

### Using the Provided Script

```bash
git clone https://github.com/Ruqing1963/q59-prime-candidate.git
cd q59-prime-candidate/scripts
python compute_q59.py
```

Follow the prompts. The script will:
1. Compute Q₅₉(10^1886792 + 3)
2. Calculate SHA-256 hash
3. Compare to expected fingerprint
4. Report verification status

**Expected result:**
```
✓ SHA-256 matches: A462032F37DC907EDEF64A575696EC0B11C052B42B469C76F6A6577B841864EF
🎉 VERIFICATION SUCCESSFUL!
```

---

## Manual Verification

### Step 1: Compute the Value

**Python**:
```python
import sys
sys.set_int_max_str_digits(0)

q = 10**1886792 + 3
result = q**59 - (q-1)**59
```

**Time required**: ~15-20 minutes on standard hardware

### Step 2: Convert to String

```python
result_str = str(result)
print(f"Digits: {len(result_str):,}")
```

**Expected**: 109,433,938 digits

### Step 3: Calculate SHA-256

```python
import hashlib
sha256 = hashlib.sha256(result_str.encode('utf-8')).hexdigest().upper()
print(f"SHA-256: {sha256}")
```

**Expected**:
```
A462032F37DC907EDEF64A575696EC0B11C052B42B469C76F6A6577B841864EF
```

### Step 4: Check Head and Tail

```python
print(f"First 60: {result_str[:60]}")
print(f"Last 60: {result_str[-60:]}")
```

**Expected**:
```
First 60: 590000000000000000000000000000000000000000000000000000000000
Last 60:  000000000000000000000000000000014130386091162273752461387579
```

---

## Verification in Other Languages

### Mathematica/Wolfram Language

```mathematica
q = 10^1886792 + 3;
result = q^59 - (q-1)^59;
IntegerLength[result]
(* Should output: 109433938 *)

resultString = ToString[result];
Hash[resultString, "SHA256", "HexString"]
(* Should match expected SHA-256 *)
```

### SageMath

```python
q = 10^1886792 + 3
result = q^59 - (q-1)^59
len(str(result))
# Should output: 109433938

import hashlib
hashlib.sha256(str(result).encode()).hexdigest().upper()
# Should match expected SHA-256
```

### GNU MP (GMP) in C

```c
#include <gmp.h>
#include <stdio.h>

int main() {
    mpz_t q, result, temp;
    mpz_init(q);
    mpz_init(result);
    mpz_init(temp);
    
    // q = 10^1886792 + 3
    mpz_ui_pow_ui(q, 10, 1886792);
    mpz_add_ui(q, q, 3);
    
    // result = q^59
    mpz_pow_ui(result, q, 59);
    
    // temp = (q-1)^59
    mpz_sub_ui(temp, q, 1);
    mpz_pow_ui(temp, temp, 59);
    
    // result = q^59 - (q-1)^59
    mpz_sub(result, result, temp);
    
    // Convert to string and hash
    char *str = mpz_get_str(NULL, 10, result);
    // Calculate SHA-256 of str
    // Compare to expected hash
    
    mpz_clear(q);
    mpz_clear(result);
    mpz_clear(temp);
    return 0;
}
```

---

## What Constitutes Successful Verification?

### Primary Success Criterion:

✅ **SHA-256 hash matches exactly**:
```
A462032F37DC907EDEF64A575696EC0B11C052B42B469C76F6A6577B841864EF
```

This proves you have computed the exact same integer.

### Secondary Checks (for quick validation):

✅ Digit count: 109,433,938  
✅ First 60 digits match  
✅ Last 60 digits match  

These provide sanity checks but SHA-256 is the definitive verification.

---

## Common Issues and Solutions

### Issue 1: Python String Conversion Limit

**Error**: `ValueError: Exceeds the limit (4300) for integer string conversion`

**Solution**:
```python
import sys
sys.set_int_max_str_digits(0)  # Must be at start of script
```

### Issue 2: Insufficient Memory

**Error**: `MemoryError` during string conversion

**Solution**:
- Ensure at least 4GB RAM available
- Close other applications
- Use 64-bit Python

### Issue 3: Computation Takes Too Long

**Expected time**: 15-20 minutes on modern hardware

**If much longer**:
- Check CPU is not throttled
- Ensure Python is not running in a VM with limited resources
- Verify using Python 3.11+ (earlier versions slower)

### Issue 4: SHA-256 Mismatch

**Possible causes**:
1. Incorrect parameters (check q_exponent, n, offset)
2. String conversion error (check for whitespace/formatting)
3. Calculation error (verify intermediate results)

**Debug steps**:
```python
# Verify parameters
print(f"q = 10^{1886792} + 3")
print(f"n = 59")

# Check intermediate values
q = 10**1886792 + 3
print(f"q has {len(str(q))} digits")  # Should be 1,886,793

# Verify q^59 and (q-1)^59 computed separately
q_power = q**59
q_minus_1_power = (q-1)**59
result = q_power - q_minus_1_power
```

---

## Partial Verification (Without Full Computation)

If you don't want to run the full computation, you can verify the fingerprint is consistent:

### Using the Quick Verification Tool:

```bash
python scripts/verify_fingerprint.py
```

Select option 2 for partial verification and enter:
- **Total digits**: 109,433,938
- **First 60 digits**: 590000000000000000000000000000000000000000000000000000000000
- **Last 60 digits**: 000000000000000000000000000000014130386091162273752461387579

This checks structural consistency without recomputing.

---

## Verification Checklist

Before reporting successful verification, confirm:

- [ ] Python 3.11+ used
- [ ] `sys.set_int_max_str_digits(0)` called
- [ ] Parameters: q = 10^1886792 + 3, n = 59
- [ ] Result has 109,433,938 digits
- [ ] SHA-256 matches exactly
- [ ] First 60 digits match
- [ ] Last 60 digits match
- [ ] No errors or warnings during computation

---

## Reporting Verification Results

### Successful Verification

If your verification succeeds, please consider:

1. **Star the repository** ⭐
2. **Open an issue** titled "Verification Successful" with:
   - Your Python version
   - Your hardware specs
   - Computation time
   - Any notable observations

3. **Share on social media** mentioning:
   - Repository: https://github.com/Ruqing1963/q59-prime-candidate
   - DOI: 10.5281/zenodo.18140813

### Failed Verification

If verification fails:

1. **Double-check** all steps above
2. **Try the provided script** instead of manual computation
3. **Open an issue** with:
   - Error messages
   - Your environment (Python version, OS, hardware)
   - Expected vs. actual results
   - Steps to reproduce

---

## Beyond Computation Verification

### Important Note:

Verifying the **computation** is correct does NOT verify that the number is **prime**.

**Computation verification** proves:
✅ The integer Q₅₉(10^1886792 + 3) was correctly calculated  
✅ The SHA-256 fingerprint is accurate  
✅ Everyone is testing the same candidate  

**Primality verification** (not yet done) would prove:
❌ Whether the number is actually prime  
❌ Requires months of computation  
❌ Needs supercomputer resources  

See [`COLLABORATION.md`](COLLABORATION.md) for information on primality testing efforts.

---

## Independent Verification Registry

We maintain a list of independent verifications. If you successfully verify:

**Email**: ruqing@hotmail.com  
**Subject**: "Q59 Independent Verification"  
**Include**:
- Your name/affiliation (optional)
- Verification method (script/manual/other)
- Date of verification
- Any observations

We'll add you to the acknowledgments (with permission).

---

## Questions?

- **GitHub Issues**: https://github.com/Ruqing1963/q59-prime-candidate/issues
- **Email**: ruqing@hotmail.com
- **Paper**: https://doi.org/10.5281/zenodo.18140813

---

**Last Updated**: January 3, 2026  
**Version**: 1.0.0
