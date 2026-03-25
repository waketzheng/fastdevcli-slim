import shlex
import subprocess


def capture_output(cmd: str) -> str:
    r = subprocess.run(shlex.split(cmd), capture_output=True, text=True, encoding="utf-8")
    return r.stdout.strip()


def test_uvx():
    cmd_old = "uvx --from fastdevcli-slim fast version"
    cmd_new = "uvx --from fast-dev-cli fast version"
    assert capture_output(cmd_old) == capture_output(cmd_new)
