import pytest
import os
import datetime
from app import cli
from click.testing import CliRunner
from app.repositories.taskRepository import loadJson

@pytest.fixture()
def runner():
    cli.DATABASE = "db/tasks_test.json"
    yield CliRunner()
    #Teardown
    if os.path.exists(cli.DATABASE):
        os.remove(cli.DATABASE)

@pytest.fixture(scope="session")
def teardown():
    yield "Session scope"
    

def test_add(runner):  
    expectedUid = 1
    expectedTitle = "Hello World"
    expectedDesc = "Much wow"   
    result = runner.invoke(cli.add, [expectedTitle, expectedDesc])
    assert result.exit_code == 0
    results = loadJson(cli.DATABASE)
    assert expectedUid == results[0]['uid'], "Add command failed: UID is incorrect."
    assert expectedTitle in results[0]['title'], "Add command failed: Title is incorrect."
    assert expectedDesc in results[0]['description'], "Add command failed: Description is incorrect."

def test_list(runner):
    expectedTitle = "Title One"
    expectedDesc = "Something"   
    expectedStatus = "todo"
    expectedCreatedAt = datetime.date.today().strftime("%B %d, %Y")
    runner.invoke(cli.add, [expectedTitle, expectedDesc])
    result = runner.invoke(cli.list)
    assert result.exit_code == 0
    assert expectedTitle in result.output, "List command failed: Title is incorrect."
    assert expectedDesc in result.output, "List command failed: Description is incorrect."
    assert expectedStatus in result.output, "List command failed: Status is incorrect."
    assert expectedCreatedAt in result.output, "List command failed: Created At is incorrect."

def test_update(runner):
    uid = "1"
    expectedTitle = 'Goodbye World'
    expectedDesc = "I was updated!"
    runner.invoke(cli.add, ['Hello World', 'Much wow'])
    result = runner.invoke(cli.update, [uid, expectedTitle, "-d", expectedDesc])
    assert result.exit_code == 0
    results = loadJson(cli.DATABASE)
    assert expectedTitle in results[0]['title'], "Update command failed: Title is incorrect."
    assert expectedDesc in results[0]['description'], "Update command failed: Description is incorrect."
    
def test_updateInvalidUid(runner):
    uid = "asdf"
    expectedTitle = 'Goodbye World'
    expectedDesc = "I was updated!"
    runner.invoke(cli.add, ['Hello World', 'Much wow'])
    result = runner.invoke(cli.update, [uid, expectedTitle, "-d", expectedDesc])
    assert result.exit_code == 2
    assert "Error: Invalid value: UID must be a valid interger." in result.output

def test_delete(runner):
    pass

def test_mark(runner):
    pass