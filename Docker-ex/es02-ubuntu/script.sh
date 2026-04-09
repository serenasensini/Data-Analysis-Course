#!/usr/bin/env bash

# Explain the purpose of the script commenting line by line
set -e

APP_NAME="myapp"
APP_VERSION="1.0.0"
SRC_DIR="./build"
TARGET_DIR="/opt/$APP_NAME"
BIN_NAME="myapp.sh"

echo "Installazione di $APP_NAME versione $APP_VERSION"

sudo mkdir -p "$TARGET_DIR"

sudo cp -r "$SRC_DIR/"* "$TARGET_DIR/"

if [ -f "$TARGET_DIR/config.example.json" ]; then
  sudo mv "$TARGET_DIR/config.example.json" "$TARGET_DIR/config.json"
fi

sudo chmod +x "$TARGET_DIR/$BIN_NAME"

sudo chmod 600 "$TARGET_DIR/config.json" || true

sudo ln -sf "$TARGET_DIR/$BIN_NAME" /usr/local/bin/$APP_NAME

export APP_HOME="$TARGET_DIR"
export PATH="$TARGET_DIR:$PATH"

echo "APP_HOME=$APP_HOME"
echo "Installazione completata"
