def loves_me(n):
    phrases = ["Loves me", "Loves me not"]
    result = []
    for i in range(n):
        phrase = phrases[i % 2]
        if i == n:
            phrase = phrase.lower()
        result.append(phrase)
    return "; ".join(result)