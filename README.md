# Simple Byte Pair Encoding (BPE) Tokenizer
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Python implementation of the Byte Pair Encoding (BPE) algorithm, demonstrating how subword vocabularies can be built from raw text.  

This project provides a minimal, readable reference for how BPE works under the hood.

---

## Features

- Encodes text at the character level  
- Builds a frequency-based vocabulary using BPE merges  
- Merges the most frequent symbol pairs iteratively  
- Displays intermediate merges and the final vocabulary  

---

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/<your-username>/simple-bpe.git
cd simple-bpe
python bpe.py
