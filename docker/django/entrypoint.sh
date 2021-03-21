#!/usr/bin/env sh

set -o errexit
set -o nounset

readonly cmd="$*"

exec $cmd
