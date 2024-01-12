import functools
import os

import nox

nox.options.envdir = "build/nox"
nox.options.sessions = ["build_container"]

@nox.session(python=None)
@nox.parametrize("base_python", ["3.11", "3.12"])
def build_container(session, base_python):
    session.run(
        "docker",
        "build",
        "--build-arg",
        f"BUILD_BASE=python:{base_python}",
        "--build-arg",
        "NAME=kalyke",
        "-f",
        "container.kalyke",
        "-t",
        f"moshez/kalyke:{base_python}",
        ".",
    )

@nox.session(python="3.11")
def refresh_deps(session):
    """Refresh the requirements.txt file"""
    session.install("pip-tools")
    session.run(
        "pip-compile",
        "--verbose",
        "--resolver=backtracking",
    )
