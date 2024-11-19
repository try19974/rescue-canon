from ultralytics import YOLO
import cv2
import math
import threading
import serial
import time

# Running real-time from webcam
cap = cv2.VideoCapture(0)
model = YOLO("C:\\Users\\korn\\Downloads\\kk\\runs\\detect\\train5\\weights\\best.pt")
arduino = serial.Serial('COM11', 115200)  # เปลี่ยนพอร์ตให้เป็นพอร์ตของคุณ

motor_lock = threading.Lock()

# Reading the classes
classnames = ['fire']

# Flag เพื่อบอกว่า Arduino กำลังหมุนมอเตอร์อยู่หรือไม่
nofire = False
stop_motor = False
detected_fire = False
motor_running = False
frame_width = 640
frame_height = 480
frame_center_y = frame_height // 2
direction= "kuy"

# ฟังก์ชันสำหรับส่งคำสั่งไปยัง Arduino และรอการตอบกลับแบบไม่บล็อก
def nocum():
    global nofire, stop_motor
    global motor_running
    nofire = True
    stop_motor = False
    global direction
    while not stop_motor:  # ลูปหมุนมอเตอร์ไปกลับจนกว่าจะได้รับคำสั่งให้หยุด
            arduino.write(b'go')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2) 
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            arduino.write(b'go')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            arduino.write(b'go')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            arduino.write(b'go')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            arduino.write(b'go')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            
            arduino.write(b'go')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            arduino.write(b'back')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2) 
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            arduino.write(b'back')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            arduino.write(b'back')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            arduino.write(b'back')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            
            arduino.write(b'back')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
            
            arduino.write(b'back')  # สั่งให้มอเตอร์หมุนไป
            time.sleep(2)
            
            if stop_motor:  # ตรวจสอบว่าถูกสั่งให้หยุดหรือไม่
                break
        
        # สั่งให้มอเตอร์หยุดเมื่อออกจากลูป
    motor_running = True
    with motor_lock:
        print(direction)
        # ส่งคำสั่งไปที่ Arduino เพื่อให้หมุนมอเตอร์
        if direction == "up":
            arduino.write(b'up')
        elif direction == "down":
            arduino.write(b'down')
        elif direction == "nomal":
            arduino.write(b'nomal')

        while True:
            if arduino.in_waiting > 0:
                response = arduino.readline().decode().strip()
                if response == "done":
                    break
    motor_running = False
    nofire = False
    direction = "kuy"

def stop_motor_control():
    global stop_motor
    stop_motor = True 
    

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (frame_width, frame_height))

    # ดึงข้อมูลการทำนายจากโมเดล YOLO
    result = model(frame, stream=True)

    detected_fire = False  # รีเซ็ตสถานะการตรวจจับไฟในทุกเฟรม

    # Getting bbox, confidence and class names information
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])

            # ตรวจสอบความมั่นใจ และหากมั่นใจเกิน 50% ว่าเป็นไฟ
            if confidence > 50:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                fire_center_y = (y1 + y2) // 2
                print("ตรวจพบไฟ")
                detected_fire = True  # พบไฟ
                if nofire:
                    stop_motor_control()

                if not motor_running:
                    if fire_center_y < frame_center_y - 50: 
                        direction="up"
                    elif fire_center_y > frame_center_y + 50:
                        direction="down"
                    else:
                        direction="nomal"

    # ถ้าไม่พบการตรวจจับไฟ
    if not detected_fire:
        print("ไม่พบไฟ")
        if not nofire:
            ku = threading.Thread(target=nocum)
            ku.start()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('frame', frame)
    cv2.waitKey(1)

# ปิดกล้องและหน้าต่าง
cap.release()
cv2.destroyAllWindows()
