#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "张开"
# Date: 2019/9/26



import subprocess
result = subprocess.Popen(r'python M:\demo\AT2\testsss.py', shell=True, stdout=subprocess.PIPE)
print(111, result.stdout.read())
print(result.stderr)