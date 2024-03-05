from time import time
"""Used to create Cooldowns/Timers in game dev settings. Classes methods are designed to run in a GUI loop."""
class Cooldown:
    def __init__(self, CooldownLength: float, Name: str = None):
        self.CooldownLength = CooldownLength
        self.Name = Name
        self.CooldownStartTime = None
        self.ACTIVE = False
        
    """Starts cooldown."""    
    def startCD(self):
        self.CooldownStartTime = time()
        self.ACTIVE = True
    
    """Checks if cooldown is ongoing. Returns True if cooldown is ongoing, False otherwise."""
    def checkCD(self):
        if self.ACTIVE:
            timeElapsed = time() - self.CooldownStartTime
            if timeElapsed > self.CooldownLength:
                self.ACTIVE = False
                return False
            else: return True
        else: return False

'Use-Case Example Below:'
'''
cd = Cooldown(3)
while True:
    if cd.checkCD() == False:
        cd.startCD()
        print('CD Not Active')
        sleep(1)
    else: 
        print('CD Is Now Active :)')
        sleep(1)
'''