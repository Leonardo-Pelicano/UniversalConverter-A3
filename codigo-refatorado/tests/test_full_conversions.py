
import pytest
from universal_converter.service import ConversionService

svc = ConversionService()

@pytest.mark.parametrize('v,frm,to,expected', [
    (0,'c','f',32),
    (100,'c','k',373.15),
    (32,'f','c',0),
    (273.15,'k','c',0),
    (0,'r','f',-459.67),

    (1,'m','cm',100),
    (100,'cm','m',1),
    (1,'km','m',1000),
    (12,'in','cm',30.48),

    (1,'kg','g',1000),
    (1000,'g','kg',1),
    (2,'lb','kg',0.90718474)
])
def test_valid_conversions(v,frm,to,expected):
    out = svc.convert(v,frm,to)
    assert round(out,6) == round(expected,6)

def test_invalid_units():
    assert svc.convert(1,'abc','m') is None
    assert svc.convert(1,'m','xyz') is None

def test_non_numeric():
    assert svc.convert('foo','m','cm') is None
