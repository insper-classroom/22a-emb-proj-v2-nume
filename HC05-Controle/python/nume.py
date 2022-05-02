import pyautogui
import serial
import argparse
import time
import logging

class MyControllerMap:
    def __init__(self):
        self.button = {'1': '1'} # Fast forward (10 seg) pro Youtube

class SerialControllerInterface:
    # Protocolo
    # byte 1 -> Botão 1 (estado - Apertado 1 ou não 0)
    # byte 2 -> EOP - End of Packet -> valor reservado 'X'

    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate=baudrate)
        self.mapping = MyControllerMap()
        self.incoming = '0'
        pyautogui.PAUSE = 0  ## remove delay
    
    def update(self):
        ## Sync protocol
        while self.incoming != b'X':
            self.incoming = self.ser.read()
            logging.debug("Received INCOMING: {}".format(self.incoming))

        head = self.ser.read()
        logging.debug("Received HEAD: {}".format(head))

        if head == b'K':
            data = self.ser.read()
            logging.debug("Received DATA: {}".format(data))

            if data == b'1':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('1')
                pyautogui.keyUp('1')

            elif data == b'2':
                logging.info("KEYDOWN 2")
                pyautogui.keyDown('2')
                pyautogui.keyUp('2')

            elif data == b'3':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('3')
                pyautogui.keyUp('3')

            elif data == b'4':
                logging.info("KEYDOWN 4")
                pyautogui.keyDown('4')
                pyautogui.keyUp('4')

            elif data == b'5':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('5')
                pyautogui.keyUp('5')

            elif data == b'6':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('6')
                pyautogui.keyUp('6')

            elif data == b'7':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('7')
                pyautogui.keyUp('7')

            elif data == b'8':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('8')
                pyautogui.keyUp('8')

            elif data == b'9':
                logging.info("KEYDOWN 9")
                pyautogui.keyDown('9')
                pyautogui.keyUp('9')

            elif data == b'0':
                logging.info("KEYDOWN 0")
                pyautogui.keyDown('0')
                pyautogui.keyUp('0')

            elif data == b'A':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('A')
                pyautogui.keyUp('A')

            elif data == b'B':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('B')
                pyautogui.keyUp('1')

            elif data == b'C':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('C')
                pyautogui.keyUp('C')

            elif data == b'D':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('D')
                pyautogui.keyUp('D')

            elif data == b'*':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('*')
                pyautogui.keyUp('*')

            elif data == b'#':
                logging.info("KEYDOWN 1")
                pyautogui.keyDown('#')
                pyautogui.keyUp('#')

        if head == b'V':
            data = self.ser.read() 
            volume = int.from_bytes(data, 'big')

            print(volume)

        self.incoming = self.ser.read()


class DummyControllerInterface:
    def __init__(self):
        self.mapping = MyControllerMap()

    def update(self):
        pyautogui.keyDown(self.mapping.button['A'])
        time.sleep(0.1)
        pyautogui.keyUp(self.mapping.button['A'])
        logging.info("[Dummy] Pressed A button")
        time.sleep(1)


if __name__ == '__main__':
    interfaces = ['dummy', 'serial']
    argparse = argparse.ArgumentParser()
    argparse.add_argument('serial_port', type=str)
    argparse.add_argument('-b', '--baudrate', type=int, default=9600)
    argparse.add_argument('-c', '--controller_interface', type=str, default='serial', choices=interfaces)
    argparse.add_argument('-d', '--debug', default=False, action='store_true')
    args = argparse.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    print("Connection to {} using {} interface ({})".format(args.serial_port, args.controller_interface, args.baudrate))
    if args.controller_interface == 'dummy':
        controller = DummyControllerInterface()
    else:
        controller = SerialControllerInterface(port=args.serial_port, baudrate=args.baudrate)

    while True:
        controller.update()
