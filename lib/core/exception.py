#!/usr/bin/env python

"""
S3SS1Z T3AM project
"""

class SqlmapBaseException(Exception):
    pass

class SqlmapCompressionException(s1l3n7BaseException):
    pass

class SqlmapConnectionException(s1l3n7BaseException):
    pass

class SqlmapDataException(s1l3n7BaseException):
    pass

class SqlmapFilePathException(s1l3n7BaseException):
    pass

class SqlmapGenericException(s1l3n7BaseException):
    pass

class SqlmapInstallationException(s1l3n7BaseException):
    pass

class SqlmapMissingDependence(s1l3n7BaseException):
    pass

class SqlmapMissingMandatoryOptionException(s1l3n7BaseException):
    pass

class SqlmapMissingPrivileges(s1l3n7BaseException):
    pass

class SqlmapNoneDataException(s1l3n7BaseException):
    pass

class SqlmapNotVulnerableException(s1l3n7BaseException):
    pass

class SqlmapSilentQuitException(s1l3n7BaseException):
    pass

class SqlmapUserQuitException(s1l3n7BaseException):
    pass

class SqlmapShellQuitException(s1l3n7BaseException):
    pass

class SqlmapSkipTargetException(s1l3n7BaseException):
    pass

class SqlmapSyntaxException(s1l3n7BaseException):
    pass

class SqlmapSystemException(s1l3n7BaseException):
    pass

class SqlmapThreadException(s1l3n7BaseException):
    pass

class SqlmapTokenException(s1l3n7BaseException):
    pass

class SqlmapUndefinedMethod(s1l3n7BaseException):
    pass

class SqlmapUnsupportedDBMSException(s1l3n7BaseException):
    pass

class SqlmapUnsupportedFeatureException(s1l3n7BaseException):
    pass

class SqlmapValueException(s1l3n7BaseException):
    pass
