# Is Unique: Implement an algorithm to determine if a string has all unique characters.  What if you cannot use additional data structures?

import unittest

def is_unique(the_string):

    i = 0
    k = 1

    while i < len(the_string) - 1:
        if the_string[i] == the_string[k]:
            return False #not unique
        else:
            k += 1

        if k > len(the_string) - 1:
            i += 1
            k = i + 1

    return True

class Test(unittest.TestCase):

    true_strings = ["helo wrd", "1234", "&^#!@32", "1", ""]
    false_strings = ["hello world", "12341", "&$@#@&", "11", "  "]

    def test_is_unique(self):
        for t_string in self.true_strings:
            self.assertTrue(is_unique(t_string), t_string)

        for f_string in self.false_strings:
            self.assertFalse(is_unique(f_string), f_string)

if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()