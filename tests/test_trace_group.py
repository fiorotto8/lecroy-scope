import pytest

from numpy.testing import assert_array_equal
import numpy as np
from pathlib import Path

import lecroyscope

files_path = Path(__file__).parent / "files"


def test_trace_group_from_files(tmp_path):
    filename = files_path / "header.trc"

    filenames = []
    channels = [1, 2, 3, 4]
    for channel in channels:
        filename = f"C{channel}Trace00001.trc"
        tmp_file = tmp_path / filename
        tmp_file.write_bytes((files_path / "header.trc").read_bytes())
        filenames.append(tmp_file)

    trace_group = lecroyscope.TraceGroup(*filenames)

    for i, trace in enumerate(trace_group):
        assert isinstance(trace, lecroyscope.Trace)
        assert trace.channel == channels[i]

    assert len(trace_group) == len(channels)

    for channel in channels:
        assert channel == trace_group[channel].channel
