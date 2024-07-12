import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Mesh import Mesh

# Inicializa o Pygame
pygame.init()

# Configurações da janela
screen_width = 1200
screen_height = 900
background_color = (0, 0, 0, 1)

# Configurações da janela do Pygame e OpenGL
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

# Caminho  para o arquivo .obj
obj_file_path = r'C:\Temp\N2-Computação Grafica\Pentagrama\Pentagrammic_prism_v1.obj'
mesh = Mesh(obj_file_path)

# Variáveis de transformação
translate_x, translate_y, translate_z = 0, 0, -5
rotate_x, rotate_y, rotate_z = 0, 0, 0
scale_x, scale_y, scale_z = 0.10, 0.10, 0.10

def initialise():
    glClearColor(0.75, 0.75, 0.75, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    # Configura a posição da luz
    light_position = [10, 10, 10, 1]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    
    # Configura as propriedades da luz
    light_ambient = [0.1, 0.1, 0.1, 1.0]
    light_diffuse = [0.8, 0.8, 0.8, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    
    # Configura as propriedades do material
    material_specular = [1.0, 1.0, 1.0, 1.0]
    material_shininess = [50.0]
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(translate_x, translate_y, translate_z)
    glViewport(0, 0, screen.get_width(), screen.get_height())

def display():
    global rotate_x, rotate_y, rotate_z
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    
    # Aplicar transformações de rotação contínua
    rotate_x += 5.0  
    rotate_y += 5.0
    rotate_z += 5.0
    
    glTranslatef(translate_x, translate_y, translate_z)
    glRotatef(rotate_x, 1, 0, 0)
    glRotatef(rotate_y, 0, 1, 0)
    glRotatef(rotate_z, 0, 0, 1)
    glScalef(scale_x, scale_y, scale_z)
    
    # Definir a cor do modelo 3D
    glColor4f(1.0, 1.0, 0.0, 1.0)
    mesh.draw()
    
    glPopMatrix()

 # Inicializa o loop
initialise()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    display()
    pygame.display.flip()
    pygame.time.wait(10)
