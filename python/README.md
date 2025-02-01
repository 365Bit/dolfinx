# DOLFINx Python interface installation

Below is guidance for building the DOLFINx Python interface.

1. Build and install the DOLFINx C++ library.

2. Ensure the Python interface build requirements are installed:

          pip install -r build-requirements.txt

3. Build DOLFINx Python interface:

          pip install --check-build-dependencies --no-build-isolation .

To build in debug and editable mode for development:

     pip -v install --check-build-dependencies --config-settings=build-dir="build" --config-settings=cmake.build-type="Debug"  --config-settings=install.strip=false --no-build-isolation -e .

### Re-generating nanobind stubs

To update the nanobind type stubs, after installing the DOLFINx Python interface, run:
```sh
python -m nanobind.stubgen -m dolfinx.cpp -M dolfinx/py.typed -o dolfinx/cpp.pyi
```
from the `python/` directory.