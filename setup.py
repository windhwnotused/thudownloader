#!/usr/bin/env python
# -*- coding: gbk -*-

from distutils.core import setup
import py2exe

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "0.5.0",
    description = u"����ѧ������",
    name = "MyDownloader",
    windows = [{"script":"MyDownloader.py","icon_resources": [(1, "MyDownloader.ico")]}])
    
