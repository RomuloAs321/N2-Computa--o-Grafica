import pywavefront
from OpenGL.GL import *
import numpy as np

# Classe para carregar o arquivo
class Mesh:
    def __init__(self, obj_file):
        try:
            self.mesh = pywavefront.Wavefront(obj_file, collect_faces=True, create_materials=True)
            self.compute_normals()
        except Exception as e:
            print(f"Erro ao carregar o arquivo {obj_file}: {e}")
            self.mesh = None

    def compute_normals(self):
       # Calcula as normais dos vértices se não estiverem presentes.
        self.normals = {}
        for name, mesh in self.mesh.meshes.items():
            for face in mesh.faces:
                v0 = self.mesh.vertices[face[0]]
                v1 = self.mesh.vertices[face[1]]
                v2 = self.mesh.vertices[face[2]]
                normal = np.cross(np.subtract(v1, v0), np.subtract(v2, v0))
                normal = normal / np.linalg.norm(normal)
                for vertex_i in face:
                    if vertex_i in self.normals:
                        self.normals[vertex_i] += normal
                    else:
                        self.normals[vertex_i] = normal

        # Normaliza todas as normais dos vértices
        for vertex_i in self.normals:
            self.normals[vertex_i] = self.normals[vertex_i] / np.linalg.norm(self.normals[vertex_i])

    def draw(self):
        if self.mesh:
            glBegin(GL_TRIANGLES)
            for name, mesh in self.mesh.meshes.items():
                for face in mesh.faces:
                    for vertex_i in face:
                        glNormal3fv(self.normals[vertex_i])
                        glVertex3fv(self.mesh.vertices[vertex_i])
            glEnd()