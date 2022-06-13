"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    longest_prefix = ""

    for counter, word in enumerate(strs):
        current_prefix = ""
        if not word:
            return ""
        if len(strs) == 1:
            return strs[0]
        if counter < len(strs) - 1:
            if strs[counter + 1] and word[0] == strs[counter + 1][0] and longest_prefix == "":
                if len(word) > len(strs[counter + 1]):
                    longest_word = word
                    shortest_word = strs[counter + 1]
                else:
                    longest_word = strs[counter + 1]
                    shortest_word = word
                for i in range(len(shortest_word)):
                    if shortest_word[i] == longest_word[i]:
                        current_prefix += shortest_word[i]
                    else:
                        break
                longest_prefix = current_prefix
            elif longest_prefix != "":
                if strs[counter + 1] and strs[counter + 1][0] != longest_prefix[0]:
                    return ""
                else:
                    if len(strs[counter + 1]) > len(longest_prefix):
                        longest_word = strs[counter + 1]
                        shortest_word = longest_prefix
                    else:
                        longest_word = longest_prefix
                        shortest_word = strs[counter + 1]
                    for i in range(len(shortest_word)):
                        if shortest_word[i] == longest_word[i]:
                            current_prefix += shortest_word[i]
                        else:
                            break
                    longest_prefix = current_prefix
            else:
                return ""

    return longest_prefix
                
print(longestCommonPrefix(["reflower","flow","flight"]))

