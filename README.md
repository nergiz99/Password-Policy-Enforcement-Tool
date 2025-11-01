# 🔐 Enterprise Password Policy Enforcement Tool (Python)

## 🚀 Introduction and Goal

The **Enterprise Password Policy Enforcement Tool** is a Python-based security application designed to **enforce mandatory compliance** with strict enterprise password security policies. The primary goal is to **eliminate the risk of employees choosing weak passwords** by implementing rigorous policy enforcement and providing an automated solution for password generation.

### Key Objectives:
- **✅ Mandatory Enforcement**: Directly refuse passwords that fail ANY policy requirement
- **🔒 Zero Tolerance**: No exceptions for weak passwords, common passwords, or passwords missing mandatory character types
- **⚡ Automated Solution**: Provide a Secure Password Generator that guarantees policy compliance
- **🛡️ Enterprise Security**: Ensure all passwords meet or exceed organizational security standards

This tool transforms password policy from a guideline into a **hard enforcement mechanism**, ensuring that only compliant passwords can be accepted by the system.

---

## 🛠️ Core Functionalities

| Option | Module Name | Description |
|--------|-------------|-------------|
| **1** | **Password Policy Enforcement** | **ENFORCES**: Directly checks the password against **ALL criteria**:<br>• **Entropy ≥ 40 bits** (minimum security threshold)<br>• **Must contain Uppercase letter** (mandatory)<br>• **Must contain Number (Digit)** (mandatory)<br>• **Must contain Special Character** (mandatory)<br>• **NOT found in common passwords list** (blacklist check)<br><br>**Result**: If **ANY single rule is violated**, the password is **REFUSED** with a clear policy violation message, and the user is directed to Option 2 for an automated solution. |
| **2** | **Secure Password Generator (CTF Solution)** | **SOLUTION**: This is the direct solution to the problem of non-compliant user choices. It generates a random, unique password that is **guaranteed to meet all policy requirements**:<br>• Minimum 10+ characters (typically 12-16 characters)<br>• Contains uppercase letters<br>• Contains digits<br>• Contains special characters<br>• High entropy (≥40 bits)<br>• Not found in common password lists<br><br>**Purpose**: Automatically and forcefully removes compliance risk by providing a guaranteed secure password that requires zero user decision-making. |

---

## 🎯 CTF Solution Justification

### The CTF Problem: User Non-Compliance

The fundamental security challenge addressed by this tool is **user non-compliance with password policies**. Even when organizations establish clear password requirements, employees may:

- Choose passwords that appear strong but fail specific requirements (e.g., `nergiznergiz` has high entropy but lacks mandatory characters)
- Select common or predictable passwords despite warnings
- Create passwords that meet some requirements but fail others
- Attempt to circumvent policy guidelines through minimal compliance

### The CTF Solution: Secure Password Generator (Option 2)

The **Secure Password Generator** (Option 2) is the **direct solution** to the CTF problem of user non-compliance. Here's why:

1. **Eliminates User Decision-Making**: By automatically generating passwords, it removes the risk of users making poor choices
2. **Guaranteed Compliance**: Every generated password is mathematically guaranteed to pass all policy checks enforced in Option 1
3. **Removes Human Error**: No possibility of missing required character types or using common passwords
4. **Immediate Resolution**: When Option 1 refuses a password, Option 2 provides an instant, compliant alternative

**The CTF Solution directly addresses the root cause**: Instead of relying on users to create compliant passwords (which Option 1 validates), Option 2 removes the problem entirely by generating passwords that cannot fail.

---

## ⚙️ Setup and Usage

### Prerequisites

- **Python 3.x** (Python 3.6 or higher recommended)
- **Standard Library Modules**: `getpass`, `math`, `string`, `random` (all included with Python)

> **Note**: All required libraries are part of Python's standard library and do not require separate installation.

### Installation

No additional packages are required. All dependencies are part of Python's standard library.

```bash
# Verify Python installation
python --version

# If needed, verify standard library modules are accessible
python -c "import getpass, math, string, random; print('All modules available')"
```

### Running the Tool

```bash
python PasswordStrengthChecker.py
```

