# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface


class IMycompanyMyproductLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IMyType(Interface):
    """
    Marker interface for .mytype.MyType
    """
