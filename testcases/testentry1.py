import random
import time
import pytest

from testcases.conftest import setup
from utilities.BaseClass import BaseClass


class Testyoutube():
    @pytest.mark.usefixtures("setup")
    def test_tube(self):
        links=['https://www.youtube.com/watch?v=yHTSEyppoME','https://www.youtube.com/watch?v=DQmsglqVKps','https://www.youtube.com/watch?v=6v5vLc7P98k']

        for i in range(5):
            self.driver.get(links[random.randint(0,len(links))-1])
            t=random.randint(20,40) #video play time 20 seconds to 40 seconds
            print(t)
            time.sleep(30)

        self.driver.quit()

# clss=Testyoutube()
# clss.test_tube()



