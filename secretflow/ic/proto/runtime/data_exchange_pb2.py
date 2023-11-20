# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: secretflow/ic/proto/runtime/data_exchange.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='secretflow/ic/proto/runtime/data_exchange.proto',
  package='org.interconnection.v2.runtime',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/secretflow/ic/proto/runtime/data_exchange.proto\x12\x1eorg.interconnection.v2.runtime\"\xa6\x04\n\x14\x44\x61taExchangeProtocol\x12\x13\n\x0bscalar_type\x18\x01 \x01(\x05\x12\x18\n\x10scalar_type_name\x18\x02 \x01(\t\x12\x38\n\x06scalar\x18\x05 \x01(\x0b\x32&.org.interconnection.v2.runtime.ScalarH\x00\x12\x44\n\rf_scalar_list\x18\x06 \x01(\x0b\x32+.org.interconnection.v2.runtime.FScalarListH\x00\x12\x44\n\rv_scalar_list\x18\x07 \x01(\x0b\x32+.org.interconnection.v2.runtime.VScalarListH\x00\x12=\n\tf_ndarray\x18\x08 \x01(\x0b\x32(.org.interconnection.v2.runtime.FNdArrayH\x00\x12=\n\tv_ndarray\x18\t \x01(\x0b\x32(.org.interconnection.v2.runtime.VNdArrayH\x00\x12\x46\n\x0e\x66_ndarray_list\x18\n \x01(\x0b\x32,.org.interconnection.v2.runtime.FNdArrayListH\x00\x12\x46\n\x0ev_ndarray_list\x18\x0b \x01(\x0b\x32,.org.interconnection.v2.runtime.VNdArrayListH\x00\x42\x0b\n\tcontainer\"\x15\n\x06Scalar\x12\x0b\n\x03\x62uf\x18\x01 \x01(\x0c\"3\n\x0b\x46ScalarList\x12\x12\n\nitem_count\x18\x01 \x01(\x03\x12\x10\n\x08item_buf\x18\x02 \x01(\x0c\"\x1c\n\x0bVScalarList\x12\r\n\x05items\x18\x01 \x03(\x0c\"+\n\x08\x46NdArray\x12\r\n\x05shape\x18\x01 \x03(\x03\x12\x10\n\x08item_buf\x18\x02 \x01(\x0c\"(\n\x08VNdArray\x12\r\n\x05shape\x18\x01 \x03(\x03\x12\r\n\x05items\x18\x02 \x03(\x0c\"J\n\x0c\x46NdArrayList\x12:\n\x08ndarrays\x18\x01 \x03(\x0b\x32(.org.interconnection.v2.runtime.FNdArray\"J\n\x0cVNdArrayList\x12:\n\x08ndarrays\x18\x01 \x03(\x0b\x32(.org.interconnection.v2.runtime.VNdArray*\x8d\x03\n\nScalarType\x12\x1b\n\x17SCALAR_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10SCALAR_TYPE_BOOL\x10\x01\x12\x14\n\x10SCALAR_TYPE_INT8\x10\x02\x12\x15\n\x11SCALAR_TYPE_UINT8\x10\x03\x12\x15\n\x11SCALAR_TYPE_INT16\x10\x04\x12\x16\n\x12SCALAR_TYPE_UINT16\x10\x05\x12\x15\n\x11SCALAR_TYPE_INT32\x10\x06\x12\x16\n\x12SCALAR_TYPE_UINT32\x10\x07\x12\x15\n\x11SCALAR_TYPE_INT64\x10\x08\x12\x16\n\x12SCALAR_TYPE_UINT64\x10\t\x12\x16\n\x12SCALAR_TYPE_INT128\x10\n\x12\x17\n\x13SCALAR_TYPE_UINT128\x10\x0b\x12\x17\n\x13SCALAR_TYPE_FLOAT16\x10\x0f\x12\x17\n\x13SCALAR_TYPE_FLOAT32\x10\x10\x12\x17\n\x13SCALAR_TYPE_FLOAT64\x10\x11\x12\x16\n\x12SCALAR_TYPE_OBJECT\x10\x14\x62\x06proto3'
)

