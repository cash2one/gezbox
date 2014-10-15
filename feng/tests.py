# encoding:utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


"""
由于时间紧张单元测试 就不写了。主要描述下思路和逻辑

1、首先写model 的单元测试
2、在写 各个form 的单元测试
3、在写handlers 的单元测试 可用TestCase类client 去模拟请求
"""
