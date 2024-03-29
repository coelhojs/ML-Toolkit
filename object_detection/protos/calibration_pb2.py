# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_scripts/object_detection/protos/calibration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_scripts/object_detection/protos/calibration.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n<tensorflow_scripts/object_detection/protos/calibration.proto\x12\x17object_detection.protos\"\xe4\x03\n\x11\x43\x61librationConfig\x12P\n\x16\x66unction_approximation\x18\x01 \x01(\x0b\x32..object_detection.protos.FunctionApproximationH\x00\x12\x62\n class_id_function_approximations\x18\x02 \x01(\x0b\x32\x36.object_detection.protos.ClassIdFunctionApproximationsH\x00\x12J\n\x13sigmoid_calibration\x18\x03 \x01(\x0b\x32+.object_detection.protos.SigmoidCalibrationH\x00\x12\\\n\x1d\x63lass_id_sigmoid_calibrations\x18\x04 \x01(\x0b\x32\x33.object_detection.protos.ClassIdSigmoidCalibrationsH\x00\x12\x61\n\x1ftemperature_scaling_calibration\x18\x05 \x01(\x0b\x32\x36.object_detection.protos.TemperatureScalingCalibrationH\x00\x42\x0c\n\ncalibrator\"L\n\x15\x46unctionApproximation\x12\x33\n\tx_y_pairs\x18\x01 \x01(\x0b\x32 .object_detection.protos.XYPairs\"\xe9\x01\n\x1d\x43lassIdFunctionApproximations\x12l\n\x15\x63lass_id_xy_pairs_map\x18\x01 \x03(\x0b\x32M.object_detection.protos.ClassIdFunctionApproximations.ClassIdXyPairsMapEntry\x1aZ\n\x16\x43lassIdXyPairsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .object_detection.protos.XYPairs:\x02\x38\x01\"\\\n\x12SigmoidCalibration\x12\x46\n\x12sigmoid_parameters\x18\x01 \x01(\x0b\x32*.object_detection.protos.SigmoidParameters\"\x8b\x02\n\x1a\x43lassIdSigmoidCalibrations\x12}\n\x1f\x63lass_id_sigmoid_parameters_map\x18\x01 \x03(\x0b\x32T.object_detection.protos.ClassIdSigmoidCalibrations.ClassIdSigmoidParametersMapEntry\x1an\n ClassIdSigmoidParametersMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.object_detection.protos.SigmoidParameters:\x02\x38\x01\"/\n\x1dTemperatureScalingCalibration\x12\x0e\n\x06scaler\x18\x01 \x01(\x02\"\xab\x01\n\x07XYPairs\x12\x39\n\x08x_y_pair\x18\x01 \x03(\x0b\x32\'.object_detection.protos.XYPairs.XYPair\x12\x45\n\x12training_data_type\x18\x02 \x01(\x0e\x32).object_detection.protos.TrainingDataType\x1a\x1e\n\x06XYPair\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"0\n\x11SigmoidParameters\x12\r\n\x01\x61\x18\x01 \x01(\x02:\x02-1\x12\x0c\n\x01\x62\x18\x02 \x01(\x02:\x01\x30*N\n\x10TrainingDataType\x12\x15\n\x11\x44\x41TA_TYPE_UNKNOWN\x10\x00\x12\x0f\n\x0b\x41LL_CLASSES\x10\x01\x12\x12\n\x0e\x43LASS_SPECIFIC\x10\x02')
)

_TRAININGDATATYPE = _descriptor.EnumDescriptor(
  name='TrainingDataType',
  full_name='object_detection.protos.TrainingDataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DATA_TYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALL_CLASSES', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLASS_SPECIFIC', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1527,
  serialized_end=1605,
)
_sym_db.RegisterEnumDescriptor(_TRAININGDATATYPE)

TrainingDataType = enum_type_wrapper.EnumTypeWrapper(_TRAININGDATATYPE)
DATA_TYPE_UNKNOWN = 0
ALL_CLASSES = 1
CLASS_SPECIFIC = 2