_SCALARTYPE = _descriptor.EnumDescriptor(
  name='ScalarType',
  full_name='org.interconnection.v2.runtime.ScalarType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_BOOL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_INT8', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_UINT8', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_INT16', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_UINT16', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_INT32', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_UINT32', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_INT64', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_UINT64', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_INT128', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_UINT128', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_FLOAT16', index=12, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_FLOAT32', index=13, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_FLOAT64', index=14, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALAR_TYPE_OBJECT', index=15, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=982,
  serialized_end=1379,
)
_sym_db.RegisterEnumDescriptor(_SCALARTYPE)

ScalarType = enum_type_wrapper.EnumTypeWrapper(_SCALARTYPE)
SCALAR_TYPE_UNSPECIFIED = 0
SCALAR_TYPE_BOOL = 1
SCALAR_TYPE_INT8 = 2
SCALAR_TYPE_UINT8 = 3
SCALAR_TYPE_INT16 = 4
SCALAR_TYPE_UINT16 = 5
SCALAR_TYPE_INT32 = 6
SCALAR_TYPE_UINT32 = 7
SCALAR_TYPE_INT64 = 8
SCALAR_TYPE_UINT64 = 9
SCALAR_TYPE_INT128 = 10
SCALAR_TYPE_UINT128 = 11
SCALAR_TYPE_FLOAT16 = 15
SCALAR_TYPE_FLOAT32 = 16
SCALAR_TYPE_FLOAT64 = 17
SCALAR_TYPE_OBJECT = 20



_DATAEXCHANGEPROTOCOL = _descriptor.Descriptor(
  name='DataExchangeProtocol',
  full_name='org.interconnection.v2.runtime.DataExchangeProtocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scalar_type', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.scalar_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scalar_type_name', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.scalar_type_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scalar', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.scalar', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f_scalar_list', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.f_scalar_list', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v_scalar_list', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.v_scalar_list', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f_ndarray', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.f_ndarray', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v_ndarray', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.v_ndarray', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f_ndarray_list', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.f_ndarray_list', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='v_ndarray_list', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.v_ndarray_list', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='container', full_name='org.interconnection.v2.runtime.DataExchangeProtocol.container',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=84,
  serialized_end=634,
)


_SCALAR = _descriptor.Descriptor(
  name='Scalar',
  full_name='org.interconnection.v2.runtime.Scalar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buf', full_name='org.interconnection.v2.runtime.Scalar.buf', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=657,
)


_FSCALARLIST = _descriptor.Descriptor(
  name='FScalarList',
  full_name='org.interconnection.v2.runtime.FScalarList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_count', full_name='org.interconnection.v2.runtime.FScalarList.item_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_buf', full_name='org.interconnection.v2.runtime.FScalarList.item_buf', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=659,
  serialized_end=710,
)


_VSCALARLIST = _descriptor.Descriptor(
  name='VScalarList',
  full_name='org.interconnection.v2.runtime.VScalarList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='org.interconnection.v2.runtime.VScalarList.items', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=712,
  serialized_end=740,
)


_FNDARRAY = _descriptor.Descriptor(
  name='FNdArray',
  full_name='org.interconnection.v2.runtime.FNdArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='org.interconnection.v2.runtime.FNdArray.shape', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_buf', full_name='org.interconnection.v2.runtime.FNdArray.item_buf', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=742,
  serialized_end=785,
)


_VNDARRAY = _descriptor.Descriptor(
  name='VNdArray',
  full_name='org.interconnection.v2.runtime.VNdArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='org.interconnection.v2.runtime.VNdArray.shape', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='org.interconnection.v2.runtime.VNdArray.items', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=787,
  serialized_end=827,
)


