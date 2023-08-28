from gl import Renderer
import shaders

# Tamaño del FrameBuffer
width = 1000
height = 500

# Crear el renderizador
rend = Renderer(width, height)

#Renderizado de fondo
rend.glBackgroundTexture("background/battlefield.bmp")
rend.glClearBackground()

# Asignar los shaders que se utilizarán
rend.vertexShader = shaders.vertexShader

#threshold_value = 0.5  # Cambia esto al valor de umbral deseado
#rend.fragmentShader = lambda **kwargs: shaders.edgeDetectionFragmentShader(threshold=threshold_value, **kwargs)
rend.fragmentShader = shaders.fragmentShader
# Cargar los modelos que se renderizarán

rend.glLoadModel(filename="objs/torre.obj",
                 textureName="textures/torre.bmp",
                 translate=(420, 70, 0),
                 rotate=(10, -90, 0),
                 scale=(2, 2, 2))
rend.glRender()


rend.fragmentShader = shaders.fragmentShader
rend.glLoadModel(filename="objs/golem.obj",
                 textureName="textures/EarthGolem.bmp",
                 translate=(750, height/10, 0),
                 rotate=(0, -20, 0),
                 scale=(20, 16, 20))
# Renderizar la escena
rend.glRender()

# Asignar el fragment shader: Cambia esto según el shader que desees usar
rend.fragmentShader = shaders.fragmentShader
# Cargar los modelos que se renderizarán

rend.glLoadModel(filename="objs/dragon.obj",
                 textureName="textures/modelD.bmp",
                 translate=(600, 200, 0),
                 rotate=(0, 90, 70),
                 scale=(2, 2, 2))

# Renderizar la escena
rend.glRender()

rend.fragmentShader = shaders.fragmentShader
# Cargar los modelos que se renderizarán
rend.glLoadModel(filename="objs/knight.obj",
                 textureName="textures/armor.bmp",
                 translate=(250, -120, 0),
                 rotate=(0, 150, 0),
                 scale=(200, 200, 200))

# Renderizar la escena
rend.glRender()


# Crear el FrameBuffer con la escena renderizada
rend.glFinish("RASTERIZER_NO_SHADERS.bmp")
