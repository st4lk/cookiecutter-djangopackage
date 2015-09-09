# -*- coding: utf-8 -*-


def pytest_runtest_setup(item):
    from django.db import connections, DEFAULT_DB_ALIAS
    connections[DEFAULT_DB_ALIAS].use_debug_cursor = True