_FNDARRAYLIST = _descriptor.Descriptor(
  name='FNdArrayList',
  full_name='org.interconnection.v2.runtime.FNdArrayList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ndarrays', full_name='org.interconnection.v2.runtime.FNdArrayList.ndarrays', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=829,
  serialized_end=903,
)


_VNDARRAYLIST = _descriptor.Descriptor(
  name='VNdArrayList',
  full_name='org.interconnection.v2.runtime.VNdArrayList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ndarrays', full_name='org.interconnection.v2.runtime.VNdArrayList.ndarrays', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=905,
  serialized_end=979,
)

_DATAEXCHANGEPROTOCOL.fields_by_name['scalar'].message_type = _SCALAR
_DATAEXCHANGEPROTOCOL.fields_by_name['f_scalar_list'].message_type = _FSCALARLIST
_DATAEXCHANGEPROTOCOL.fields_by_name['v_scalar_list'].message_type = _VSCALARLIST
_DATAEXCHANGEPROTOCOL.fields_by_name['f_ndarray'].message_type = _FNDARRAY
_DATAEXCHANGEPROTOCOL.fields_by_name['v_ndarray'].message_type = _VNDARRAY
_DATAEXCHANGEPROTOCOL.fields_by_name['f_ndarray_list'].message_type = _FNDARRAYLIST
_DATAEXCHANGEPROTOCOL.fields_by_name['v_ndarray_list'].message_type = _VNDARRAYLIST
_DATAEXCHANGEPROTOCOL.oneofs_by_name['container'].fields.append(
  _DATAEXCHANGEPROTOCOL.fields_by_name['scalar'])
_DATAEXCHANGEPROTOCOL.fields_by_name['scalar'].containing_oneof = _DATAEXCHANGEPROTOCOL.oneofs_by_name['container']
_DATAEXCHANGEPROTOCOL.oneofs_by_name['container'].fields.append(
  _DATAEXCHANGEPROTOCOL.fields_by_name['f_scalar_list'])
_DATAEXCHANGEPROTOCOL.fields_by_name['f_scalar_list'].containing_oneof = _DATAEXCHANGEPROTOCOL.oneofs_by_name['container']
_DATAEXCHANGEPROTOCOL.oneofs_by_name['container'].fields.append(
  _DATAEXCHANGEPROTOCOL.fields_by_name['v_scalar_list'])
_DATAEXCHANGEPROTOCOL.fields_by_name['v_scalar_list'].containing_oneof = _DATAEXCHANGEPROTOCOL.oneofs_by_name['container']
_DATAEXCHANGEPROTOCOL.oneofs_by_name['container'].fields.append(
  _DATAEXCHANGEPROTOCOL.fields_by_name['f_ndarray'])
_DATAEXCHANGEPROTOCOL.fields_by_name['f_ndarray'].containing_oneof = _DATAEXCHANGEPROTOCOL.oneofs_by_name['container']
_DATAEXCHANGEPROTOCOL.oneofs_by_name['container'].fields.append(
  _DATAEXCHANGEPROTOCOL.fields_by_name['v_ndarray'])
_DATAEXCHANGEPROTOCOL.fields_by_name['v_ndarray'].containing_oneof = _DATAEXCHANGEPROTOCOL.oneofs_by_name['container']
_DATAEXCHANGEPROTOCOL.oneofs_by_name['container'].fields.append(
  _DATAEXCHANGEPROTOCOL.fields_by_name['f_ndarray_list'])
_DATAEXCHANGEPROTOCOL.fields_by_name['f_ndarray_list'].containing_oneof = _DATAEXCHANGEPROTOCOL.oneofs_by_name['container']
_DATAEXCHANGEPROTOCOL.oneofs_by_name['container'].fields.append(
  _DATAEXCHANGEPROTOCOL.fields_by_name['v_ndarray_list'])
