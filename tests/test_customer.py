from customer import Customer

def test_customer_name():
    c1 = Customer("Esther")
    assert c1.name == "Esther"
    
    c2 = Customer("Joy")
    assert c2.name == "Joy"

def test_bad_names():
    try:
        Customer("MyNameIsEstherMuthoni")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    try:
        Customer(123)
        assert False, "Should have raised TypeError"
    except TypeError:
        pass