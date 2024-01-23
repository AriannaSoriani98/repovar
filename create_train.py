import os
import random
import shutil
from zipfile import ZipFile

def random_sampling(input_folder, output_folder, num_samples=500):
    # Elenco di tutti i file nella cartella di input
    all_files = os.listdir(input_folder)

    # Esegui il sampling casuale di num_samples file
    selected_files = random.sample(all_files, min(num_samples, len(all_files)))

    # Crea la cartella di output se non esiste
    os.makedirs(output_folder, exist_ok=True)

    # Copia i file selezionati nella cartella di output
    for file in selected_files:
        source_path = os.path.join(input_folder, file)
        destination_path = os.path.join(output_folder, file)
        shutil.copy2(source_path, destination_path)

    # Crea un file zip con i file copiati
    zip_filename = os.path.join(output_folder, output_folder +'.zip')
    with ZipFile(zip_filename, 'w') as zip_file:
        for file in selected_files:
            file_path = os.path.join(output_folder, file)
            zip_file.write(file_path, os.path.basename(file_path))

# Esempio di utilizzo
lettera='del'
input_folder = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\progetto\asl_alphabet_train\asl_alphabet_train\\'+lettera
output_folder = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\progettogit\\' +lettera

random_sampling(input_folder, output_folder, num_samples=500)
