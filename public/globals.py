#! -*- coding:utf-8 -*-
__version__ = '1.0.0.0'

import logging
import os
from robothub.adaptor.android.public import SetTestSuiteInformation
from robothub.common.logger import get_logger
logger = get_logger(__name__, level=logging.DEBUG)

# 全局参数
device = '172.17.197.35'
log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))+'/Log/'
log_level = logging.INFO
model = 5
result_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/image/result'
baseline_image_path =os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/image/baseline'
SetTestSuiteInformation("MdaTestSuite", "v1.0.0", "88888888")

filePath = "d:/upgrade"