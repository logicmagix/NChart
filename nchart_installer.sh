#!/bin/bash

# Set target install path
INSTALL_PATH="$HOME/.local/bin/nchart"

# Copy or symlink the script without extension
cp nchart.py "$INSTALL_PATH"

# Rename to remove .py
mv "$INSTALL_PATH" "${INSTALL_PATH/.py/}"

# Make executable
chmod +x "${INSTALL_PATH/.py/}"

echo "nchart installed to ~/.local/bin. Run it with: nchart"
