import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        # Add special tokens with fixed IDs
        special_tokens = [
            self.pad_token,
            self.unk_token,
            self.bos_token,
            self.eos_token
        ]
        
        for idx, token in enumerate(special_tokens):
            self.word_to_id[token] = idx
            self.id_to_word[idx] = token
        
        # Collect unique words
        unique_words = set()
        
        for text in texts:
            words = text.lower().split()
            unique_words.update(words)
        
        # Add sorted words after special tokens
        start_idx = len(special_tokens)
        
        for idx, word in enumerate(sorted(unique_words), start=start_idx):
            self.word_to_id[word] = idx
            self.id_to_word[idx] = word
        
        # Set vocab size
        self.vocab_size = len(self.word_to_id)
        pass
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        words = text.lower().split()
        unk_id = self.word_to_id[self.unk_token]
        
        return [
            self.word_to_id.get(word, unk_id)
            for word in words
        ]
        pass
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        unk_token = self.unk_token
        
        words = [
            self.id_to_word.get(idx, unk_token)
            for idx in ids
        ]
        
        return " ".join(words)
        pass
