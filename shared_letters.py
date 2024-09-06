

# * Letters Shared Between Two Words
# todo Create a function that returns the number of characters shared between two words.

# ? Examples
# ? shared_letters("apple", "meaty") ➞ 2
# ? # Since "ea" is shared between "apple" and "meaty".

# ? shared_letters("fan", "forsook") ➞ 1

# ? shared_letters("spout", "shout") ➞ 4
# ! Notes
# N/A



#  ! //////////////////////////////////////////////////////////////////

def shared_letters(test_str1, test_str2):
    res = ""
    for i in test_str1:
        if i in test_str2 and not i in res:
            res += i
    return len(res)

print(shared_letters("apple", "meaty"))

#  * //////////////////////////////////////////////////////////////////

# ? there are a couple of small optimizations and improvements :

# ? Use a set for the result: Sets are automatically unique and would remove the need to manually check if a character is already in res.

def shared_letters(test_str1, test_str2):
    res = set()  # Use a set to automatically handle uniqueness
    for i in test_str1:
        if i in test_str2:  # Check if character exists in second string
            res.add(i)  # Add to set (automatically handles duplicates)
    return len(res)  # Return the length of the set

# Test cases
print(shared_letters("apple", "meaty"))  # ➞ 2
print(shared_letters("fan", "forsook"))  # ➞ 1
print(shared_letters("spout", "shout"))  # ➞ 4


#  ! //////////////////////////////////////////////////////////////////


def shared_letters(word1, word2):
    # Convert both words to sets
    set1 = set(word1)
    set2 = set(word2)
    
    # Find the intersection (shared letters)
    shared = set1 & set2
    
    # Return the number of shared letters
    return len(shared)

# Test cases
print(shared_letters("apple", "meaty"))  # ➞ 2
print(shared_letters("fan", "forsook"))  # ➞ 1
print(shared_letters("spout", "shout"))  # ➞ 4




# * Convert to sets: We convert both word1 and word2 to sets, which automatically handles repeated characters and makes comparisons easy.

# ? For example, set("apple") becomes {'a', 'e', 'l', 'p'} and set("meaty") becomes {'m', 'a', 't', 'e', 'y'}.


# * Intersection: The & operator finds the intersection of two sets, which are the characters that exist in both sets.

# ? The intersection of {'a', 'e', 'l', 'p'} and {'m', 'a', 't', 'e', 'y'} is {'a', 'e'}.


# * Return the length: We then return the number of elements in the intersection set using len().