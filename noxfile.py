import nox
import nox_uv


@nox_uv.session(
    name="py-version",
    python=["3.10", "3.13"],
    reuse_venv=True,
    venv_backend="uv",
    uv_groups=["dev"],
    uv_sync_locked=False,
)
def test_different_python_versions(session: nox.Session) -> None:
    session.run("uv", "sync", "-U", "--dry-run")  # Using the newest dependencies, in new venv
    session.run("pytest")


@nox_uv.session(
    name="locked-deps",
    python=["3.10", "3.13"],
    reuse_venv=True,
    venv_backend="uv",
    uv_groups=["dev"],
)
def test_with_locked_dependencies(session: nox.Session) -> None:
    session.run("pytest")