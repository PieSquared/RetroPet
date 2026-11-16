# Run this as normal user, not root
set -euo pipefail

REPO_RAW="https://raw.githubusercontent.com/PieSquared/RetroPet/main/Firmware"
INSTALL_DIR="$HOME/retropet"
VENV_DIR="$HOME/petenv"
SERVICE_NAME="retropet"
RUN_USER="$USER"

echo "Installing system packages"
sudo apt update
sudo apt install -y \
    curl python3-full python3-venv \
    python3-gpiozero python3-pil python3-spidev \
    python3-lgpio python3-rpi-lgpio

echo "Enabling SPI"
sudo raspi-config nonint do_spi 0

echo "Adding $RUN_USER to spi and gpio groups"
sudo usermod -aG spi,gpio "$RUN_USER"

echo "making venv at $VENV_DIR"
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv --system-site-packages "$VENV_DIR"
fi
"$VENV_DIR/bin/pip" install --upgrade luma.lcd

echo "Downloading fw to $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"
curl -fL "$REPO_RAW/FW.py" -o "$INSTALL_DIR/FW.py"
curl -fL "$REPO_RAW/sprites.png" -o "$INSTALL_DIR/sprites.png"

echo "creating service"
sudo tee "/etc/systemd/system/$SERVICE_NAME.service" > /dev/null <<EOF
[Unit]
Description=RetroPet desktop pet
After=multi-user.target

[Service]
Type=simple
User=$RUN_USER
WorkingDirectory=$INSTALL_DIR
ExecStart=$VENV_DIR/bin/python $INSTALL_DIR/FW.py
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable "$SERVICE_NAME"

echo "Done. Rebooting..."
sleep 3
sudo reboot
