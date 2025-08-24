import h5py
import numpy as np

#with h5py.File('pfad/zur/datei.hdf', 'r') as file:
    #video_array = file['name_des_videos'][:]
#with h5py.File('E:\HiDrive\TSR_2010_11_24\GC1380CH_2010-Nov-24_10_33_47.hdf', 'r') as f:   #hier sind 137 Dinger in
#with h5py.File('E:\HiDrive\TSR_2010_10_11\GC1380CH_2010-Oct-11_11_16_37.hdf', 'r') as f:
with h5py.File('E:\HiDrive\TSR_2010_10_29\GC1380CH_2010-Oct-29_17_33_46.hdf', 'r') as f:
    dataset = f['Stream']
    video_array = dataset[:]
import cv2

# Einstellen der Fenstergröße
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', 1360, 1024)

# Schleife über jedes Frame im Video
for frame in video_array:

    og = frame[64:]
    #print(len(og))

    final = np.reshape(og, (1024, 1360))
    #print(final[0:30])
    #og
    demosaicing = cv2.cvtColor(final, cv2.COLOR_BayerRG2RGB)
    #selbes ergebnis
    #demosaicing2 = cv2.cvtColor(final, cv2.COLOR_BayerBG2BGR)

    print(demosaicing)
    #print(demosaicing[0:30])
    cv2.imshow('Video', demosaicing)

    # Anzeigen des Frames
    #cv2.imshow('Video', test)
    #cv2.imshow('Video', frame[:len(frame)-64])
    #1392704   sind es
    #1392640   sind es actually
    #entspricht 64 werte zu viel

    # Warten auf das Drücken einer Taste, um zum nächsten Frame zu gehen
    if cv2.waitKey(250) & 0xFF == ord('q'):
        continue



# Schließen des Fensters und Freigabe des Videospeichers
cv2.destroyAllWindows()
