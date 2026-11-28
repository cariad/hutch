from importlib.metadata import version

import pytest

from hutch.cli import main


def test_help_flag_prints_help(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that `--help` prints usage and exits successfully."""

    with pytest.raises(SystemExit) as exit_info:
        main(["--help"])

    assert exit_info.value.code == 0
    assert "usage: hutch" in capsys.readouterr().out


def test_no_arguments_fails(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that running without arguments fails with a usage error."""

    with pytest.raises(SystemExit) as exit_info:
        main([])

    assert exit_info.value.code == 2
    err = capsys.readouterr().err
    assert "usage: hutch" in err
    assert "the following arguments are required: verb, domain" in err


def test_unknown_argument_fails(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that an unknown argument fails with a usage error."""

    args = [
        "deploy",
        "cariad.engineering",
        "--nope",
    ]

    with pytest.raises(SystemExit) as exit_info:
        main(args)

    assert exit_info.value.code == 2
    assert "unrecognized arguments: --nope" in capsys.readouterr().err


def test_version_flag_prints_version(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that `--version` prints the version then exits successfully."""

    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])

    assert exit_info.value.code == 0
    assert capsys.readouterr().out.strip() == version("hutch")
