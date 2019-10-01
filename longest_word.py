import string
import re
def remove_punctuation(pattern, phrase):
    for pat in pattern:
        return (re.findall(pat, phrase))

pattern = ['[^!.?]+']
def find_longest_word(word_list):
    word_list = "".join(remove_punctuation(pattern, word_list))
    word_list.translate(string.punctuation)
    word_list = word_list.split()
    longest_word = max(word_list, key=len)
    print(longest_word)
    return longest_word

sen = "Hello guys my name is Bot. I'm a bot created by the amazing Junction!  team, and my job is to be your friend and bedazzle you!"
find_longest_word(sen)