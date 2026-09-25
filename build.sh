#!/bin/bash
set -e

case "${1:-}" in
  --clean)
    jupyter-book clean --html book
    ;;
  "")
    ;;
  *)
    echo "Usage: $0 [--clean]" >&2
    exit 1
    ;;
esac

find . -name '*.ipynb' -exec nbstripout {} +
jupyter-book build book
