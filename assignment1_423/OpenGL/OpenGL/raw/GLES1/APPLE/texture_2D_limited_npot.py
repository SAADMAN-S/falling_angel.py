'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES1_APPLE_texture_2D_limited_npot'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES1,'GLES1_APPLE_texture_2D_limited_npot',error_checker=_errors._error_checker)