### Menu Options

Upon running the tool, you will be presented with the following menu:

| Option | Function |
|--------|----------|
| **1. Check password strength** | **Password Policy Enforcement**: Securely prompts for a password (characters are hidden using `getpass`) and enforces ALL policy requirements. If the password fails ANY check, it is refused with detailed violation reasons. |
| **2. Secure Password Generator** | **CTF Solution**: Automatically generates a secure password that is guaranteed to pass all policy requirements enforced in Option 1. Displays the generated password with full compliance verification. |
| **3. Exit** | Terminates the application |

### Usage Workflow

1. **User attempts to set a password** → Selects Option 1
2. **Password is checked** → All policy requirements are validated
3. **If password fails** → Policy violation is displayed, user is directed to Option 2
4. **User selects Option 2** → Secure password is automatically generated
5. **Generated password is guaranteed compliant** → Can be immediately used

---

## 📋 Policy Requirements

The Enterprise Password Policy enforced by this tool requires **ALL** of the following criteria to be met:

| Requirement | Minimum Standard | Enforcement |
|------------|------------------|-------------|
| **Entropy** | ≥ 40 bits | Measured using Shannon Entropy calculation |
| **Uppercase Letter** | At least 1 | Mandatory character type check |
| **Number (Digit)** | At least 1 | Mandatory character type check |
| **Special Character** | At least 1 | Mandatory character type check |
| **Common Password Check** | Not in blacklist | Checks against `common_passwords.txt` |
| **Length** | Variable (10+ recommended) | Length affects entropy calculation |

**⚠️ Important**: If **ANY single requirement** fails, the password is **REFUSED** and cannot be set.

---

## 🔬 Technical Details

### Shannon Entropy Calculation

The tool calculates entropy using the formula:

$$H = L \times \log_2(N)$$

Where:
- **L** = Password length
- **N** = Character space size (sum of present character categories)
  - Lowercase letters: 26
  - Uppercase letters: 26
  - Digits: 0-9: 10
  - Special symbols: ~32

**Strength Thresholds:**
- **Policy Minimum**: ≥ 40 bits (required to pass)
- **Strong**: > 60 bits (exceeds minimum)

### Password Generation Algorithm

The Secure Password Generator (Option 2) uses a deterministic algorithm that guarantees compliance:

1. **Required Character Injection**: Ensures at least one uppercase, digit, and special character
2. **Random Character Fill**: Adds random characters from all character sets to reach minimum length
3. **Extended Length**: Generates 12-16 characters for enhanced security
4. **Character Shuffling**: Randomizes character positions to prevent predictable patterns
5. **Compliance Verification**: Validates generated password against all policy requirements

---

## 💡 Why This Approach Works

### Problem-Solution Architecture

1. **Option 1 (Enforcement)** identifies the problem: Non-compliant passwords
2. **Option 2 (Generator)** provides the solution: Guaranteed compliant passwords
3. **Together**, they form a complete system that both prevents weak passwords and provides an instant remedy

### Enterprise Benefits

- **Zero User Error**: Eliminates possibility of employees accidentally choosing weak passwords
- **Policy Compliance**: Ensures 100% adherence to organizational security standards
- **Reduced IT Support**: Fewer password-related security incidents and reset requests
- **Immediate Resolution**: When a password fails, a compliant alternative is instantly available
- **Educational Value**: Clear violation messages help users understand policy requirements

---

## 📁 File Structure

```
Project of Nargiz Jafarova/
├── PasswordStrengthChecker.py    # Main application file
├── common_passwords.txt          # Curated list of common weak passwords (blacklist)
└── README.md                     # This documentation file
```

---

## ⚠️ Security Disclaimer

This tool is designed for **enterprise password policy enforcement** within authorized organizational environments. Users should:

- Only use this tool in authorized enterprise environments
- Respect organizational security policies and guidelines
- Understand that the Secure Password Generator provides cryptographically random passwords suitable for production use
- Store generated passwords securely using a password manager

---

## 📝 License

This project is created for educational and enterprise security enforcement purposes.

---

**Built with 🔒 Security Enforcement and 🎯 Compliance in Mind**
