def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    count = 0
    allowed = set(allowed)
    for word in words:
        word = set(word)
        if len(word.difference(allowed)) > 0:
            count += 1
    return len(words) - count