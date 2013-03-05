#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011-2013 by Łukasz Langa

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import os
import unittest

import six

from null import Null, NullDict, NullList, nullify
from oa import e


class TestNull(unittest.TestCase):
    def setUp(self):
        pass

    def data(self, name):
        directory = os.path.split(__file__)[0]
        return os.path.join(directory, name)

    def test_simple(self):
        self.assertIs(Null, Null)
        self.assertEqual(Null, Null)
        self.assertEqual(six.text_type(Null), "")
        self.assertEqual(six.binary_type(Null), b"")
        self.assertEqual(repr(Null), "Null")
        self.assertFalse(Null)
        self.assertEqual(len(Null), 0)
        self.assertIs(Null.any_attribute, Null)
        Null.other_attribute = "ping"
        self.assertIs(Null.other_attribute, Null)
        self.assertIs(Null["item!"], Null)
        Null["other"] = "ping"
        self.assertIs(Null["other"], Null)
        del Null["other"]
        self.assertIs(Null["other"], Null)
        self.assertIs(Null(), Null)
        self.assertIs(Null("argument"), Null)
        self.assertIs(Null("argument", kwarg="argument"), Null)
        with self.assertRaises(StopIteration):
            Null.next()
        for i in Null:
            self.fail()

    def test_nulldict(self):
        d = NullDict()
        d['exists'] = True
        self.assertTrue(d['exists'])
        self.assertFalse(d['does not exist'])
        self.assertIs(d['does not exist'], Null)
        del d['exists']
        self.assertFalse(d['exists'])
        self.assertIs(d['exists'], Null)

    def test_nulllist(self):
        l = NullList([1, 2, 3, 4])
        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)
        self.assertEqual(l[2], 3)
        self.assertEqual(l[3], 4)
        self.assertIs(l[4], Null)
        self.assertEqual(l[-1], 4)
        l.append(5)
        self.assertEqual(l[4], 5)
        self.assertIs(l[5], Null)
        self.assertEqual(l[-1], 5)
        l.pop()
        self.assertIs(l[4], Null)
        self.assertEqual(l[-1], 4)

    def test_nullify(self):
        with open(self.data("reddit.json")) as f:
            j = json.load(f)
        self.assertTrue(isinstance(j, dict))
        self.assertFalse(isinstance(j, NullDict))
        self.assertTrue(isinstance(j['data']['children'], list))
        self.assertFalse(isinstance(j['data']['children'], NullList))
        self.assertEqual(
            j['data']['children'][24]['data']['url'],
            'http://technicaldiscovery.blogspot.com/2011/06/speeding-up-python'
            '-numpy-cython-and.html',
        )
        with self.assertRaises(IndexError):
            j['data']['children'][25]
        with self.assertRaises(KeyError):
            j['data']['parents']
        k = nullify(j)
        self.assertTrue(isinstance(k, dict))
        self.assertTrue(isinstance(k, NullDict))
        self.assertTrue(isinstance(k['data']['children'], list))
        self.assertTrue(isinstance(k['data']['children'], NullList))
        self.assertEqual(
            k['data']['children'][24]['data']['url'],
            'http://technicaldiscovery.blogspot.com/2011/06/speeding-up-python'
            '-numpy-cython-and.html',
        )
        self.assertIs(k['data']['children'][25], Null)
        self.assertIs(k['data']['parents'], Null)

    def test_configparser(self):
        try:
            import configparser
        except ImportError:
            self.skipTest("configparser not installed.")
        p = configparser.ConfigParser()
        with open(self.data("idle_config.ini")) as f:
            p.read_file(f)
        p = nullify(p)
        self.assertIn('EditorWindow', p)
        self.assertIn('FormatParagraph', p)
        self.assertIn('General', p)
        self.assertIn('HelpFiles', p)
        self.assertIn('History', p)
        self.assertIn('Indent', p)
        self.assertIn('Keys', p)
        self.assertIn('Theme', p)
        self.assertIn('default', p['Theme'])
        self.assertIn('name', p['Theme'])
        self.assertNotIn('DoesNotExist', p)
        self.assertNotIn('DoesNotExist', p['Theme'])
        self.assertIs(p['DoesNotExist'], Null)
        self.assertIs(p['DoesNotExist']['DoesNotExist'], Null)
        self.assertNotIn('DoesNotExist', p['DoesNotExist'])

    def test_xml(self):
        f = nullify(e)
        self.assertEqual(e[1]['INFRA2']['MANAGERS']['MANAGER'][0]['POWER']
                         ['POWERSTATE'], 'ON')
        with self.assertRaises(IndexError):
            e[1]['INFRA2']['MANAGERS']['MANAGER'][10]['POWER']['POWERSTATE']
        with self.assertRaises(KeyError):
            e[1]['INFRA2']['MANAGERS']['MANAGER'][0]['POWER']['LEVEL']
        self.assertEqual(f[1]['INFRA2']['MANAGERS']['MANAGER'][0]['POWER']
                         ['POWERSTATE'], 'ON')
        self.assertIs(f[1]['INFRA2']['MANAGERS']['MANAGER'][10]['POWER']
                      ['POWERSTATE'], Null)
        self.assertIs(f[1]['INFRA2']['MANAGERS']['MANAGER'][0]['POWER']
                      ['LEVEL'], Null)


if __name__ == '__main__':
    unittest.main()
