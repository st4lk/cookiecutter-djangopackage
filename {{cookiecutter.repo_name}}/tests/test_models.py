#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `{{ cookiecutter.app_name }}` models module.
"""

from django.test import TestCase
from model_mommy import mommy

from {{ cookiecutter.app_name }} import models


class Test{{ cookiecutter.app_name|capitalize }}(TestCase):

    def setUp(self):
        super(Test{{ cookiecutter.app_name|capitalize }}, self).setUp()

    def test_something(self):
        pass

    def tearDown(self):
        super(Test{{ cookiecutter.app_name|capitalize }}, self).tearDown()
