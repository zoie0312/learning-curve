# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    reverse_str = ''
    if len(aStr) < 2:
        return aStr
    else:
        reverse_str = aStr[len(aStr)-1] + reverseString(aStr[:-1])
    return reverse_str

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO.
    #result = True
    if len(x) > len(word):
        return False
    elif len(x) == 0:
        return True
    elif x[0] not in word:
        return False
    else:
  #      temp = word.split(x[0])
  #      print(temp)
  #      print(x[1:])
        ind = word.find(x[0])  
        return x_ian(x[1:], word[ind+1:]) 
 #   return result

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
    if len(text) < lineLength:
        return text
    else:
        if text[lineLength-1] == ' ':
            temp_str = text[:lineLength] + '\n'
            return temp_str + insertNewlines(text[lineLength:], lineLength)
        else:
            temp_str1 = text[:lineLength]
            temp_str2 = text[lineLength:]
            space_ind = temp_str2.find(' ')
            temp_str3 = temp_str2[:space_ind]
            temp_str = temp_str1 + temp_str3 + '\n'
            return temp_str + insertNewlines(temp_str2[space_ind+1:], lineLength)
        
