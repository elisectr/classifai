# dataset_management.py
import os
import random
from typing import List

# Chemin vers le dossier contenant les images
dataset_path = "./dataset"

# Fonction pour lire les images du dataset et en sélectionner 20
def get_random_images(num_images: int = 20) -> List[str]:
    try:
        # Lister les fichiers dans le dossier et filtrer les images jpg
        images = [f for f in os.listdir(dataset_path) if f.lower().endswith(('.jpg', '.jpeg'))]
        
        # Vérifier qu'il y a assez d'images dans le dataset
        if len(images) < num_images:
            raise ValueError("Le dataset ne contient pas assez d'images.")
        
        # Sélectionner aléatoirement le nombre d'images souhaité
        selected_images = random.sample(images, num_images)
        return selected_images
    except FileNotFoundError:
        raise FileNotFoundError("Le dossier du dataset est introuvable. Veuillez vérifier le chemin.")

# Exemple d'utilisation
if __name__ == "__main__":
    images = get_random_images()
    print(images)