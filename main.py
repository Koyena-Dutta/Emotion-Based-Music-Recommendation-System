import cv2
import time
import webbrowser
from deepface import DeepFace


# 📌 Spotify playlist URLs for each emotion
EMOTION_PLAYLISTS = {
    "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
    "sad": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
    "angry": "https://open.spotify.com/playlist/37i9dQZF1DX3ndUj0YtV8E",
    "neutral": "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY",
    "surprise": "https://open.spotify.com/playlist/37i9dQZF1DX3qCx5yEZkcJ",
    "disgust": "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd",
    "fear": "https://open.spotify.com/playlist/37i9dQZF1DWXe9gFZP0gtP"
}


def open_spotify_playlist(emotion):
    playlist_url = EMOTION_PLAYLISTS.get(emotion)
    if playlist_url:
        print(f"[SPOTIFY] Opening playlist for: {emotion}")
        webbrowser.open(playlist_url)
    else:
        print(f"[ERROR] No playlist mapped for emotion: {emotion}")


def analyze_emotion(frame):
    try:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = DeepFace.analyze(
            rgb,
            actions=['emotion'],
            enforce_detection=False
        )

        # DeepFace sometimes returns a list
        if isinstance(result, list):
            result = result[0]

        dominant = result.get("dominant_emotion", None)
        print(f"[DEBUG] Detected emotion: {dominant}")
        return dominant.lower() if dominant else None

    except Exception as e:
        print("[ERROR] DeepFace error:", e)
        return None


def main():
    print("Opening camera...")

    # Try external webcam first
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    time.sleep(1)

    if not cap.isOpened():
        print("[INFO] External cam not found. Trying internal...")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        time.sleep(1)

    if not cap.isOpened():
        print("❌ No camera detected.")
        return

    cap.set(3, 1280)
    cap.set(4, 720)

    print("Camera started! Capturing emotion for 5 seconds...")
    emotions = []
    start = time.time()

    # ⭐ Capture emotions for exactly 5 seconds
    while time.time() - start < 5:
        ret, frame = cap.read()
        if not ret:
            break

        small = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6)

        emo = analyze_emotion(small)
        if emo:
            emotions.append(emo)

        cv2.putText(frame, "Capturing emotion...", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        cv2.imshow("Emotion Capture (5 sec)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("User exited.")
            break

    cap.release()
    cv2.destroyAllWindows()

    if not emotions:
        print("❌ No emotion detected. Try again.")
        return

    # ⭐ Pick the most common emotion after 5 seconds
    final_emotion = max(set(emotions), key=emotions.count)

    print("\n==============================")
    print(f"🎯 FINAL DETECTED EMOTION: {final_emotion}")
    print("==============================\n")

    # ⭐ Open playlist ONCE
    open_spotify_playlist(final_emotion)


if __name__ == "__main__":
    main()