_CALIBRATIONCONFIG = _descriptor.Descriptor(
  name='CalibrationConfig',
  full_name='object_detection.protos.CalibrationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='function_approximation', full_name='object_detection.protos.CalibrationConfig.function_approximation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_id_function_approximations', full_name='object_detection.protos.CalibrationConfig.class_id_function_approximations', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sigmoid_calibration', full_name='object_detection.protos.CalibrationConfig.sigmoid_calibration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_id_sigmoid_calibrations', full_name='object_detection.protos.CalibrationConfig.class_id_sigmoid_calibrations', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature_scaling_calibration', full_name='object_detection.protos.CalibrationConfig.temperature_scaling_calibration', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='calibrator', full_name='object_detection.protos.CalibrationConfig.calibrator',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=90,
  serialized_end=574,
)


_FUNCTIONAPPROXIMATION = _descriptor.Descriptor(
  name='FunctionApproximation',
  full_name='object_detection.protos.FunctionApproximation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_y_pairs', full_name='object_detection.protos.FunctionApproximation.x_y_pairs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=576,
  serialized_end=652,
)


_CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY = _descriptor.Descriptor(
  name='ClassIdXyPairsMapEntry',
  full_name='object_detection.protos.ClassIdFunctionApproximations.ClassIdXyPairsMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='object_detection.protos.ClassIdFunctionApproximations.ClassIdXyPairsMapEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='object_detection.protos.ClassIdFunctionApproximations.ClassIdXyPairsMapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=798,
  serialized_end=888,
)

_CLASSIDFUNCTIONAPPROXIMATIONS = _descriptor.Descriptor(
  name='ClassIdFunctionApproximations',
  full_name='object_detection.protos.ClassIdFunctionApproximations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_id_xy_pairs_map', full_name='object_detection.protos.ClassIdFunctionApproximations.class_id_xy_pairs_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=655,
  serialized_end=888,
)


_SIGMOIDCALIBRATION = _descriptor.Descriptor(
  name='SigmoidCalibration',
  full_name='object_detection.protos.SigmoidCalibration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sigmoid_parameters', full_name='object_detection.protos.SigmoidCalibration.sigmoid_parameters', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=890,
  serialized_end=982,
)


_CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY = _descriptor.Descriptor(
  name='ClassIdSigmoidParametersMapEntry',
  full_name='object_detection.protos.ClassIdSigmoidCalibrations.ClassIdSigmoidParametersMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='object_detection.protos.ClassIdSigmoidCalibrations.ClassIdSigmoidParametersMapEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='object_detection.protos.ClassIdSigmoidCalibrations.ClassIdSigmoidParametersMapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1142,
  serialized_end=1252,
)

_CLASSIDSIGMOIDCALIBRATIONS = _descriptor.Descriptor(
  name='ClassIdSigmoidCalibrations',
  full_name='object_detection.protos.ClassIdSigmoidCalibrations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_id_sigmoid_parameters_map', full_name='object_detection.protos.ClassIdSigmoidCalibrations.class_id_sigmoid_parameters_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=985,
  serialized_end=1252,
)


_TEMPERATURESCALINGCALIBRATION = _descriptor.Descriptor(
  name='TemperatureScalingCalibration',
  full_name='object_detection.protos.TemperatureScalingCalibration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scaler', full_name='object_detection.protos.TemperatureScalingCalibration.scaler', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1254,
  serialized_end=1301,
)


_XYPAIRS_XYPAIR = _descriptor.Descriptor(
  name='XYPair',
  full_name='object_detection.protos.XYPairs.XYPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='object_detection.protos.XYPairs.XYPair.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='object_detection.protos.XYPairs.XYPair.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1445,
  serialized_end=1475,
)

_XYPAIRS = _descriptor.Descriptor(
  name='XYPairs',
  full_name='object_detection.protos.XYPairs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_y_pair', full_name='object_detection.protos.XYPairs.x_y_pair', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_data_type', full_name='object_detection.protos.XYPairs.training_data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_XYPAIRS_XYPAIR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1304,
  serialized_end=1475,
)


_SIGMOIDPARAMETERS = _descriptor.Descriptor(
  name='SigmoidParameters',
  full_name='object_detection.protos.SigmoidParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='object_detection.protos.SigmoidParameters.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='object_detection.protos.SigmoidParameters.b', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1477,
  serialized_end=1525,
)

