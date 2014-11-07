from pyexperian import services


def test_business_no_address():
    business = {'name': 'Franklin BBQ'}
    translated = services.BaseProduct._translate_business(business)
    assert 'CurrentAddress' not in translated

    business['address'] = {}
    translated = services.BaseProduct._translate_business(business)
    assert 'CurrentAddress' not in translated


def test_good_business():
    business = {'name': 'Franklin BBQ', 'address': {'city': 'austin', 'state': 'tx', 'zip': '78701', 'street': ''}}
    translated = services.BaseProduct._translate_business(business)
    assert 'BusinessName' in translated
    assert 'CurrentAddress' in translated
    assert 'Street' not in translated['CurrentAddress'] and 'City' in translated['CurrentAddress'] and 'State' in translated['CurrentAddress'] and 'Zip' in translated['CurrentAddress']
