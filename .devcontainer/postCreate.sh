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

install_images() {
    #Pull cEOS-Lab image
    pull_arch_specific_ceos_image
    
    #Pull srlinux image
    docker pull ghcr.io/nokia/srlinux:25.3.2
    
    #Build client image
    (
        cd alpine_host || exit 1
        docker build -t alpine-host .
    )
    
    #Pull gnmic image
    docker pull ghcr.io/openconfig/gnmic:latest
}

install_packages() {
    #Install gnmic
    bash -c "$(curl -sL https://get-gnmic.openconfig.net)"
    
    #Install gnoic
    #bash -c "$(curl -sL https://get-gnoic.kmrd.dev)"
    
    #Upgrade pip and install requirements
    python3 -m pip install --upgrade pip
    python3 -m pip install -r .devcontainer/requirements.txt
}

set +e

install_packages
install_images
