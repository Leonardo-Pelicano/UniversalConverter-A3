
"""Universal Converter package.

Provides ConversionService, Converter base classes, implementations for Temperature, Length and Weight,
a CLI and optional simple Flask-based web endpoint (disabled by default).
"""
from .service import ConversionService
from .cli import main as cli_main
