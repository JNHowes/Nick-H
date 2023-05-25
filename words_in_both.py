# Author: Nick Howes
# GitHub username: JNHowes
# Date:May 24, 2023
# Description: a function named words_in_both that takes two strings as parameters and returns a Python set containing
# only those words that appear in both strings.

def words_in_both(string1, string2):
    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Split the strings into lists of words
    words1 = string1.split()
    words2 = string2.split()

    # Find the common words using set intersection
    common_words = set(words1) & set(words2)

    return common_words
