def anagrams(st):
    if st == "":
        return [""]
    else:
        answer = []
        for word in anagrams(st[1:]):
            for pos in range(len(word) +1):
                new_word = word[:pos] + st[0] + word[pos:]
                if new_word not in answer:
                    answer.append(new_word)
        return answer
        
