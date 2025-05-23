#!/bin/bash

set +e

# Install required packages
bash -c "$(curl -sL https://get-gnmic.openconfig.net)"
# go install github.com/aristanetworks/goarista/cmd/gnmi@latest
python3 -m pip install --upgrade pip
python3 -m pip install -r .devcontainer/requirements.txt