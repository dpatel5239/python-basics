                       # precedence  and associativity of operators in python
# precedence determines the order in which operators are evaluated in an expression, operators with higher precedence are evaluated before operators with lower precedence
# associativity determines the order in which operators of the same precedence are evaluated, operators with left-to-right associativity are evaluated from left to right, while operators with right-to-left associativity are evaluated from right to left
# for example in the expression 3 + 4 * 5, the multiplication operator has higher precedence than the addition operator, so the multiplication is evaluated first, resulting in 3 + 20, which gives the final result of 23. In the expression 10 - 5 + 2, both the subtraction and addition operators have the same precedence, but they are evaluated from left to right due to their left-to-right associativity, resulting in (10 - 5) + 2, which gives the final result of 7.

# Operator Precedence and Associativity in Python (highest to lowest):

# 1. () (Parentheses), f(args) (function calls), [] (indexing), {} (dict/set literals) - Left-to-right
# 2. ** (Exponentiation) - Right-to-left
# 3. +x, -x, ~x (Unary plus, minus, bitwise NOT) - Right-to-left
# 4. *, /, //, % - Left-to-right
# 5. +, - (Addition, subtraction) - Left-to-right
# 6. <<, >> (Bitwise shifts) - Left-to-right
# 7. & (Bitwise AND) - Left-to-right
# 8. ^ (Bitwise XOR) - Left-to-right
# 9. | (Bitwise OR) - Left-to-right
# 10. Comparison: <, <=, >, >=, ==, !=, is, is not, in, not in - Left-to-right
# 11. not (Logical NOT) - Right-to-left
# 12. and (Logical AND) - Left-to-right
# 13. or (Logical OR) - Left-to-right
# 14. if ... else (Conditional expression) - Right-to-left
# 15. lambda - Left-to-right
# 16. = and assignment operators (+=, -=, *=, etc.) - Right-to-left
