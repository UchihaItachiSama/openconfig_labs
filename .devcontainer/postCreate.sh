#!/bin/bash

pull_arch_specific_ceos_image() {
    #Get the architecture
    local arch=$(uname -m)
    # Based on arch pull arm or 64bit image
    case ${arch} in
        x86_64)
            echo "Detected AMD64/x86_64 architecture. Pulling cEOS64-lab image"
            ardl get eos --format cEOS64 --version 4.34.1F --import-docker
            return $?
            ;;
        aarch64|arm64)
            echo "Detected ARM64/aarch64 architecture. Pulling cEOSarm-lab image"
            ardl get eos --format cEOSarm --version 4.34.1F --import-docker
            return $?
            ;;
        *)
            echo "Error: Unknown architecture: ${arch}"
            return 1
            ;;
    esac
}

set +e

# Install required packages
bash -c "$(curl -sL https://get-gnmic.openconfig.net)"
#bash -c "$(curl -sL https://get-gnoic.kmrd.dev)"
python3 -m pip install --upgrade pip
python3 -m pip install -r .devcontainer/requirements.txt
# Install cEOS-Lab Image
pull_arch_specific_ceos_image