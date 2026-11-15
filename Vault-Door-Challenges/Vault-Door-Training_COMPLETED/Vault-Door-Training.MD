# Vault-Door-Training — Reversing

> Flag: academy{w4rm1ng_Up_w1tH_jAv4_69bd4dc7adf}

### Details:

vault-door-training
Reverse EngineeringEasy
by Mark E. Haase·
picoCTF 2019

Read the source code of a training vault and find its password.

## 1. Analysis

The challenge provides the Java source file upfront, so no decompiler is needed. I read it with 'cat' and ran it with 'java'.

'main' asks for a password, and 'checkPassword' decides whether it is correct.

## 2. <Key function or step>

  1. Input Formatting:

  String input = userInput.substring("academy{".length(), userInput.length()-1);

  - Before the password checking function, the program manipulates the input string by removing the first 8 characters; specifically "academy{" and the last one "}".

  2. Password string

  return password.equals("w4rm1ng_Up_w1tH_jAv4_69bd4dc7adf");

  - The raw password is written upfront in the the bool for checkPassword.

## 3. Dynamic Analysis   (unnecessary for this challenge)

## 4. Script and Explanation
script:

#!/bin/bash

echo "academy{$(cat VaultDoorTraining.java | grep -oE 'w4[a-zA-Z0-9_]*')}"

- Although a script was unecessary to find the flag, I still wanted to practice woth scripts and the one above is what i researched online for the flag to be returned in the format its intended.


## 5. Learning
1. Hardcoded secrets in source code are the easiest bug to find.
2. Read the code around the check, not just the check. The 'substring' changed what I needed to enter.
