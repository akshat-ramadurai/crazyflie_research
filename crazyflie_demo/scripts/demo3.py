#!/usr/bin/env python
from demo import Demo

if __name__ == '__main__':
    demo = Demo(
        [
            #x   ,   y,   z, yaw, sleep
            [0.0 , 0.0, 0.5, 0, 2],
            [0.0 , 0.0, 0.55, 0, 2],
            [0.0 , 0.0, 0.5, 0, 2],
            [0.0 , 0.0, 0.55, 0, 2],
            [0.0 , 0.0, 0.5, 0, 0],
        ]
    )
    demo.run()
