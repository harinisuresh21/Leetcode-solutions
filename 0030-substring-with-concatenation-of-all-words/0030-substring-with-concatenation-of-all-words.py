class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        target_counts = Counter(words)
        results = []
        
        # Run the sliding window for each possible offset
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            words_used = 0
            
            # Slide the 'right' pointer across the string in steps of word_len
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in target_counts:
                    current_counts[word] += 1
                    words_used += 1
                    
                    # If we have too many instances of this word, shrink from the left
                    while current_counts[word] > target_counts[word]:
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                    # If the window size matches the total length required
                    if words_used == word_count:
                        results.append(left)
                else:
                    # Found a word not in our list: clear and reset
                    current_counts.clear()
                    words_used = 0
                    left = right
                    
        return results