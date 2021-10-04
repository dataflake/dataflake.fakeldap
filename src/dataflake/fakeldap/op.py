##############################################################################
#
# Copyright (c) 2012-2021 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from .utils import from_utf8


class Op:
    """ A simple representation for operators like !, &, |

    Operators chain or qualify a set of LDAP search filters
    """

    def __init__(self, op):
        self.op = op

    def __repr__(self):
        return "Op('%s')" % from_utf8(self.op)
