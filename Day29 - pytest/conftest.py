import pytest
@pytest.fixture
def sample_number():
    print("running fixture")
    return (10,20)