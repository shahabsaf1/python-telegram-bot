# -*- coding: utf-8 -*-
import telebot
import simplejson as json
import requests
import time
import os
import magic
import tempfile
from telebot import types
import traceback
import urllib
import re
import sys
import mimetypes
import importlib


#https://github.com/luksireiku/polaris/blob/master/utils.py
def fix_extension(file_path):
    type = magic.from_file(file_path, mime=True).decode("utf-8")
    extension = str(mimetypes.guess_extension(type, strict=False))
    if extension is not None:
        # I hate to have to use this s***, f*** jpe
        if '.jpe' in extension:
            extension = extension.replace('jpe', 'jpg')
        os.rename(file_path, file_path + extension)
        return file_path + extension
    else:
        return file_path

#https://github.com/luksireiku/polaris/blob/master/utils.py
def download(url, params=None, headers=None):
    try:
        jstr = requests.get(url, params=params, headers=headers, stream=True)
        ext = os.path.splitext(url)[1]
        f = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
        for chunk in jstr.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    except IOError as e:
        return None
    f.seek(0)
    if not ext:
        f.name = fix_extension(f.name)
    file = open(f.name, 'rb')
    return file