# (){}
# ({})
# ({[]})

def check_parentheses_validity(s: str) -> bool:
    opening_parentheses_queue = []
    opening_parentheses_hash_map = {
        "{": "}",
        "(": ")",
        "[": "]",
    }

    closing_parentheses_hash_map = {
        "}": "{",
        ")": "(",
        "]": "["
     }
    for letter in s:
        if letter in opening_parentheses_hash_map:
            opening_parentheses_queue.append(letter)
        else:
            if opening_parentheses_queue:
                last_item = opening_parentheses_queue[len(opening_parentheses_queue) - 1]
                if last_item == closing_parentheses_hash_map[letter]:
                    opening_parentheses_queue.pop()
                else:
                    return False
            else:
                return False

    if not opening_parentheses_queue:
        return True
    else:
        return False


print(check_parentheses_validity("()"))
print(check_parentheses_validity(")()"))
print(check_parentheses_validity("(]"))
print(check_parentheses_validity("([)]"))
print(check_parentheses_validity("(])"))
print(check_parentheses_validity("]"))
