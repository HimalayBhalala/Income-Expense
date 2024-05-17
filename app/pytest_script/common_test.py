import pytest

@pytest.fixture(scope='module')
def SetUpTearDownClass():
    print("Setupclass Working...................")
    yield
    print("TearDownClass Working................")


@pytest.fixture()
def setupmethod():
    print("setup method worked....")
    yield
    print("teardown method worked....")


