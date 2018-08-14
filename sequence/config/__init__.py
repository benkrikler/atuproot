from __future__ import absolute_import


def build_sequence(sequence_cfg_path):
    from ..sequence import sequence
    from ..Modules import ScribblerWrapper
    return [(ScribblerWrapper(reader), collector)
            for (reader, collector) in sequence]
