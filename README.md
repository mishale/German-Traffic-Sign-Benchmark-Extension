# German Traffic Sign Benchmark Extension

This project was developed as part of the **Media Technology Bachelor program**.  
The main goal was to **extend the German Traffic Sign Recognition Benchmark (GTSRB)** by introducing a new class of *traffic sign lookalikes* (false positives), making the dataset more challenging for deep learning models.

## Project Overview
Traditional CNNs already achieve nearly **100% accuracy** on GTSRB. To challenge modern models, we designed a workflow that:
- Processes raw **HDF5 video data** and converts it into usable MP4 files.
- Implements multiple approaches for **traffic sign detection**:
  - A custom CNN detector.
  - A Positive/Negative CNN classifier (traffic sign vs. non-traffic sign).
  - Exploration of YOLO-based object detection.
- Creates a **new dataset class** of traffic sign-like structures that confuse CNNs.

## Features
- **HDF5 Processing**  
  - Reading raw datasets (`h5py`, `numpy`, `cv2`).  
  - Preprocessing & demosaicing Bayer-RG frames.  
  - Exporting to MP4 for visualization.  

- **Traffic Sign Detection Models**  
  - **Detection CNN** (bounding box regression, later replaced).  
  - **Positive-Negative CNN** (binary classification, effective on video frames).  
  - **YOLO exploration** for future improvements.  

- **New Dataset Class**  
  - Positive class: red-bordered traffic signs (triangles, circles).  
  - Negative class: false positives extracted from GTSDB frames.  

## Tech Stack
- **Languages**: Python  
- **Libraries**: PyTorch, NumPy, Pandas, OpenCV, Matplotlib, Scikit-Learn, PIL  
- **Tools**: Jupyter Notebook, Visual Studio Code, Panoply, LaTeX  

## Results
- Positive-Negative CNN achieved reliable classification results on video frames.
- Sliding-window approach enabled detection of traffic sign-like patterns in videos.
- Prepared scripts for YOLO (TFRecord conversion) to enable future improvements.

## License
This repository is for **educational and research purposes only**.
