import cv2
import mediapipe as mp

# Khởi tạo thư viện MediaPipe (Bộ não nhận diện tay)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Cấu hình: Nhìn 1 tay hay 2 tay? Độ tin cậy bao nhiêu?
hands = mp_hands.Hands(
    max_num_hands=2,           # Nhìn tối đa 2 bàn tay
    min_detection_confidence=0.7 # Phải chắc chắn 70% mới vẽ
)

# Mở Camera (Số 0 là camera laptop, số 1 là camera rời nếu có)
cap = cv2.VideoCapture(0)

print("Đang mở Camera... Nhấn phím 'q' để thoát.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Không nhận được tín hiệu camera")
        break

    # Lật ngược hình ảnh cho giống soi gương (tùy chọn)
    frame = cv2.flip(frame, 1)

    # Chuyển màu từ BGR (mặc định camera) sang RGB (Google thích cái này)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # --- PHẦN XỬ LÝ AI ---
    results = hands.process(frame_rgb)

    # Nếu nhìn thấy tay
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Vẽ bộ xương lên tay
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS
            )
            
            # --- LOGIC ĐƠN GIẢN ĐỂ NHẬN DIỆN CỬ CHỈ ---
            # Lấy tọa độ đầu ngón cái (số 4) và đầu ngón trỏ (số 8)
            ngon_cai = hand_landmarks.landmark[4]
            ngon_tro = hand_landmarks.landmark[8]
            
            # Ví dụ: Nếu đầu ngón cái chạm đầu ngón trỏ (tọa độ gần nhau)
            # (Khoảng cách Euclide đơn giản hóa)
            khoang_cach = ((ngon_cai.x - ngon_tro.x)**2 + (ngon_cai.y - ngon_tro.y)**2)**0.5
            
            if khoang_cach < 0.05: # Nếu gần sát nhau
                cv2.putText(frame, "OK / A-Okay!", (50, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Hiển thị lên màn hình
    cv2.imshow('Kinh Thong Minh - Mat Than', frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Dọn dẹp
cap.release()
cv2.destroyAllWindows()