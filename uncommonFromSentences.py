class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
		# this runs way faster than 69.39%
        return max(sentence.count(' ') + 1 for sentence in sentences)
        
        # ITERATIVE APPROACH:
        maxW = 0
        for sentence in sentences:
            sentence = sentence.split()
            if len(sentence) > maxW:
                maxW = len(sentence)
        return maxW		