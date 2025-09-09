def isBalanced(s: str) -> str:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            
            stack.append(char)
        elif char in bracket_map:
            
            if not stack or stack[-1] != bracket_map[char]:
                return "NO"
            stack.pop()
        else:
            
            return "NO"
    
    return "YES" if not stack else "NO"


n = (input("Please Enter the Input: "))
print(f"{n} ->{isBalanced(n)}")
print("\n")

print("Test CasesS")
test_cases = [
    "{[()]}",   
    "{[(])}",   
    "{{[[(())]]}}",  
    "((())",   
]
for s in test_cases:
    print(f"{s} -> {isBalanced(s)}")
