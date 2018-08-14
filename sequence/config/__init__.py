from __future__ import absolute_import
from fast_flow.v1 import read_sequence_yaml, read_sequence_dict


__all__ = ["read_sequence_yaml", "read_sequence_dict"]


def build_sequence(sequence_cfg_path):
    from ..sequence import sequence
    from ..Modules import ScribblerWrapper
    return [(ScribblerWrapper(reader), collector)
            for (reader, collector) in sequence]
