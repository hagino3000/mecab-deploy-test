# coding=utf-8
import unittest

import MeCab

from myapp import sample


class TestMyApp(unittest.TestCase):
    def test_get_tagger(self):
        self.assertIsInstance(sample.get_tagger(), MeCab.Tagger)

    def test_extract_words(self):
        ret = sample.extract_words(u'すもももももももものうち')
        self.assertEqual(ret, ['すもも', 'もも', 'もも', 'うち'])


if __name__ == '__main__':
    unittest.main()
