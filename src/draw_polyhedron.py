"""
2-17. 多面体描画のコード
"""

import numpy as np
from vpython import *


from vertex_enumeration import *

# vpython初期設定
scene = canvas(width = 800, height = 600)
vmin = np.min(vlist) - 0.5
length = np.max(vlist) - vmin + 0.5

scene.up = vector(0, 0, 1)
scene.forward = vector(-1, -1, -1)
scene.center = vector(0, 0, 0)
scene.range = 0.9 * length
scene.background = color.white

cb = color.black

# x,y,z軸を描画
arrow(pos=vector(vmin,0,0), axis=vector(length,0,0),
      shaftwidth=0.002, headwidth=0.05, color=cb)
arrow(pos=vector(0,vmin,0), axis=vector(0,length,0),
      shaftwidth=0.002, headwidth=0.05, color=cb)
arrow(post=vector(0,0,vmin), axis=vector(0,0,length),
      shaftwidth=0.002, headwidth=0.05, color=cb)

# 頂点と稜線を描画
vertices = [sphere(pos=vector(*v),
                radius=0.01, color=cb) for v in vlist]
edges = [curve(pos=[vector(*vlist[i]), vector(*vlist[j])],
               radius=0.007, color=cb) for [i,j] in elist]
