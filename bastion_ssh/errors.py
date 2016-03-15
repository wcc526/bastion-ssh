#!/usr/bin/env python
# coding: utf-8

class ClientError(Exception):
    pass


class ServerError(Exception):
    pass


class BadParameter(RuntimeError):
    pass


class DockerNotFound(RuntimeError):
    pass


class PublicImageNotFound(RuntimeError):
    pass


class StreamOutputError(Exception):
    pass


class InternalError(RuntimeError):
    pass


class ConnectionError(RuntimeError):
    pass


class MissingAsset(RuntimeError):
    pass


class NothingChanged(RuntimeError):
    pass
