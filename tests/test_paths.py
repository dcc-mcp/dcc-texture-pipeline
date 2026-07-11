import importlib.util
from pathlib import Path


def load(path):
    spec = importlib.util.spec_from_file_location("command", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_oiio_rejects_overwrite(tmp_path):
    module = load(Path(__file__).parents[1] / "skill/oiio-textures/scripts/_command.py")
    source = tmp_path / "a.exr"
    source.write_bytes(b"x")
    try:
        module.new_output(str(source), str(source))
    except ValueError:
        pass
    else:
        raise AssertionError("source overwrite must fail")


def test_ocio_creates_output_parent(tmp_path):
    module = load(Path(__file__).parents[1] / "skill/ocio-color/scripts/_command.py")
    source = tmp_path / "a.exr"
    source.write_bytes(b"x")
    _, output = module.output_paths(str(source), str(tmp_path / "nested/b.exr"))
    assert output.parent.is_dir()