_CALIBRATIONCONFIG.fields_by_name['function_approximation'].message_type = _FUNCTIONAPPROXIMATION
_CALIBRATIONCONFIG.fields_by_name['class_id_function_approximations'].message_type = _CLASSIDFUNCTIONAPPROXIMATIONS
_CALIBRATIONCONFIG.fields_by_name['sigmoid_calibration'].message_type = _SIGMOIDCALIBRATION
_CALIBRATIONCONFIG.fields_by_name['class_id_sigmoid_calibrations'].message_type = _CLASSIDSIGMOIDCALIBRATIONS
_CALIBRATIONCONFIG.fields_by_name['temperature_scaling_calibration'].message_type = _TEMPERATURESCALINGCALIBRATION
_CALIBRATIONCONFIG.oneofs_by_name['calibrator'].fields.append(
  _CALIBRATIONCONFIG.fields_by_name['function_approximation'])
_CALIBRATIONCONFIG.fields_by_name['function_approximation'].containing_oneof = _CALIBRATIONCONFIG.oneofs_by_name['calibrator']
_CALIBRATIONCONFIG.oneofs_by_name['calibrator'].fields.append(
  _CALIBRATIONCONFIG.fields_by_name['class_id_function_approximations'])
_CALIBRATIONCONFIG.fields_by_name['class_id_function_approximations'].containing_oneof = _CALIBRATIONCONFIG.oneofs_by_name['calibrator']
_CALIBRATIONCONFIG.oneofs_by_name['calibrator'].fields.append(
  _CALIBRATIONCONFIG.fields_by_name['sigmoid_calibration'])
_CALIBRATIONCONFIG.fields_by_name['sigmoid_calibration'].containing_oneof = _CALIBRATIONCONFIG.oneofs_by_name['calibrator']
_CALIBRATIONCONFIG.oneofs_by_name['calibrator'].fields.append(
  _CALIBRATIONCONFIG.fields_by_name['class_id_sigmoid_calibrations'])
_CALIBRATIONCONFIG.fields_by_name['class_id_sigmoid_calibrations'].containing_oneof = _CALIBRATIONCONFIG.oneofs_by_name['calibrator']
_CALIBRATIONCONFIG.oneofs_by_name['calibrator'].fields.append(
  _CALIBRATIONCONFIG.fields_by_name['temperature_scaling_calibration'])
_CALIBRATIONCONFIG.fields_by_name['temperature_scaling_calibration'].containing_oneof = _CALIBRATIONCONFIG.oneofs_by_name['calibrator']
_FUNCTIONAPPROXIMATION.fields_by_name['x_y_pairs'].message_type = _XYPAIRS
_CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY.fields_by_name['value'].message_type = _XYPAIRS
_CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY.containing_type = _CLASSIDFUNCTIONAPPROXIMATIONS
_CLASSIDFUNCTIONAPPROXIMATIONS.fields_by_name['class_id_xy_pairs_map'].message_type = _CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY
_SIGMOIDCALIBRATION.fields_by_name['sigmoid_parameters'].message_type = _SIGMOIDPARAMETERS
_CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY.fields_by_name['value'].message_type = _SIGMOIDPARAMETERS
_CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY.containing_type = _CLASSIDSIGMOIDCALIBRATIONS
_CLASSIDSIGMOIDCALIBRATIONS.fields_by_name['class_id_sigmoid_parameters_map'].message_type = _CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY
_XYPAIRS_XYPAIR.containing_type = _XYPAIRS
_XYPAIRS.fields_by_name['x_y_pair'].message_type = _XYPAIRS_XYPAIR
_XYPAIRS.fields_by_name['training_data_type'].enum_type = _TRAININGDATATYPE
DESCRIPTOR.message_types_by_name['CalibrationConfig'] = _CALIBRATIONCONFIG
DESCRIPTOR.message_types_by_name['FunctionApproximation'] = _FUNCTIONAPPROXIMATION
DESCRIPTOR.message_types_by_name['ClassIdFunctionApproximations'] = _CLASSIDFUNCTIONAPPROXIMATIONS
DESCRIPTOR.message_types_by_name['SigmoidCalibration'] = _SIGMOIDCALIBRATION
DESCRIPTOR.message_types_by_name['ClassIdSigmoidCalibrations'] = _CLASSIDSIGMOIDCALIBRATIONS
DESCRIPTOR.message_types_by_name['TemperatureScalingCalibration'] = _TEMPERATURESCALINGCALIBRATION
DESCRIPTOR.message_types_by_name['XYPairs'] = _XYPAIRS
DESCRIPTOR.message_types_by_name['SigmoidParameters'] = _SIGMOIDPARAMETERS
DESCRIPTOR.enum_types_by_name['TrainingDataType'] = _TRAININGDATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CalibrationConfig = _reflection.GeneratedProtocolMessageType('CalibrationConfig', (_message.Message,), dict(
  DESCRIPTOR = _CALIBRATIONCONFIG,
  __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.CalibrationConfig)
  ))
