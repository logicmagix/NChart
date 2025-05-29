#!/usr/bin/env bash


INSTALL_DIR="$HOME/.local/share/nchart"
BIN_DIR="$HOME/.local/bin"
WRAPPER="$BIN_DIR/nchart"


# Ensure target directories exist
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"


# Copy project files into the install dir
cp -r nchart "$INSTALL_DIR"


# Create the wrapper script
cat << 'EOF' > "$WRAPPER"
#!/usr/bin/env bash
PYTHONPATH="$HOME/.local/share/nchart" python3 -m nchart.nchart "$@"
EOF


# Make the wrapper executable
chmod +x "$WRAPPER"


# Notify the user
echo "[+] nchart installed to: $WRAPPER"
echo "[+] Make sure ~/.local/bin is in your PATH"


