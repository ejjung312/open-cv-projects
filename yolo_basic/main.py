from ultralytics import YOLO
import cv2

# load yolo model
model = YOLO()

# load video
input_video = '/content/test.mp4'
output_video = '/content/output.mp4'
cap = cv2.VideoCapture(input_video)

# 비디오 속성 가져오기
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 코덱 설정 (mp4)

# 비디오 저장 설정
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# read frames
if cap.isOpened():
  while True:
    ret, frame = cap.read()
    if not ret:
      break
    
    # detect objects
    # track objects
    # persist: 객체 추적 상태를 다음 프레임으로 유지
    results = model.track(frame, persist=True)

    # plot results
    # 첫번째 프레임에 대한 추적 결과를 시각화
    frame_ = results[0].plot()

    # 프레임 저장
    out.write(frame_)

    # visualize
    # cv2.imshow('frame', frame_)
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #   break

cap.release()
out.release()
# cv2.destroyAllWindows()