'''
Author: sunjie
Date: 2025-03-06 23:49:53
LastEditors: sunj
LastEditTime: 2025-03-07 00:25:06
FilePath: /sunjPy/luffyapi/luffyapi/utils/exceptions.py
'''
from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status

import logging

logger = logging.getLogger("django")


def custom_exception_handler(exec, context):
    """
    自定义异常处理
    :param exc :本次发生的异常
    :param context:异常发生的上下文
    """

    response = exception_handler(exc, context)
    if response is None:
        """ 要么程序出错了未识别,要么没有出现错误"""
        if isinstance(exc, DatabaseError):
            # 数据库异常
            logger.error("[%s] %s" % (view.exc))
            response = Response({"message": "数据库异常"},
                                status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response
