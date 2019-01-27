
def Compareresult(filename):
    tokens = []
    date_l = []

    with open(filename,'r') as f:
        f.next()
        for line in f:
            tokens = line.rstrip('\n').split('\t')
            date_l.append((tokens[3]))

        return date_l



import unittest

class TestCountinTable(unittest.TestCase):
    """

    """
    def test_count(self):
        test_results = Compareresult('tableout.txt')
        self.assertEqual(int(test_results[0]), 0, " test case failed")
        self.assertEqual(int(test_results[1]), 0, " test case failed")
        self.assertEqual(int(test_results[2]), 0, " test case failed")



if __name__ == '__main__':
    unittest.main()