"""Decision OS — a sovereign, agnostic decision platform for the enterprise.

This package is organised as the six architecture layers from the execution
plan. Each layer is a module so the structure of the code mirrors the picture
you show a co-founder or investor:

    Layer 5  Experience .................. api.py + web/index.html
    Layer 4  Reasoning & agents .......... reasoning.py
    Layer 3  Semantic layer ("one brain")  semantic.py
    Layer 2  Connective tissue ........... connectors.py
    Layer 1  Governance & sovereignty .... governance.py
    Layer 0  Deployment substrate ........ db.py + config.py  (local, in-boundary)

Sovereign by default: everything runs on your own machine and, with the
built-in local model provider, makes zero external network calls. Your data
never leaves the box.
"""

__version__ = "0.1.0"