_DATAEXCHANGEPROTOCOL.fields_by_name['v_ndarray_list'].containing_oneof = _DATAEXCHANGEPROTOCOL.oneofs_by_name['container']
_FNDARRAYLIST.fields_by_name['ndarrays'].message_type = _FNDARRAY
_VNDARRAYLIST.fields_by_name['ndarrays'].message_type = _VNDARRAY
DESCRIPTOR.message_types_by_name['DataExchangeProtocol'] = _DATAEXCHANGEPROTOCOL
DESCRIPTOR.message_types_by_name['Scalar'] = _SCALAR
DESCRIPTOR.message_types_by_name['FScalarList'] = _FSCALARLIST
DESCRIPTOR.message_types_by_name['VScalarList'] = _VSCALARLIST
DESCRIPTOR.message_types_by_name['FNdArray'] = _FNDARRAY
DESCRIPTOR.message_types_by_name['VNdArray'] = _VNDARRAY
DESCRIPTOR.message_types_by_name['FNdArrayList'] = _FNDARRAYLIST
DESCRIPTOR.message_types_by_name['VNdArrayList'] = _VNDARRAYLIST
DESCRIPTOR.enum_types_by_name['ScalarType'] = _SCALARTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataExchangeProtocol = _reflection.GeneratedProtocolMessageType('DataExchangeProtocol', (_message.Message,), {
  'DESCRIPTOR' : _DATAEXCHANGEPROTOCOL,
  '__module__' : 'secretflow.ic.proto.runtime.data_exchange_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.runtime.DataExchangeProtocol)
  })
_sym_db.RegisterMessage(DataExchangeProtocol)

Scalar = _reflection.GeneratedProtocolMessageType('Scalar', (_message.Message,), {
  'DESCRIPTOR' : _SCALAR,
  '__module__' : 'secretflow.ic.proto.runtime.data_exchange_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.runtime.Scalar)
  })
_sym_db.RegisterMessage(Scalar)

FScalarList = _reflection.GeneratedProtocolMessageType('FScalarList', (_message.Message,), {
  'DESCRIPTOR' : _FSCALARLIST,
  '__module__' : 'secretflow.ic.proto.runtime.data_exchange_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.runtime.FScalarList)
  })
_sym_db.RegisterMessage(FScalarList)

VScalarList = _reflection.GeneratedProtocolMessageType('VScalarList', (_message.Message,), {
  'DESCRIPTOR' : _VSCALARLIST,
  '__module__' : 'secretflow.ic.proto.runtime.data_exchange_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.runtime.VScalarList)
  })
_sym_db.RegisterMessage(VScalarList)

FNdArray = _reflection.GeneratedProtocolMessageType('FNdArray', (_message.Message,), {
  'DESCRIPTOR' : _FNDARRAY,
  '__module__' : 'secretflow.ic.proto.runtime.data_exchange_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.runtime.FNdArray)
  })
_sym_db.RegisterMessage(FNdArray)

VNdArray = _reflection.GeneratedProtocolMessageType('VNdArray', (_message.Message,), {
  'DESCRIPTOR' : _VNDARRAY,
  '__module__' : 'secretflow.ic.proto.runtime.data_exchange_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.runtime.VNdArray)
  })
_sym_db.RegisterMessage(VNdArray)

FNdArrayList = _reflection.GeneratedProtocolMessageType('FNdArrayList', (_message.Message,), {
  'DESCRIPTOR' : _FNDARRAYLIST,
  '__module__' : 'secretflow.ic.proto.runtime.data_exchange_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.runtime.FNdArrayList)
  })
_sym_db.RegisterMessage(FNdArrayList)

VNdArrayList = _reflection.GeneratedProtocolMessageType('VNdArrayList', (_message.Message,), {
  'DESCRIPTOR' : _VNDARRAYLIST,
  '__module__' : 'secretflow.ic.proto.runtime.data_exchange_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.runtime.VNdArrayList)
  })
_sym_db.RegisterMessage(VNdArrayList)


# @@protoc_insertion_point(module_scope)