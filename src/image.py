from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin = Image()
        
        # affectation a l'image im_bin d'un tableau de pixels de meme taille
        # que self dont les intensites, de type uint8 (8bits non signes),
        # sont mises a 0
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        
        mask = self.pixels > S
        np.putmask(im_bin.pixels, mask == True , 255)
        np.putmask(im_bin.pixels, mask == False, 0)
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):   
        l_min = self.H
        l_max = 0
                
        c_min = self.W
        c_max = 0
        
        for i in range(self.H):
            for j in range(self.W):
                if self.pixels[i][j] == 0:
                   
                    if j < c_min:
                        c_min = j

                    if j > c_max:
                        c_max = j
                        
                    if i < l_min:
                        l_min = i
                        
                    if i > l_max:
                        l_max = i
                        
        img_cropped = Image()
        img_cropped.set_pixels(self.pixels[l_min:l_max,c_min:c_max])
        return img_cropped
    
        
            

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        img_resized = Image()
        pixel_resized = resize(self.pixels, (new_H, new_W), 0)
        img_resized.set_pixels(np.uint8(pixel_resized*255))
        
        return img_resized
        


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        resized1 =  self.resize(im.H, im.W)
        correlations = resized1.pixels == im.pixels 
        pixels_similaires = 0
        for i in range(im.H):
            for j in range(im.W):
                if correlations[i][j] == True :
                    pixels_similaires += 1
        print(f"{pixels_similaires} {(im.H * im.W)}")
        return pixels_similaires / ( im.H * im.W )
                
        
        
        
        
        
        


