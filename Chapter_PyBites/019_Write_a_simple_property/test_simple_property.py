from datetime import timedelta
import inspect

from datetime import timedelta
import inspect

from simple_property import Promo, NOW

def test_promo_expired():
    past = datetime.today() - timedelta(days=365)
    mypromo_past=Promo('promocion_past',past)
    assert mypromo_past.expired

def test_promo_not_expired():
    future = datetime.today() + timedelta(days=365)
    mypromo_future=Promo('promocion_future',future)  
    assert not mypromo_future.expired

def test_uses_property():
    assert 'property' in inspect.getsource(Promo)