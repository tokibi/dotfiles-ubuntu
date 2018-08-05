#!/bin/bash

MITAMAE_PATH="/usr/local/bin/mitamae"
MITAMAE_URI="https://github.com/itamae-kitchen/mitamae/releases/download/v1.6.2/mitamae-x86_64-linux"

if [ "$(whoami)" != "root" ]; then
  echo "Require root privilege"
  exit 1
fi

if ! which mitamae &> /dev/null; then
  wget $MITAMAE_URI -O $MITAMAE_PATH
  chmod +x $MITAMAE_PATH
fi

mitamae local ./recipe.rb --node-json node.json
