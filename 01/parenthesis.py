# Input: s = "[{()}]"
# Output: true
# Explanation: All the brackets are well-formed.

# Input: s = "[()()]{}"
# Output: true
# Explanation: All the brackets are well-formed.

# Input: s = "([]"
# Output: False
# Explanation: The expression is not balanced as there is a missing ')' at the end.

# Input: s = "([{]})"
# Output: False
# Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.

from collections import deque

input_rule ={'}':'{',']':'[',')':'('}
def is_valid(s: str) -> bool:
    pass