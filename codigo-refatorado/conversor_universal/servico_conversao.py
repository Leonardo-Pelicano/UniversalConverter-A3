
from .factory import ConverterFactory

class ConversionService:
    """Service that converts between units using converters and canonical base units."""
    def convert(self, value, from_unit, to_unit):
        try:
            # value may be string; try cast
            v = float(value)
        except:
            return None
        from_conv = ConverterFactory.get_converter_for(from_unit)
        to_conv = ConverterFactory.get_converter_for(to_unit)
        if from_conv is None or to_conv is None:
            return None
        base = from_conv.to_base(v)
        return to_conv.from_base(base)
