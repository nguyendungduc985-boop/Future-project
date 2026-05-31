import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
import os
import time

# --- CẤU HÌNH ---
API_KEY = "AIzaSyA8XgP_eqreE2je-gu7qvQ2J5LKnfQxl8k"
genai.configure(api_key=API_KEY)

# Dùng model xịn nhất của bạn
model = genai.GenerativeModel('gemini-2.5-flash')
recognizer = sr.Recognizer()

# --- CÀI ĐẶT NGÔN NGỮ ĐẦU VÀO (Tai nghe) ---
# Nếu muốn nghe tiếng Anh: để "en-US"
# Nếu muốn nghe tiếng Nhật: đổi thành "ja-JP"
# Nếu muốn nghe tiếng Trung: đổi thành "zh-CN"
# Nếu muốn nghe tiếng Hàn: đổi thành "ko-KR"
NGON_NGU_CAN_NGHE = "zn-CN" 

def noi_chuyen(text):
    """Máy tính đọc to kết quả"""
    print(f"🤖 Kính nói: {text}")
    try:
        # Loại bỏ dấu * để đọc cho mượt
        text_clean = text.replace("*", "").replace("#", "")
        tts = gTTS(text=text_clean, lang='vi')
        tts.save("tra_loi.mp3")
        os.system("start tra_loi.mp3") 
    except Exception:
        pass

def xu_ly_ai(cau_hoi):
    print("...Đang suy nghĩ...")
    # --- ĐÂY LÀ CHỖ DẠY AI CÁCH NÓI CHUYỆN ---
    prompt = f"""
    Bạn là trợ lý phiên dịch.
    Người dùng vừa nghe được câu: "{cau_hoi}"
    
    Yêu cầu trả lời:
    1. Dịch câu đó sang tiếng Việt chuẩn xác.
    2. Bắt đầu câu trả lời bằng cụm từ: "Câu này có nghĩa là".
    3. Tuyệt đối KHÔNG dùng các ký tự đặc biệt như dấu sao (*), dấu thăng (#).
    4. Chỉ viết ra lời nói, không viết thêm giải thích.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Xin lỗi, tôi bị mất kết nối mạng."

def main():
    print("\n" + "="*40)
    print(f"   KÍNH ĐANG LẮNG NGHE ({NGON_NGU_CAN_NGHE})   ")
    print("="*40)
    
    while True:
        try:
            with sr.Microphone() as source:
                print("\n🎧 Đang nghe... (Im lặng để thu âm)")
                # Tăng độ nhạy mic lên một chút
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Nghe trong 5 giây
                audio = recognizer.listen(source, timeout=5)
                
                print("⏳ Đang nhận dạng ngôn ngữ...")
                # Chỗ này quyết định nghe tiếng nước nào
                text_input = recognizer.recognize_google(audio, language=NGON_NGU_CAN_NGHE)
                
                print(f"🗣️ Nghe được: {text_input}")

                if text_input:
                    ket_qua = xu_ly_ai(text_input)
                    print("-" * 30)
                    print(f"💡 Dịch: {ket_qua}")
                    print("-" * 30)
                    noi_chuyen(ket_qua)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            # Không in lỗi đỏ nữa cho đỡ rối mắt
            print(".", end="", flush=True) 
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()