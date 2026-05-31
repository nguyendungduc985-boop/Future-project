# 🧠 ADVANCED COMPUTER VISION & HUMAN-COMPUTER INTERACTION (HCI) PROJECTS

<p align="center">
  <a href="#tieng-viet">Tiếng Việt</a> • 
  <a href="#english">English</a> • 
  <a href="#korean">한국어</a>
</p>

---

## Tiếng Việt <a name="tieng-viet"></a>

> **Một hệ sinh thái giả lập Kính thông minh (Smart Glasses) tích hợp AI, nhận diện cử chỉ (Computer Vision) và phiên dịch viên thời gian thực (Speech-to-Text & LLM) chạy trực tiếp trên máy tính cá nhân.**

### 🌟 Giới thiệu Dự án
Dự án nhằm mục đích xây dựng phần mềm cốt lõi cho một chiếc Kính thông minh hỗ trợ giao tiếp và tương tác bằng AI. Dù hiện tại chưa triển khai trên phần cứng (Kính AR/VR), hệ thống đã hoàn thiện các module giả lập cốt lõi thông qua Webcam và Microphone của máy tính nhằm hỗ trợ người khiếm thính hoặc hỗ trợ giao tiếp đa ngôn ngữ với chi phí bằng **0**.

### 🛠️ Các Tính Năng Hiện Có (Cấu trúc Repo)

| Tên File | Chức Năng Chính | Công Nghệ Sử Dụng |
| :--- | :--- | :--- |
| 👁️ **mat_than.py** | **Module Mắt Thần Cử Chỉ**: Tracking 21 điểm xương bàn tay. Tự động nhận diện cử chỉ `"OK / A-Okay!"` khi đầu ngón cái và ngón trỏ chạm nhau để chuẩn bị cho các lệnh điều khiển HUD. | `MediaPipe Hands`, `OpenCV` |
| 🧠 **tritue.py** | **Trợ Lý Phiên Dịch Đa Ngôn Ngữ**: Lắng nghe đa ngôn ngữ (mặc định tiếng Trung `zh-CN`), dịch thuật tự nhiên theo ngữ cảnh và chuyển thành giọng nói tiếng Việt qua file `tra_loi.mp3`. | `Gemini 2.5 Flash`, `gTTS`, `SpeechRecognition` |
| 🕶️ **kinh_hoan_thien.py** | **Kính Thông Minh Hợp Nhất**: Chạy đa luồng (**Multithreading**). Vừa tracking cử chỉ tay (`Like` -> `"TUYỆT VỜI"`), vừa lắng nghe hội thoại tiếng Anh, dịch và hiển thị phụ đề tiếng Việt có dấu lên giao diện HUD. | `OpenCV`, `Pillow (PIL)`, `Gemini API`, `Threading` |

### 🚀 Hướng Dẫn Cài Đặt

Cài đặt các thư viện phụ thuộc:
bash
```
pip install opencv-python mediapipe SpeechRecognition google-generativeai pillow numpy gTTS
```
---

## English <a name="english"></a>

> **A Smart Glasses simulation ecosystem powered by AI, Computer Vision hand-gesture recognition, and real-time speech translation running directly on a personal computer.**

### 🌟 Project Overview
This project aims to develop the core software of an AI-powered Smart Glasses system for communication assistance and human-computer interaction. Although not yet deployed on AR/VR hardware, all major modules are fully functional using a standard webcam and microphone, providing an accessible and low-cost solution for hearing-impaired users and multilingual communication.

### 🛠️ Current Features (Repository Structure)

| File Name | Main Function | Technologies |
| :--- | :--- | :--- |
| 👁️ **mat_than.py** | **Hand Gesture Vision Module**: Tracks 21 hand landmarks and automatically detects the `"OK / A-Okay!"` gesture when the thumb and index finger touch. Designed as the foundation for future HUD controls. | `MediaPipe Hands`, `OpenCV` |
| 🧠 **tritue.py** | **Multilingual AI Translator Assistant**: Listens to speech (default: Chinese `zh-CN`), performs contextual translation, and generates Vietnamese voice responses through `tra_loi.mp3`. | `Gemini 2.5 Flash`, `gTTS`, `SpeechRecognition` |
| 🕶️ **kinh_hoan_thien.py** | **Unified Smart Glasses System**: Uses multithreading to simultaneously detect hand gestures (`Like` → `"EXCELLENT"`), listen to English conversations, translate them, and display Vietnamese subtitles on a HUD interface. | `OpenCV`, `Pillow (PIL)`, `Gemini API`, `Threading` |

### 🚀 Installation

Install required dependencies:

```bash
pip install opencv-python mediapipe SpeechRecognition google-generativeai pillow numpy gTTS
```

### 🎯 Future Development Goals

- Real-time AR Glasses deployment
- Sign Language Recognition
- Face Recognition & User Profiles
- Voice Command Navigation
- AI-powered Context Awareness
- Offline Translation Support
- HUD Menu Control via Hand Gestures

---

## 한국어 <a name="korean"></a>

> **AI, 컴퓨터 비전 기반 손동작 인식, 실시간 음성 번역 기능을 통합한 스마트 안경(Smart Glasses) 시뮬레이션 프로젝트입니다.**

### 🌟 프로젝트 소개

본 프로젝트는 AI 기반 스마트 안경의 핵심 소프트웨어를 개발하는 것을 목표로 합니다. 아직 AR/VR 하드웨어에는 적용되지 않았지만, 일반 웹캠과 마이크만으로 핵심 기능을 구현하여 청각 장애인 지원 및 다국어 의사소통을 위한 저비용 솔루션을 제공합니다.

### 🛠️ 현재 기능 (저장소 구조)

| 파일명 | 주요 기능 | 사용 기술 |
| :--- | :--- | :--- |
| 👁️ **mat_than.py** | **손동작 인식 모듈**: 손의 21개 랜드마크를 추적하고 엄지와 검지가 닿을 때 `"OK / A-Okay!"` 제스처를 자동으로 인식합니다. 향후 HUD 제어 기능의 기반이 됩니다. | `MediaPipe Hands`, `OpenCV` |
| 🧠 **tritue.py** | **다국어 AI 통역 비서**: 음성을 인식하고(기본 언어: 중국어 `zh-CN`), 문맥에 맞게 번역한 후 `tra_loi.mp3`를 통해 베트남어 음성으로 출력합니다. | `Gemini 2.5 Flash`, `gTTS`, `SpeechRecognition` |
| 🕶️ **kinh_hoan_thien.py** | **통합 스마트 안경 시스템**: 멀티스레딩을 사용하여 손동작(`Like` → `"최고!"`) 인식, 영어 대화 청취, 번역 및 HUD 자막 표시를 동시에 수행합니다. | `OpenCV`, `Pillow (PIL)`, `Gemini API`, `Threading` |

### 🚀 설치 방법

필수 라이브러리 설치:

```bash
pip install opencv-python mediapipe SpeechRecognition google-generativeai pillow numpy gTTS
```

### 🎯 향후 개발 계획

- AR 스마트 안경 실기기 적용
- 수어(Sign Language) 인식
- 얼굴 인식 및 사용자 프로필 관리
- 음성 명령 기반 내비게이션
- AI 상황 인식(Context Awareness)
- 오프라인 번역 기능
- 손동작 기반 HUD 메뉴 제어

- 📬 Contact / 연락처
Developer: Nguyễn Đức Dũng (덕용)

Email: nguyendungduc985@gmail.com

Major: Artificial Intelligence (AI) @ East Asia University (Đại học Đông Á)
