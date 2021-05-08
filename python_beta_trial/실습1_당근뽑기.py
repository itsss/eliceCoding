# 당근 마을을 만드는 코드예요. 이 코드는 수정하지 마세요!
from elicerabbits import *
import time as _time
load_world("worlds/harvest1.wld")
rabbit = Rabbit()
rabbit.set_trace('blue')
rabbit.set_pause(0.3)
_time.sleep(0.3)

# 토끼가 당근을 수확할 수 있도록 아래에 코드를 써주세요!

rabbit.move()
rabbit.pick_carrot()


