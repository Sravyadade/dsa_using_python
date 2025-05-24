# Python implementation to find valid 
# word break using Recursion

def wordBreakHelper(s, dictSet, curr, res, start):
  
    # If start reaches the end of the string,
    # save the result
    if start == len(s):
        res.append(curr)
        return

    # Try every possible substring from the current index
    for end in range(start + 1, len(s) + 1):
        word = s[start:end]

        # Check if the word exists in the dictionary
        if word in dictSet:
            prev = curr

            # Append the word to the current sentence
            if curr:
                curr += " "
            curr += word

            # Recurse for the remaining string
            wordBreakHelper(s, dictSet, curr, res, end)

            # Backtrack to restore the current sentence
            curr = prev

def wordBreak(s, dict):
  
    # Convert dictionary list to a set
    dictSet = set(dict)

    res = []
    curr = ""

    wordBreakHelper(s, dictSet, curr, res, 0)

    return res


if __name__=='__main__':

    s = "ilikesamsungmobile"
    dict = ["i", "like", "sam", "sung",
                           "samsung", "mobile", "ice",
                            "and", "cream", "icecream",
                            "man", "go", "mango"]

    result = wordBreak(s, dict)

    for sentence in result:
        print(sentence)
