#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :__init__.py.py
# @Time      :2026/5/19 09:58:22
# @Author    :雨霓同学
# @Project   :ODPlatform
# @Function  :
"""
ODPlatform - 通用的目标检测开发平台

Public API入口，具体的子模块
- odp_paltform.common : 基础工具(路径、日志，字符串，系统，性能)
- odp_platfoprm.cli ： 命令行入口
"""
from odp_platform._version import __version__

__all__ = ["__version__"]


