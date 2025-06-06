# Perspective transformation

This repository explores practical use of perspective transformations in computer vision. We focus on three applications: correcting document images to make them look like scanned copies, generating aerial (bird's eye) views from regular photos, and creatively changing viewpoints in artworks. For example, in document correction, the aim is to turn a photo of a paper or ID card taken at an angle into a clean, front-facing image. In aerial view generation, perspective transformation helps convert side view photos into top-down views, which is useful in areas like traffic analysis, sports, and urban planning. We also explore how changing perspectives can give new artistic interpretations to classic images.


## 🔧 Technical Pipeline (General for All):

Detect four points (source points)  automatically.


Define destination points based on the desired output view.


Compute the perspective transformation matrix using OpenCV’s getPerspectiveTransform().


Apply the transformation with warpPerspective().


Display and save the result.


## ▶️ How to Run

### 1. Clone the repository

git clone https://github.com/Filsduvent/Persperctive_transformation.git

cd Perspective_transformation

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the pipeline

python main.py

This command starts an interactive menu in the terminal, where the user can choose which operation to perform among the three available options: Document Perspective Correction, Aerial View Simulation, and Artistic Point of View Change. The program will continue to run until the user selects the option to exit.


## 📸 Results

The results are organized into three subsections, each corresponding to one of the use cases developed in this project:

Document Perspective Correction
Aerial View Simulation
Artistic Point of View Change

The images below represent for each use case examples of input images, its corresponding showing contours drawn and their corresponding transformed output.

## Document perspective Correction
<p align="center">
  <img src="document_correction/input/cell_pic.jpg" width="30%" alt="Input image" />
  <img src="document_correction/output/urban_2_segmented_color.png" width="30%"lt="Selected contours" />
  <img src="document_correction/output/Scanned_cell_pic.jpg" width="30%" alt="The scanned version" />
</p>

<p align="center">
  <img src="document_correction/input/desk.JPG" width="30%" alt="original image" />
  <img src="document_correction/output/image_1749157422.34825_contour.jpg" width="30%"lt="Selected contours" />
  <img src="document_correction/output/Scanned_desk.JPG" width="30%" alt="The Scanned version" />
</p>

## Aerial View simulation
<p align="center">
  <img src="aerial_view_simulation/input/dollar_bill.JPG" width="30%" alt="Input image" />
  <img src="aerial_view_simulation/output/" width="30%"lt="Selected contours" />
  <img src="aerial_view_simulation/output/" width="30%" alt="Transformed image" />
</p>

<p align="center">
  <img src="aerial_view_simulation/input/urban_2_original.png" width="30%" alt="Input image" />
  <img src="aerial_view_simulation/output/urban_2_segmented_color.png" width="30%"lt="Selected contours" />
  <img src="aerial_view_simulation/output/urban_11_original.png" width="30%" alt="Transformed image" />
</p>

## Painting Point of view change
<p align="center">
  <img src="painting_view_change/input/unsplash.jpg" width="30%" alt="Input image" />
  <img src="painting_view_change/output/with_contour_image_20250605_214458.jpg" width="30%"lt="Selected contours" />
  <img src="painting_view_change/output/view_.jpg_" width="30%" alt="Transformed image" />
</p>

<p align="center">
  <img src="painting_view_change/input/urban_2_original.png" width="30%" alt="Input image" />
  <img src="painting_view_change/output/urban_2_segmented_color.png" width="30%"lt="Selected contours" />
  <img src="painting_view_change/output/urban_11_original.png" width="30%" alt="Transformed image" />
</p>

