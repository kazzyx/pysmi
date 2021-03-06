#
# This file is part of pysmi software.
#
# Copyright (c) 2015-2017, Ilya Etingof <etingof@gmail.com>
# License: http://pysmi.sf.net/license.html
#
from pysmi.borrower.base import AbstractBorrower


class AnyFileBorrower(AbstractBorrower):
    """Create arbitrary MIB file borrowing object"""
