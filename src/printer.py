# src/printer.py

import logging
from usb_handler import USBHandler


class Printer:
    def __init__(self, usb_device, config):
        self.usb = USBHandler(usb_device)
        self.config = config

    def reset_waste_ink_levels(self, dry_run=False):
        logging.info("Starting waste ink reset via USB...")

        if dry_run:
            logging.info(
                "Dry run mode activated, no real actions will be taken.")
            return True

        # Отправляем команды на сброс уровня чернил через USB
        reset_command = self.config['reset_command']
        response = self.usb.send_command(reset_command)

        if response:
            logging.info("Waste ink levels successfully reset.")
            return True
        else:
            logging.error("Failed to reset waste ink levels.")
            return False
