#!/bin/bash

INSTALL_DIR="$HOME/.local/share/nchart"
BIN_DIR="$HOME/.local/bin"
WRAPPER="$BIN_DIR/nchart"
mkdir -p "$INSTALL_DIR"
cp -r src/nchart "$INSTALL_DIR"
mkdir -p "$BIN_DIR"
cat << EOF > "$WRAPPER"
#!/usr/bin/env bash
python3 -m nchart.nchart
EOF
chmod u+x "$WRAPPER"
echo "nchart installed to $WRAPPER"
echo "Make sure ~/.local/bin is in your PATH."
