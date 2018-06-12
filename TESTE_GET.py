#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:51:23 2018

@author: pedrohames
"""

import requests
from PIL import Image
import io
r = requests.get('https://wiki.sj.ifsc.edu.br/wiki/images/b/b9/PTC-20162-Fsm-rcv.jpg')

Image.open(io.BytesIO(r.content)).show()
