import pytest
import os
from app import cli
from click.testing import CliRunner

@pytest.fixture()
def runner():
    cli._dbjson = "db/tasks_test.json"
    yield CliRunner()
    if os.path.exists(cli._dbjson):
        os.remove(cli._dbjson)

@pytest.fixture(scope="session")
def teardown():
    yield "Session scope"
    

def test_add(runner):   
    result = runner.invoke(cli.add, ['Hello World', 'Much wow'])
    assert result.exit_code == 0
    result = runner.invoke(cli.list)
    print(result.output)
    assert "Hello World" in result.output, "Add command failed: Title is incorrect."
    assert "Much wow" in result.output, "Add command failed: Description is incorrect."

def test_update(runner):
    pass

def test_delete(runner):
    pass

def test_mark(runner):
    pass