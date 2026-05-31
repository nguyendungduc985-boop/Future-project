import cv2
import mediapipe as mp
import speech_recognition as sr
import google.generativeai as genai
from PIL import ImageFont, ImageDraw, Image # Thư viện xử lý ảnh xịn hơn
import numpy as np
import os
import threading
import time

# --- CẤU HÌNH ---
API_KEY = "AIzaSyDzRnDFlJijqmuGy4sgvSa5kKHMA3NfJVw" 
genai.configure(api_key=API_KEY)
# Dùng model nào cũng được, flash cho nhanh
model = genai.GenerativeModel('gemini-2.5-flash') 

# Biến toàn cục
phu_de_hien_tai = "Đang lắng nghe..."
mau_chu = (255, 255, 255) # Trắng

# --- HÀM MỚI: VIẾT TIẾNG VIỆT LÊN ẢNH ---
def viet_tieng_viet(img, text, pos, color, font_size=30):
    """
    Hàm này giúp OpenCV viết được tiếng Việt có dấu
    bằng cách chuyển đổi qua lại giữa OpenCV và PIL
    """
    try:
        # 1. Chuyển ảnh OpenCV (BGR) sang ảnh PIL (RGB)
        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        
        # 2. Chọn font chữ (Lấy Arial có sẵn trong Windows)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            # Nếu không tìm thấy Arial thì dùng font mặc định (xấu hơn chút)
            font = ImageFont.load_default()
        
        # 3. Vẽ chữ
        draw.text(pos, text, font=font, fill=color[::-1]) # Đảo ngược màu BGR->RGB
        
        # 4. Chuyển lại về ảnh OpenCV
        return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Lỗi font chữ: {e}")
        return img

# --- PHẦN 1: XỬ LÝ ÂM THANH ---
def xu_ly_audio(recognizer, audio):
    global phu_de_hien_tai, mau_chu
    try:
        print("...Đang xử lý âm thanh...")
        # Nghe tiếng Anh (hoặc bạn đổi thành ngôn ngữ khác nếu muốn)
        text_input = recognizer.recognize_google(audio, language="en-US") 
        print(f"Nghe được: {text_input}")

        # Gửi Gemini dịch
        prompt = f"""
        Dịch câu này sang tiếng Việt ngắn gọn: "{text_input}"
        Chỉ in ra kết quả dịch, không giải thích.
        """
        response = model.generate_content(prompt)
        ket_qua_dich = response.text.strip()
        
        # Cập nhật phụ đề
        phu_de_hien_tai = f"Dịch: {ket_qua_dich}"
        mau_chu = (0, 255, 255) # Màu vàng
        
    except sr.UnknownValueError:
        pass 
    except Exception as e:
        print(f"Lỗi Mic: {e}")

def lang_nghe_lien_tuc():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
    r.listen_in_background(m, xu_ly_audio)
    while True:
        time.sleep(1)

# --- PHẦN 2: XỬ LÝ HÌNH ẢNH ---
def chay_kinh_thong_minh():
    global phu_de_hien_tai, mau_chu
    
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

    cap = cv2.VideoCapture(0)

    print("--- KÍNH ĐÃ KHỞI ĐỘNG (BẢN VIỆT HÓA) ---")
    print("Nhấn 'q' để thoát")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        # OpenCV xử lý hình ảnh thô
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Logic Like
                y_ngon_cai = hand_landmarks.landmark[4].y
                y_khop_cai = hand_landmarks.landmark[3].y
                
                if y_ngon_cai < y_khop_cai - 0.05:
                    phu_de_hien_tai = "Cử chỉ: TUYỆT VỜI! (LIKE)"
                    mau_chu = (0, 255, 0) # Xanh lá

        # --- GIAO DIỆN MỚI ---
        h, w, _ = frame.shape
        # Vẽ bảng đen nền
        cv2.rectangle(frame, (0, h-100), (w, h), (0, 0, 0), -1) 
        
        # --- THAY ĐỔI QUAN TRỌNG NHẤT Ở ĐÂY ---
        # Thay vì dùng cv2.putText, ta dùng hàm viết tiếng Việt mới tạo
        frame = viet_tieng_viet(frame, phu_de_hien_tai, (20, h-60), mau_chu, font_size=35)

        cv2.imshow('Kinh Thong Minh AI (Vietnamese Version)', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    thread_am_thanh = threading.Thread(target=lang_nghe_lien_tuc)
    thread_am_thanh.daemon = True 
    thread_am_thanh.start()

    chay_kinh_thong_minh()