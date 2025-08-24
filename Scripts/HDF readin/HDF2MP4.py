import h5py
import os
import numpy as np
import cv2
import time

#ausgelagert, da die Bildgröße der Dateien schon im vorhinein bekannt war
height = 1024
width = 1360

def mp4Converter(main_folder_path, sub_folder_path, file_name):
    hdf_path = main_folder_path + sub_folder_path + file_name
    #with h5py.File('E:\HiDrive\TSR_2010_10_29\GC1380CH_2010-Oct-29_17_33_46.hdf', 'r') as f:
    with h5py.File(hdf_path, 'r') as f:
        dataset = f['Stream']
        video_array = dataset[:]

    # Define the output directory
    #output_dir = 'C:\\Users\\Haennes\\Desktop\\mp4test\\'
    output_dir = output_main_folder + sub_folder_path

    # Extract the original file name
    #file_name = os.path.basename(f.filename)
    #file_name = "GC1380CH_2010-Oct-29_17_33_46.hdf"
    output_file = os.path.join(output_dir, os.path.splitext(file_name)[0] + '.mp4')

    # Define the video codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Create a VideoWriter object
    out = cv2.VideoWriter(output_file, fourcc, 25.0, (width, height))

    # Write each frame to the output video
    for frame in video_array:
        og = frame[64:]
        final = np.reshape(og, (height, width))
        demosaiced = cv2.cvtColor(final, cv2.COLOR_BayerRG2RGB)

        # Write the frame to the output video file
        out.write(demosaiced)

    # Release the VideoWriter and close the output file
    out.release()

def get_file_names(main_folder_path, sub_folder_path, start_index=0):
    # Überprüfen, ob der angegebene Pfad ein Ordner ist
    folder_path = main_folder_path + sub_folder_path
    if not os.path.isdir(folder_path):
        print("Ungültiger Ordnerpfad.")
        return
    index = 0
    # Durchlaufe alle Dateien im Ordner
    for filename in os.listdir(folder_path):
        # Überprüfen, ob es sich um eine Datei handelt
        if(index >= start_index):
            #if(index >= 120):
                #exit()
            if os.path.isfile(os.path.join(folder_path, filename)):
                mp4Converter(main_folder_path, sub_folder_path, filename)
                print('Die Datei: ', filename, ' wurde erfolgreich umgewandelt!')
                #optional um der CPU kurz Luft zu geben
                time.sleep(3)
                index += 1
                print('continue...')

        else:
            index += 1

# Beispielaufruf der Funktion mit dem Ordnerpfad 'C:\\Users\\Haennes\\Desktop\\'
mainfolder = 'E:\\HiDrive\\'
subfolder = "TSR_2010_11_24\\"
output_main_folder = 'C:\\Users\\Haennes\\Desktop\\MP4s\\'
get_file_names(mainfolder, subfolder, 120)
