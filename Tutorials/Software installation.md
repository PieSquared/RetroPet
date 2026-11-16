## Requirements

Before setting up Retro Pets, make sure you have the following:

| Requirement | Description |
|---|---|
| Internet Connection | Required to download software and complete setup. |
| MicroSD Card (8GB minimum) | Used to store the Raspberry Pi operating system and Retro Pets software. |
| Computer | Required to prepare the MicroSD card and configure the Raspberry Pi. |
| MicroSD Card Adapter | Used to connect the MicroSD card to your computer. |

# Install the OS

1. Download and install [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
2. Insert your MicroSD card into your computer using the adapter.
3. Open Raspberry Pi Imager, select **Raspberry Pi OS**, and follow the setup instructions.
4. During configuration, make sure to enable **Raspberry Pi Connect** and **SSH**.
5. Once the installation is complete, insert the MicroSD card into your Raspberry Pi and power it on.
6. Log in to [Raspberry Pi Connect](https://connect.raspberrypi.com/) and open the SSH terminal.
7. Run the following command:

```bash
curl -fsSL https://raw.githubusercontent.com/PieSquared/RetroPet/main/setup.sh | bash
```

Note: Make sure your Raspberry Pi is connected to the internet before running the command.

8. Wait for the installation to finish.

Done! Your Retro Pets software should now be installed after it reboots
