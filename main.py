
from utils.gl_color import color
from utils.gl_math import V2, V3
from gl import Raytracer
from obj import Obj, Texture
from sphere import Sphere, Material
import random

width = 600
height = 400


snow = Material(diffuse=color(1,1,1))
button = Material(diffuse=color(0,0,0))
mouth= Material(diffuse=(color(0.5,0.5,0.5)))
nose = Material(diffuse=(color(1,0.65,0)))


r = Raytracer(width,height)
r.scene.append( Sphere(V3(0, -3.1, -10), 2.3, snow) )
r.scene.append( Sphere(V3(0, 0,  -10), 1.8, snow) )
r.scene.append( Sphere(V3(0, 2.9, -10), 1.3, snow) )


r.scene.append( Sphere(V3(0, 2.15, -8), 0.24, nose) )

r.scene.append( Sphere(V3(0.43, 1.8, -8), 0.1, mouth) )
r.scene.append( Sphere(V3(0.15, 1.6, -8), 0.1, mouth) )
r.scene.append( Sphere(V3(-0.15, 1.6, -8), 0.1, mouth) )
r.scene.append( Sphere(V3(-0.43, 1.8, -8), 0.1, mouth) )

r.scene.append( Sphere(V3(0.40, 2.5, -8), 0.12, button) )
r.scene.append( Sphere(V3(-0.40, 2.5, -8), 0.12, button) )

r.scene.append( Sphere(V3(0, 0.5, -6), 0.26, button) )
r.scene.append( Sphere(V3(0, -0.8, -6), 0.4, button) )
r.scene.append( Sphere(V3(0, -2.2, -6), 0.6, button) )








r.rtRender()

r.glFinish('output.bmp')






