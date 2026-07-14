This page is designed to get you up and running with building this repository.

# Initial Setup

Ubuntu 20.04 is the preferred platform of choice, with you running it either:
- Natively
- Via WSL
- Via Docker

Other Linux distros are untested, as is attempting to compile via MSYS2.

## Installing Prerequisites

If you wish to use Docker, then follow the [guide](https://docs.docker.com/engine/install/ubuntu/) to installing Docker. Otherwise you can install the prerequisites natively.

The most up-to-date source for the prerequisites is the [Dockerfile](https://github.com/mkst/conker/blob/master/Dockerfile) but at the time of the writing, the following 3 commands will install necessary tools and libraries:

```sh
sudo apt-get update

sudo apt-get install -y \
    binutils-mips-linux-gnu \
    build-essential \
    less \
    libglib2.0 \
    python3 \
    python3-pip \
    unzip \
    wget

python3 -m pip install \
    capstone pyyaml pycparser \
    colorama ansiwrap watchdog python-Levenshtein cxxfilt \
    python-ranges \
    pypng
```

## Using Docker

You can build the Docker image yourself via

```sh
docker build . -t conker
```

Or you can use the pre-built image `markstreet/conker:latest`

After cloning the repo, simply spin up the image, mounting the conker directory as `/conker`:

```sh
docker run --rm -ti -v $(pwd)/conker:/conker markstreet/conker:latest
```

# Building the ROM

First we need to extract the code and assets from the ROM, this is done via the `make extract` recipe:

```sh
make extract
```

You can then simply run `make` to compile the ROM; a successful build will create `build/conker.us.z64`

```sh
make
```

## Game logic

If you wish to modify the code (and/or work on the decompilation effort) you can extract this section via `make extract` recipe inside the `conker/` directory:

Navigate inside `conker/`:

```sh
cd conker/
```

Extract the (assembly) code out of the `game.VERSION.bin` file:

```sh
make extract
```

Compile it:

```sh
make --jobs # run as many concurrent jobs as possible
```

Replace the extracted `game.VERSION.bin` with the newly compiled section:
```sh
make replace
```

You will then need to run `make` from the base of the repository to include this updated `game.bin` in the `build/conker.us.z64` ROM.