import pytest
import graphics.gaussian_splat_sort as mod

CASES = [
    ("sort_fence", (1,)),
    ("defer_recycle", (1,)),
    ("min_coverage", (1,)),
    ("sort_per_camera", (1,)),
    ("stable_tie", (1,)),
    ("load", (1,)),
    ("sort", (1,)),
    ("cull", (1,)),
    ("draw", (1,)),
    ("unload", (1,)),
    ("validate_splat", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
