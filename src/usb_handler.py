# src/usb_handler.py

import usb.core
import usb.util
import logging


class USBHandler:
    def __init__(self, device_id):
        self.device = usb.core.find(
            idVendor=device_id['vendor_id'], idProduct=device_id['product_id'])
        if self.device is None:
            raise ValueError("Device not found")

        # Устанавливаем активную конфигурацию
        self.device.set_configuration()

    def send_command(self, command):
        try:
            # Пример отправки команды на принтер через USB
            logging.info(f"Sending command: {command}")
            # Здесь следует описать логику отправки команды
            # Например, используем endpoint
            self.device.write(1, command)

            # Получаем ответ от устройства
            response = self.device.read(0x81, 64)
            logging.info(f"Received response: {response}")
            return response
        except usb.core.USBError as e:
            logging.error(f"USB Error: {str(e)}")
            return None
