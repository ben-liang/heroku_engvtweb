#!/bin/bash

echo "Put this in your profile:"
echo "export ATLAS=None"
echo "export BLAS=/usr/local/opt/openblas/lib/libopenblas.dylib"
echo "export LAPACK=/usr/local/opt/openblas/lib/libopenblas.dylib"

brew install gcc gpp

brew install python
brew linkapps

# Ensure all scipy deps are met by installing it here as well as virtualenvs
brew tap homebrew/science
brew install openblas  # Apple Accelerate (included BLAS) fails scipy unittests
brew tap homebrew/python
brew install numpy --with-openblas
brew install scipy --with-openblas
brew install matplotlib

# Handle all other packages we need
brew install gmp mysql postgresql ruby md5sha1sum wget cmake