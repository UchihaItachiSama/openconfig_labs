# Labs

- [Labs](#labs)
  - [Deploying Labs](#deploying-labs)
    - [Requirements](#requirements)
  - [Arista cEOS-Lab](#arista-ceos-lab)
    - [Installing Arista cEOS-Lab image](#installing-arista-ceos-lab-image)
    - [Installing client image](#installing-client-image)
  - [Multi-vendor Lab](#multi-vendor-lab)
    - [Installing Nokia SR Linux image](#installing-nokia-sr-linux-image)

## Deploying Labs

It's advised to deploy the labs using below options, as it takes care of installing required images, tools and packages:

- Codespaces -- [Click here to deploy](https://codespaces.new/UchihaItachiSama/openconfig_labs/tree/update-labs?quickstart=1&devcontainer_path=.devcontainer%2Fdocker-in-docker%2Fdevcontainer.json)
- Devpod
  - Docker outside of Docker -- [Click here to deploy](https://devpod.sh/open#https://github.com/UchihaItachiSama/openconfig_labs/tree/update-labs)
  - Docker in Docker -- [Click here to deploy](https://devpod.sh/open#https://github.com/UchihaItachiSama/openconfig_labs/blob/update-labs/.devcontainer/docker-in-docker/devcontainer.json)

**NOTE:** *If deploying manually then refer to respective lab sections for steps to install images. To know more about containerlab in codespaces go [here](https://containerlab.dev/manual/codespaces/), for devpod go [here](https://containerlab.dev/macos/#devpod)*

### Requirements

- For Devpod need to have [docker](https://docs.docker.com/get-started/get-docker/) and [Devpod](https://devpod.sh/docs/getting-started/install) installed on host
- For codespaces need to have GitHub [account](https://github.com/signup) with [codespaces](https://github.com/features/codespaces) access
- [Arista account](https://www.arista.com/) with ability to download cEOS-lab via [Software downloads](https://www.arista.com/en/support/software-download)
- Arista user [token](https://www.arista.com/en/users/profile)
  - This is required for both Devpod or codespaces deployment.
  - For codespaces user will be prompted to enter token when starting the lab
  - For Devpod use `echo 'export ARTOKEN=token-value' >> ~/.zshenv` on your host

## Arista cEOS-Lab

<img src="../images/ceos-lab.png" width=450 height=350>

**NOTE:** *Clients are disabled by default, to use clients uncomment the lines from [topology.yml](../labs/arista-ceos/topology.clab.yml)*

### Installing Arista cEOS-Lab image

- Download the image from [www.arista.com](https://www.arista.com) > Software Downloads > cEOS-Lab > EOS-4.2x.y > cEOS-lab-4.2x.y.tar.xz
- Copy the cEOS-lab-4.2x.y.tar.xz to the host/server/VM.
- Next, use the tar file to import the cEOS-Lab image using the following command

```shell
docker import cEOS64-lab-4.26.1F.tar.xz arista/ceos:4.26.1F
```

- Now you should be able to see the Arista cEOS-Lab image.

```shell
docker images | egrep "REPO|ceos"
```

Use the [topology.clab.yml](../labs/arista-ceos/topology.clab.yml) file to deploy the Arista cEOS-Lab using [containerlab](https://containerlab.dev/cmd/deploy/) `clab deploy` command or use the vscode containerlab extension.

### Installing client image

Use the following steps to build the client image

```shell
cd alpine_host
docker build -t alpine-host .
```

## Multi-vendor Lab

<img src="../images/ceos-srl-lab.png" width=700 height=250>

Install Arista cEOS-Lab image using steps mentioned [above](#installing-arista-ceos-lab-image).

### Installing Nokia SR Linux image

```shell
docker pull ghcr.io/nokia/srlinux:25.3.2
```

Use the [topology.clab.yml](../labs/multi-vendor/topology.clab.yml) file to deploy the lab using [containerlab](https://containerlab.dev/cmd/deploy/) `clab deploy` command or use the vscode containerlab extension.
