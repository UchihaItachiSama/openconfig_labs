#!/bin/bash

set +e

# Install required packages
bash -c "$(curl -sL https://get-gnmic.openconfig.net)"
python3 -m pip install pyang
python3 -m pip install pyangbind
