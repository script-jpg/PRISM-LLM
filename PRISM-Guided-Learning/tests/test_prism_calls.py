"""The planner runs exactly the PRISM commands it ran before PRISM calls became yielded tasks
(tests/data/prism_calls.json, recorded on the earlier code; see tests/prism_calls.py)."""
import json
import shutil

import pytest

from prism_calls import BASELINE, collect

needs_prism = pytest.mark.skipif(not shutil.which("prism"), reason="PRISM not on PATH")


@needs_prism
def test_each_instance_runs_the_recorded_prism_commands_in_order():
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    now = collect()
    assert list(now) == list(baseline)
    for case in baseline:
        assert now[case] == baseline[case], case
