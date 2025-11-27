
from abc import ABC, abstractmethod

class Converter(ABC):
    """Abstract base for converters that convert to/from a canonical base unit."""
    @abstractmethod
    def to_base(self, value):
        pass

    @abstractmethod
    def from_base(self, value):
        pass

class TempConverterBase(Converter):
    # base unit: Kelvin
    pass

class LengthConverterBase(Converter):
    # base unit: meter
    pass

class WeightConverterBase(Converter):
    # base unit: kilogram
    pass

# Temperature converters using Kelvin as base
class CelsiusConverter(TempConverterBase):
    def to_base(self, v): return float(v) + 273.15
    def from_base(self, v): return float(v) - 273.15

class FahrenheitConverter(TempConverterBase):
    def to_base(self, v): return (float(v) + 459.67) * 5/9
    def from_base(self, v): return float(v) * 9/5 - 459.67

class KelvinConverter(TempConverterBase):
    def to_base(self, v): return float(v)
    def from_base(self, v): return float(v)

class RankineConverter(TempConverterBase):
    def to_base(self, v): return float(v) * 5/9
    def from_base(self, v): return float(v) * 9/5

# Length converters using meters as base
class MeterConverter(LengthConverterBase):
    def to_base(self, v): return float(v)
    def from_base(self, v): return float(v)

class CentimeterConverter(LengthConverterBase):
    def to_base(self, v): return float(v)/100
    def from_base(self, v): return float(v)*100

class MillimeterConverter(LengthConverterBase):
    def to_base(self, v): return float(v)/1000
    def from_base(self, v): return float(v)*1000

class KilometerConverter(LengthConverterBase):
    def to_base(self, v): return float(v)*1000
    def from_base(self, v): return float(v)/1000

class InchConverter(LengthConverterBase):
    def to_base(self, v): return float(v)*0.0254
    def from_base(self, v): return float(v)/0.0254

class FootConverter(LengthConverterBase):
    def to_base(self, v): return float(v)*0.3048
    def from_base(self, v): return float(v)/0.3048

# Weight converters using kilograms as base
class KilogramConverter(WeightConverterBase):
    def to_base(self, v): return float(v)
    def from_base(self, v): return float(v)

class GramConverter(WeightConverterBase):
    def to_base(self, v): return float(v)/1000
    def from_base(self, v): return float(v)*1000

class MilligramConverter(WeightConverterBase):
    def to_base(self, v): return float(v)/1e6
    def from_base(self, v): return float(v)*1e6

class PoundConverter(WeightConverterBase):
    def to_base(self, v): return float(v)*0.45359237
    def from_base(self, v): return float(v)/0.45359237
