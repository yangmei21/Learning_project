import unittest
"""
    目标：unittest常用断言
        1.assertTure：如果结果为true通过，否则失败
"""

class Test02(unittest.TestCase):
    def test001(self):
        #flag=True
        #1----断言是否为True
        #self.assertTrue(flag)
        #self.assertFalse(flag)

        #2----判断两个字符串是否相等
        #self.assertEqual("你好，斑马！","你好，马！")
        #self.assertEqual("你好，斑马！", "你好，斑马！")

        # 3----判断后面字符串是否包含前面的字符串
        #self.assertIn("hello","hello,wuwu")
        #self.assertIn("hello,li", "hello,wuwu,li")  #该语句FALSE，因为不能跳过包含

        #判断是否为none
        flag=None
        #self.assertIsNone(flag)
        #self.assertIsNotNone(flag)
