# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: guess.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bguess.proto\x12\tguessgame\"\x1d\n\x0cGuessRequest\x12\r\n\x05guess\x18\x01 \x01(\x05\" \n\rGuessResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\x06Limits\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x32R\n\x0cGuessService\x12\x42\n\x0bguessNumber\x12\x17.guessgame.GuessRequest\x1a\x18.guessgame.GuessResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'guess_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GUESSREQUEST._serialized_start=26
  _GUESSREQUEST._serialized_end=55
  _GUESSRESPONSE._serialized_start=57
  _GUESSRESPONSE._serialized_end=89
  _LIMITS._serialized_start=91
  _LIMITS._serialized_end=121
  _GUESSSERVICE._serialized_start=123
  _GUESSSERVICE._serialized_end=205
# @@protoc_insertion_point(module_scope)
