import pytest

@pytest.fixture()
def setup():
    print("Launch Browser")
    print("Login")
    print("Browse Products")
    yield
    print("Logoff")
    print("Close browser")
def testAddItemtoCart(setup):
    print("Add Items to the cart")
def testRemoveItemFromCart(setup):
    print("Remove Items from the cart")