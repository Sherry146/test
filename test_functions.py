import unittest
from main import *

class TestMyfuctions(unittest.TestCase):
    def setUp(self):
        self.min_value = 0
        self.max_value = 1
        
    def tearDown(self):
        del self.min_value
        del self.max_value
    
    def test_calculate_cosine_similarity(self):
        outcome = calculate_cosine_similarity("谢建豪","谢建豪")
        self.assertEqual(outcome, 1)
        outcome = calculate_cosine_similarity("谢建豪","谢老王")
        self.assertEqual(outcome,0)
        result = calculate_cosine_similarity("好好好","好好好好好好")
        self.assertTrue(self.min_value <= result <= self.max_value,
                        f"{result} is not within the range [{self.min_value}, {self.max_value}]")
        outcome = calculate_cosine_similarity("天气好好","我先去吃饭")
        self.assertEqual(outcome,0)
        outcome = calculate_cosine_similarity("软件测试","软件分析")
        self.assertEqual(outcome,0)
        outcome = calculate_cosine_similarity("你好","Hello")
        self.assertEqual(outcome,0)
        outcome = calculate_cosine_similarity("五年级","八年级")
        self.assertTrue(self.min_value <= result <= self.max_value,
                        f"{result} is not within the range [{self.min_value}, {self.max_value}]")
        outcome = calculate_cosine_similarity("你在哪里吃饭","你在哪里")
        self.assertTrue(self.min_value <= result <= self.max_value,
                        f"{result} is not within the range [{self.min_value}, {self.max_value}]")
        outcome = calculate_cosine_similarity("你生意还好吗","你好吗")
        self.assertTrue(self.min_value <= result <= self.max_value,
                        f"{result} is not within the range [{self.min_value}, {self.max_value}]")
        
if __name__ == "__main__":
    unittest.main()
        