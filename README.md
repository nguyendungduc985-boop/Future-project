# 🧠 ADVANCED COMPUTER VISION & HUMAN-COMPUTER INTERACTION (HCI) PROJECTS

<p align="center">
  <a href="#tieng-viet">Tiếng Việt</a> • 
  <a href="#english">English</a> • 
  <a href="#korean">한국어</a>
</p>

---

<h2 id="tieng-viet"> 🇻🇳 Tiếng Việt </h2>

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
```bash
pip install opencv-python mediapipe SpeechRecognition google-generativeai pillow numpy gTTS
Thay API Key Gemini của bạn vào các file mã nguồn và chạy ứng dụng hợp nhất:Bashpython kinh_hoan_thien.py
A smart glasses simulation ecosystem integrating AI, hand gesture recognition (Computer Vision), and real-time translation (Speech-to-Text & LLM) running directly on personal computers.🌟 Project OverviewThis project aims to build the core software for AI-powered Smart Glasses. Although not yet deployed on physical AR/VR hardware, the system simulates core functionalities using a standard PC webcam and microphone. It serves as a zero-cost solution to assist the hearing impaired and facilitate multilingual communication.🛠️ Core Features (Repository Structure)File NameMain FunctionalityTech Stack👁️ mat_than.pyGesture Recognition Module: Tracks 21 hand landmarks. It detects the "OK / A-Okay!" gesture when the thumb and index finger touch, paving the way for touchless HUD control commands.MediaPipe Hands, OpenCV🧠 tritue.pyMultilingual AI Translation Assistant: Listens to foreign languages (configured to Chinese zh-CN by default), connects to API for context-aware natural translation, and outputs smooth Vietnamese audio via tra_loi.mp3.Gemini 2.5 Flash, gTTS, SpeechRecognition🕶️ kinh_hoan_thien.pyIntegrated Smart Glasses: A high-level multithreaded implementation. It simultaneously tracks hand gestures (Thumbs up -> "LIKE/EXCELLENT") and listens to English speech, dynamically rendering Vietnamese subtitles onto the HUD overlay.OpenCV, Pillow (PIL), Gemini API, Threading🚀 Quick StartInstall dependencies:Bashpip install opencv-python mediapipe SpeechRecognition google-generativeai pillow numpy gTTS
Insert your Gemini API Key into the source files and execute:Bashpython kinh_hoan_thien.py
개인 PC에서 직접 실행되는 AI, 손동작 인식(컴퓨터 비전) 및 실시간 통역(Speech-to-Text & LLM) 기능이 통합된 스마트 글래스 시뮬레이션 에코시스템입니다.🌟 프로젝트 개요본 프로젝트는 AI 기반 스마트 글래스의 핵심 소프트웨어를 구축하는 것을 목표로 합니다. 현재 실제 AR/VR 하드웨어에 구현되지는 않았지만, PC의 웹캠과 마이크를 통해 핵심 기능을 시뮬레이션합니다. 이를 통해 청각 장애인을 지원하고 비용 부담 없이 다국어 소통을 돕는 솔루션을 제공합니다.🛠️ 핵심 기능 (레포지토리 구조)파일명주요 기능사용 기술👁️ mat_than.py손동작 인식 모듈: 21개의 손 관절 포인트를 추적합니다. 엄지와 검지가 맞닿을 때 "OK / A-Okay!" 제스처를 감지하여 향후 HUD 제어 명령을 위한 기반을 마련합니다.MediaPipe Hands, OpenCV🧠 tritue.py다국어 AI 통역 비서: 외국어(기본 설정: 중국어 zh-CN)를 실시간으로 청취하고, 문맥에 맞는 자연스러운 번역을 수행한 뒤 자연스러운 베트남어 음성 파일(tra_loi.mp3)로 출력합니다.Gemini 2.5 Flash, gTTS, SpeechRecognition🕶️ kinh_hoan_thien.py통합 스마트 글래스: 멀티스레딩(Multithreading)으로 구동되는 고급 통합 모듈입니다. 손동작 (엄지 척 -> "LIKE / 최고")을 추적하는 동시에 영어 음성을 감지하여 성조가 포함된 베트남어 자막을 HUD 화면에 실시간으로 매끄럽게 표시합니다.OpenCV, Pillow (PIL), Gemini API, Threading🚀 시작 가이드필수 라이브러리 설치:Bashpip install opencv-python mediapipe SpeechRecognition google-generativeai pillow numpy gTTS
소스 코드 파일에 본인의 Gemini API Key를 입력한 후 아래 명령어를 실행하세요:Bashpython kinh_hoan_thien.py
📬 Contact / 연락처Developer: Nguyễn Đức Dũng (덕용)Email: nguyendungduc985@gmail.comMajor: Artificial Intelligence (AI) @ East Asia University (Đại học Đông Á)
