from main.data.models import Dummy


# Test to ensure a new record can be created from the models imported
def test_new_dummy(new_dummy):
    """
    GIVEN a Dummy model
    WHEN a new Dummy is created
    THEN check that a new id is generated
    """
    assert new_dummy.name == 'wibble'
    assert new_dummy.description == 'wobble'
    assert type(new_dummy.id) is int
