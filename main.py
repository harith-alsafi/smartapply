from src.gui.MainInterface import MainInterface
import sys

if __name__ == "__main__":
    api_key:str = sys.argv[1]
    main_interface = MainInterface(api_key)
    main_interface.start()
    main_interface.main_interface()
