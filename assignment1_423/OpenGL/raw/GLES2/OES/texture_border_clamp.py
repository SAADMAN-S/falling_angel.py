'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_OES_texture_border_clamp'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_OES_texture_border_clamp',error_checker=_errors._error_checker)
GL_CLAMP_TO_BORDER_OES=_C('GL_CLAMP_TO_BORDER_OES',0x812D)
GL_TEXTURE_BORDER_COLOR_OES=_C('GL_TEXTURE_BORDER_COLOR_OES',0x1004)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetSamplerParameterIivOES(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetSamplerParameterIuivOES(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexParameterIivOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glGetTexParameterIuivOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glSamplerParameterIivOES(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glSamplerParameterIuivOES(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexParameterIivOES(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glTexParameterIuivOES(target,pname,params):pass