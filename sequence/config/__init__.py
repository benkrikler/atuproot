from __future__ import absolute_import
from fast_flow.v1 import read_sequence_yaml, read_sequence_dict


__all__ = ["read_sequence_yaml", "read_sequence_dict"]


def build_sequence(sequence_cfg_path):
    from ..sequence import sequence
    from ..collectors import reader_collectors
    from ..Modules import ScribblerWrapper
    from alphatwirl.loop import NullCollector
    return [(ScribblerWrapper(module), NullCollector())
                           for module in sequence] + reader_collectors
