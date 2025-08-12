text = "hello chat gpt"

tokens = list(text)

print(tokens)

tokens = [char for char in text if char!= ' ']
print(tokens)


vocab = sorted(set(text))
char_to_id = {ch: idx for idx, ch in enumerate(vocab)}
id_to_char = {idx: ch for ch, idx in char_to_id.items()}

#encode
ids = [char_to_id[ch] for ch in text]
print("Token IDs: ", ids)

#decode
decoded = ''.join(id_to_char[i] for i in ids)
print("Decoded: ", decoded)

# Our text corpus
corpus = "hello hello chatter chat"

# Step 1: Start with characters + end symbol
words = [list(word) + ["</w>"] for word in corpus.split()]
words = [tuple(w) for w in words]

# Make a frequency dictionary of words
word_freq = {}
for w in words:
    word_freq[w] = word_freq.get(w, 0) + 1

def get_stats(word_freq):
    """Count frequency of each symbol pair without Counter"""
    pairs = {}
    for word, freq in word_freq.items():
        for i in range(len(word) - 1):
            pair = (word[i], word[i + 1])
            pairs[pair] = pairs.get(pair, 0) + freq
    return pairs

def merge_vocab(pair, word_freq):
    """Merge the most frequent pair"""
    new_word_freq = {}
    bigram = " ".join(pair)
    replacement = "".join(pair)
    for word, freq in word_freq.items():
        w = " ".join(word)
        w_new = w.replace(bigram, replacement)
        new_word_freq[tuple(w_new.split(" "))] = freq
    return new_word_freq

# Step 2: Run BPE merges
vocab_size_target = 15
while True:
    pairs = get_stats(word_freq)
    if not pairs:
        break
    # Pick the most common pair
    best_pair = max(pairs, key=pairs.get)
    word_freq = merge_vocab(best_pair, word_freq)
    print(f"Merged: {best_pair}")
    # Stop if vocab big enough
    symbols = set(sym for word in word_freq for sym in word)
    if len(symbols) >= vocab_size_target:
        break

print("\nFinal vocab:")
print(set(sym for word in word_freq for sym in word))
