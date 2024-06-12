import functools

from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response

# from django.db import connection, reset_queries
# import time
# import functools
# def query_debugger(func):
#     @functools.wraps(func)
#     def inner_func(*args, **kwargs):
#         reset_queries()
#         start_queries = len(connection.queries)
#
#         start = time.perf_counter()
#         func(*args, **kwargs)
#         end = time.perf_counter()
#
#         end_queries = len(connection.queries)
#         print(f'View (function name): {func.__name__}')
#         print(f'Queries quantity: {end_queries - start_queries}')
#         print(f'Execution time: {(end - start):.2f}s')
#
#     return inner_func
