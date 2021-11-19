from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    im_bin = image.binarisation(S)
    im_loc = im_bin.localisation()
    im_loc.display("test")
    
    sim_max = 0
    indice_sim = 0
    
    for i in range(len(liste_modeles)):
        modele = liste_modeles[i]
        im_resized = im_loc.resize(modele.H, modele.W)
        sim = im_resized.similitude(modele)
        print(f"modele : {i}   similitude : {sim}")
        if sim > sim_max:
            sim_max = sim
            indice_sim = i
        
    liste_modeles[indice_sim].display("sim")
    
    print(f"MODELE : {indice_sim}   SIM : {sim_max}")
    
    return indice_sim

