# 🖼️ Image Filter Web Application

[![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=flat-square&logo=render)](https://image-filter-4pce.onrender.com/)  
[![GitHub](https://img.shields.io/badge/Source-GitHub-blue?style=flat-square&logo=github)](https://github.com/TheKhushant/Image_Filter)

## 🔍 Overview

A simple yet powerful **web-based application** that allows users to upload images and apply various image processing filters. It is built using **HTML, CSS, JavaScript** on the frontend and **Python Flask** on the backend. The project demonstrates full-stack integration and the use of OpenCV for real-time image processing.

---

## 🎯 Project Objectives

- ✅ Upload an image and apply multiple filters server-side.
- ✅ Provide a clean, responsive, and intuitive UI.
- ✅ Learn and demonstrate full-stack development using Flask.

---

## 🛠️ Technologies Used

| Layer     | Technologies                                |
|-----------|---------------------------------------------|
| Frontend  | HTML, CSS, JavaScript                       |
| Backend   | Python (Flask)                              |
| Libraries | OpenCV (cv2), NumPy, Flask                  |

---

## 🔄 Working Flow

1. **Image Upload:** User selects and uploads an image.
2. **Backend Processing:** Image is sent to `/process` route using Fetch API.
3. **Image Filtering:** Server applies the following filters using OpenCV:
   - **Grayscale**
   - **Edge Detection**
   - **Gaussian Blur**
   - **Cartoon Effect**
4. **Display Results:** Processed images are shown using flip cards with hover effects.

---

## 🎨 Filters Implemented

| Filter        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **Grayscale** | Converts image to black and white using `cv2.cvtColor()`                    |
| **Edge**      | Applies edge detection using `cv2.Canny()`                                  |
| **Blur**      | Smooths the image using `cv2.GaussianBlur()`                                |
| **Cartoon**   | Combines bilateral filter & adaptive thresholding to produce cartoon effect |

---

## 📚 Features & Learnings

- 🔄 Flip card UI for processed images.
- 📤 Image upload form with preview.
- 🔁 JavaScript Fetch API for form submission.
- 📱 Responsive design with Flexbox.
- 🔄 Re-upload and refresh functionality.
- 🔧 Flask static file handling for processed images.

---

## ✅ Conclusion

Through this project, we learned:

- Full-stack communication using **Flask** and **Fetch API**.
- Handling image file uploads in a web application.
- Implementing real-time image filters with **OpenCV**.
- Building responsive UI using **HTML**, **CSS**, and **JavaScript**.
- Organizing code into frontend/backend components.
- Debugging and improving project structure and performance.

---

## 🚀 Live Project

🔗 **Live Demo**: [https://image-filter-4pce.onrender.com/](https://image-filter-4pce.onrender.com/)  
📦 **GitHub Repo**: [https://github.com/TheKhushant/Image_Filter](https://github.com/TheKhushant/Image_Filter)

---

## 🙌 Contributed By

**Khushant Wankhede**  
_Student | MCA (AI & ML) | Ramdeobaba University_

---

