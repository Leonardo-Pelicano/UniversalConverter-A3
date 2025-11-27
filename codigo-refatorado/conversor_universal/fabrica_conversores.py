
from .converters import (
    CelsiusConverter, FahrenheitConverter, KelvinConverter, RankineConverter,
    MeterConverter, CentimeterConverter, MillimeterConverter, KilometerConverter,
    InchConverter, FootConverter,
    KilogramConverter, GramConverter, MilligramConverter, PoundConverter
)

class ConverterFactory:
    """Create converter instances by unit symbol."""
    TEMP = {'c':'celsius','f':'fahrenheit','k':'kelvin','r':'rankine'}
    LEN = {'m':'meter','cm':'centimeter','mm':'millimeter','km':'kilometer','in':'inch','ft':'foot'}
    WGT = {'kg':'kilogram','g':'gram','mg':'milligram','lb':'pound','lb':'pound'}

    @staticmethod
    def get_converter_for(unit):
        u = unit.lower()
        # temperature
        if u in ['c','celsius']:
            return CelsiusConverter()
        if u in ['f','fahrenheit']:
            return FahrenheitConverter()
        if u in ['k','kelvin']:
            return KelvinConverter()
        if u in ['r','rankine']:
            return RankineConverter()
        # length
        if u in ['m','meter','metre']:
            return MeterConverter()
        if u in ['cm','centimeter','centimetre']:
            return CentimeterConverter()
        if u in ['mm','millimeter','millimetre']:
            return MillimeterConverter()
        if u in ['km','kilometer','kilometre']:
            return KilometerConverter()
        if u in ['in','inch','inches']:
            return InchConverter()
        if u in ['ft','foot','feet']:
            return FootConverter()
        # weight
        if u in ['kg','kilogram','kilograms']:
            return KilogramConverter()
        if u in ['g','gram','grams']:
            return GramConverter()
        if u in ['mg','milligram','milligrams']:
            return MilligramConverter()
        if u in ['lb','pound','pounds','lbs']:
            return PoundConverter()
        return None
