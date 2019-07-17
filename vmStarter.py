import time
from pywinauto.application import Application
import config

def main():
        # Run a target application
        app = Application().start(config.VMPLAYER_PATH)
        dlg = app.window(title_re='VMware Workstation*')

        # wait till the window is really open
        dlg.wait('visible')
                
        # Search for VM to start
        time.sleep(2)
        for i in dlg.ListView.items():
                if (i.text() == config.VM_NAME_TO_START):
                        i.click()        
                        break
        
        time.sleep(1)
        # Set User and Password
        dlg.Edit2.set_edit_text(config.VM_USERNAME)
        dlg.Edit3.set_edit_text(config.VM_PASSWORD)
        dlg.Button14.click()

        time.sleep(5)

        playButton = dlg.window(best_match = 'Play virtual machine')
        playButton.click()

if __name__ == '__main__':
    main()