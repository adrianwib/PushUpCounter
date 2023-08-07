import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[-1]-b[-1], c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle > 180.0:
        angle = 360-angle

    return angle



cap = cv2.VideoCapture("D:\PushHUh\pushcas.mp4")

hitungan = 0
posisi = None

with mp_pose.Pose(min_detection_confidence=0.5 , min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        hasil = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)

        # Extract Landmarks
        try:
            landmarks = hasil.pose_landmarks.landmark
            pundak = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            siku = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            gelang = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            pundak_kanan = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            siku_kanan = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            gelang_kanan = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            pinggang_kanan = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            lutut_kanan = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

            ankle_kiri = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            lutut_kiri = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            pinggang_kiri = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            jempol_kiri = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]





            angle = calculate_angle(pundak, siku, gelang)
            angle_kanan = calculate_angle(pundak_kanan, siku_kanan, gelang_kanan)
            angle_pinggang_kanan = calculate_angle(pundak_kanan, pinggang_kanan , lutut_kanan)
            angle_lutut_kiri = calculate_angle(ankle_kiri, lutut_kiri, pinggang_kiri)
            angle_ankle_kiri = calculate_angle(lutut_kiri, ankle_kiri, jempol_kiri)

            # visualize
            cv2.putText(image, str(round(angle)),tuple(np.multiply(siku, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 2, cv2.LINE_AA
                        )
            cv2.putText(image, str(round(angle_kanan)), tuple(np.multiply(siku_kanan, [640, 320]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 2, cv2.LINE_AA
                        )
            cv2.putText(image, str(round(angle_lutut_kiri)),
                        tuple(np.multiply(pinggang_kanan, [1540, 840]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA
                        )
            cv2.putText(image, str(round(angle_ankle_kiri)),
                        tuple(np.multiply(pinggang_kanan, [1840, 840]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA
                        )

            if angle > 150 and angle_kanan > 150 and angle_ankle_kiri >90:
                posisi = "naik"
            if angle < 70 and angle_kanan < 70 and angle_ankle_kiri <90 and posisi == "naik":
                posisi = "turun"
                hitungan += 1
                print(hitungan)


            print(landmarks)
        except:
            pass

        cv2.rectangle(image, (0, 0), (100, 73), (245, 117, 16), -1)

        cv2.putText(image, 'HITUNGAN', (15, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(hitungan),
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        mp_drawing.draw_landmarks(image , hasil.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0,0,255) , thickness=2 , circle_radius=4),
                                  mp_drawing.DrawingSpec(color=(255,13,14) , thickness=2 , circle_radius=4)
                                  )

        cv2.imshow("Push Up Counter" , image)
        print("Total Push : " , hitungan)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()


