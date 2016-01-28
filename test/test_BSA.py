# -*- coding: utf-8 -*-
"""
Tests using the standard BSA data from SASBDB (SASDA32)

"""

import os.path

from sasciftools.mmCif import mmcifIO


BSA_file = os.path.join(os.path.dirname(__file__),
                        "SASDA32.sascif")


def test_open():
    sasCIFIn = mmcifIO.CifFileReader()
    sasCIFDict = sasCIFIn.read(BSA_file)
    assert len(sasCIFDict) > 0
