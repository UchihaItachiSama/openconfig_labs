#!/bin/bash

set +e

# Install required packages
bash -c "$(curl -sL https://get-gnmic.openconfig.net)"
bash -c "$(curl -sL https://get-gnoic.kmrd.dev)"
python3 -m pip install --upgrade pip
python3 -m pip install -r .devcontainer/requirements.txt