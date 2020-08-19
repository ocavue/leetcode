#!/usr/bin/env bash

set -euo pipefail

cd $(dirname $0)

Number=$1

go test . -v -count 1 -run "^Test$Number$"