_sym_db.RegisterMessage(CalibrationConfig)

FunctionApproximation = _reflection.GeneratedProtocolMessageType('FunctionApproximation', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONAPPROXIMATION,
  __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.FunctionApproximation)
  ))
_sym_db.RegisterMessage(FunctionApproximation)

ClassIdFunctionApproximations = _reflection.GeneratedProtocolMessageType('ClassIdFunctionApproximations', (_message.Message,), dict(

  ClassIdXyPairsMapEntry = _reflection.GeneratedProtocolMessageType('ClassIdXyPairsMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY,
    __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.ClassIdFunctionApproximations.ClassIdXyPairsMapEntry)
    ))
  ,
  DESCRIPTOR = _CLASSIDFUNCTIONAPPROXIMATIONS,
  __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ClassIdFunctionApproximations)
  ))
_sym_db.RegisterMessage(ClassIdFunctionApproximations)
_sym_db.RegisterMessage(ClassIdFunctionApproximations.ClassIdXyPairsMapEntry)

SigmoidCalibration = _reflection.GeneratedProtocolMessageType('SigmoidCalibration', (_message.Message,), dict(
  DESCRIPTOR = _SIGMOIDCALIBRATION,
  __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SigmoidCalibration)
  ))
_sym_db.RegisterMessage(SigmoidCalibration)

ClassIdSigmoidCalibrations = _reflection.GeneratedProtocolMessageType('ClassIdSigmoidCalibrations', (_message.Message,), dict(

  ClassIdSigmoidParametersMapEntry = _reflection.GeneratedProtocolMessageType('ClassIdSigmoidParametersMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY,
    __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.ClassIdSigmoidCalibrations.ClassIdSigmoidParametersMapEntry)
    ))
  ,
  DESCRIPTOR = _CLASSIDSIGMOIDCALIBRATIONS,
  __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.ClassIdSigmoidCalibrations)
  ))
_sym_db.RegisterMessage(ClassIdSigmoidCalibrations)
_sym_db.RegisterMessage(ClassIdSigmoidCalibrations.ClassIdSigmoidParametersMapEntry)

TemperatureScalingCalibration = _reflection.GeneratedProtocolMessageType('TemperatureScalingCalibration', (_message.Message,), dict(
  DESCRIPTOR = _TEMPERATURESCALINGCALIBRATION,
  __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.TemperatureScalingCalibration)
  ))
_sym_db.RegisterMessage(TemperatureScalingCalibration)

XYPairs = _reflection.GeneratedProtocolMessageType('XYPairs', (_message.Message,), dict(

  XYPair = _reflection.GeneratedProtocolMessageType('XYPair', (_message.Message,), dict(
    DESCRIPTOR = _XYPAIRS_XYPAIR,
    __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.XYPairs.XYPair)
    ))
  ,
  DESCRIPTOR = _XYPAIRS,
  __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.XYPairs)
  ))
_sym_db.RegisterMessage(XYPairs)
_sym_db.RegisterMessage(XYPairs.XYPair)

SigmoidParameters = _reflection.GeneratedProtocolMessageType('SigmoidParameters', (_message.Message,), dict(
  DESCRIPTOR = _SIGMOIDPARAMETERS,
  __module__ = 'tensorflow_scripts.object_detection.protos.calibration_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.SigmoidParameters)
  ))
_sym_db.RegisterMessage(SigmoidParameters)


_CLASSIDFUNCTIONAPPROXIMATIONS_CLASSIDXYPAIRSMAPENTRY._options = None
_CLASSIDSIGMOIDCALIBRATIONS_CLASSIDSIGMOIDPARAMETERSMAPENTRY._options = None
# @@protoc_insertion_point(module_scope)
