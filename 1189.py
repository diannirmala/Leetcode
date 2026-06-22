from collections import Counter

def maxNumberOfBalloons(text):
    c = Counter(text)

    return min(
        c['b'],
        c['a'],
        c['l'] // 2,
        c['o'] // 2,
        c['n']
    )

# Input from user
text = input("Enter a string: ")

# Call function and print result
result = maxNumberOfBalloons(text)
print("Maximum number of 'balloon':", result)

'''
test_cases = [
    "nlaebolko",
    "loonbalxballpoon",
    "leetcode"
]

for text in test_cases:
    print(f"Input: {text}")
    print("Output:", maxNumberOfBalloons(text))
    print()
'''