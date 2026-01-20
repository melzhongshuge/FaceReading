import tkinter as tk
from tkinter import scrolledtext
import threading
import cv2 as cv
import numpy as np
from datetime import datetime
from PIL import Image, ImageTk

# ========== BRIGHTNESS_READINGS ANALYSIS  ==========

def get_brightness(crop, y1, y2, x1=0.3, x2=0.7):
    h, w = crop.shape[:2]
    roi = crop[int(h*y1):int(h*y2), int(w*x1):int(w*x2)]
    if roi.size == 0:
        return 128
    gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    return np.mean(gray)

# ---------- HOUSE READINGS ----------

def wealth_house_scan(crop):
    b = get_brightness(crop, 0.48, 0.68)

    if b > 160:
        return (
            "Your nose is bright and full — the true mark of the Wealth Palace. You possess natural magnetism for money, "
            "decisiveness, courage, and bold talent. Your treasury (nose wings) is strong, and you both earn and keep wealth with ease. "
            "Age 41–50 will be your golden period. You are destined to rise high and live comfortably.", b)
    elif b > 150:
        return (
            "Your nose radiates exceptional vitality and prosperity energy. The tip is well-rounded like a hanging drop—a classical sign of abundant wealth accumulation. "
            "You have rare entrepreneurial vision and the courage to seize golden opportunities. Money multiplies in your hands. "
            "Your generosity is legendary, yet wealth continues to flow back to you effortlessly.", b)
    elif b > 140:
        return (
            "Your nose shows excellent balance and proportion—a sign of natural wealth magnetism. The bridge is clear, connecting smoothly from Life Palace to tip. "
            "You have strong self-worth and confidence that attracts opportunities. Money flows to you through multiple channels. "
            "Your financial intuition is sharp, and you make sound decisions that protect and grow your assets.", b)
    elif b > 130:
        return (
            "Your nose shows generous energy and warm heart. You spend freely and enjoy life, yet fortune returns to you. "
            "People trust and help you. Though you give much, you never truly lack — your path is blessed with flow and recovery.", b)
    elif b > 115:
        return (
            "Your nose has good structure with moderately full wings—the treasury is present but requires mindful management. "
            "You earn steadily through honest work and dedication. While you may not become extremely wealthy overnight, you build security through persistence. "
            "Your spending habits are reasonable, and you know how to live within your means while still enjoying life.", b)
    elif b > 100:
        return (
            "You have a practical and thrifty nature. Your nostrils are hidden — a sign of one who knows how to save and protect wealth. "
            "You think deeply, plan wisely, and build slowly but surely. Middle age will reward your patience.", b)
    elif b > 95:
        return (
            "Your nose shows a practical, grounded approach to wealth. The nostrils are somewhat hidden—a classical sign of one who saves carefully. "
            "You may experience fluctuations in income, but your cautious nature protects you from major losses. "
            "Focus on building multiple income streams. Age 41-50 requires extra diligence in financial planning and avoiding risky ventures.", b)
    elif b > 80:
        return (
            "Your wealth flow is moderate. There may be worries or leaks between age 41–50. Avoid standing guarantee for others. "
            "Focus on stability, careful saving, and avoiding impulsive risks. With discipline, comfort is still possible.", b)
    elif b > 70:
        return (
            "Your Wealth Palace faces temporary challenges. The nose may appear slightly sunken or pale, indicating blocked money flow. "
            "This period calls for conservative financial choices and debt reduction. Avoid lending money or becoming a guarantor for others. "
            "Health issues affecting the nose area should be addressed. With patience and careful management, stability returns.", b)
    else:
        return (
            "Your nose currently shows significant wealth obstacles and possible health concerns. There may be dark spots, uneven coloring, or a receded bridge—all signs of blocked fortune between age 41-50. "
            "This is a time for financial caution, medical attention if needed, and spiritual cultivation. Avoid all speculation, investment risks, and major purchases. "
            "Focus on healing and rebuilding your foundation slowly.", b)

def career_house_scan(crop):
    b = get_brightness(crop, 0.05, 0.25)

    if b > 160:
        return (
            "Your forehead is high, broad, and luminous — the mark of a born leader. Heaven favors you with sharp intelligence, "
            "adaptability, and noble destiny. Success comes naturally in any field. Even if other features are modest, "
            "your career will shine brightly and bring both wealth and respect.", b)
    elif b > 150:
        return (
            "Your forehead possesses imperial quality—vast, smooth, and radiant like polished jade. This is the mark of extraordinary destiny and heaven's favor. "
            "You are blessed with visionary thinking, natural authority, and the ability to inspire masses. "
            "Your influence extends far beyond your immediate circle. Historical figures and great leaders share this feature. Power, legacy, and timeless impact define your path.", b)
    elif b > 145:
        return (
            "Your forehead extends high and wide with luminous quality—a mark of exceptional intellect and leadership destiny. "
            "You possess strategic vision and analytical power that sets you apart. Authority figures respect you, and positions of influence come naturally. "
            "Your career path is blessed with mentor support and recognition. Even obstacles transform into stepping stones for your ascent.", b)
    elif b > 130:
        return (
            "You have the strong, clear forehead of responsibility and achievement. Your thinking is structured and powerful. "
            "You are trusted in business and leadership. Your path is one of steady rise, honor, and lasting success.", b)
    elif b > 120:
        return (
            "Your forehead shows solid structure and clear energy—indicating reliable career progress through competence and responsibility. "
            "You are trusted in professional settings and build reputation through consistent performance. Your thinking is organized and practical. "
            "Success comes through diligence rather than luck, but it is lasting and respected. Leadership opportunities arise in mid-career.", b)
    elif b > 105:
        return (
            "Your forehead has gentle, rounded qualities suggesting artistic talent and creative intelligence. "
            "You excel in fields requiring imagination, beauty, or human connection. While you may not seek traditional power, you attract helpful people and supportive networks. "
            "Your career unfolds through collaboration and your warm, approachable nature. Recognition comes from your unique contributions.", b)
    elif b > 100:
        return (
            "Your forehead is kind and creative — rounded or M-shaped. You are artistic, supported by others, and blessed with helpful connections. "
            "Your success comes through talent, warmth, and noble friends. Longevity and happiness follow you.", b)
    elif b > 85:
        return (
            "Your forehead shows early-life challenges, possibly a low or uneven hairline indicating difficult family background or limited parental support in youth. "
            "Your path has required more self-reliance and struggle. However, after age 30-35, your fortune shifts significantly. "
            "The hardships build character and resilience. Later success is sweeter because you earned it yourself.", b)
    elif b > 80:
        return (
            "Early life may have been difficult — low or uneven hairline suggests challenges from family or superiors. "
            "But after age 35, your fortune improves greatly. Patience now brings comfort later.", b)
    else:
        return (
            "Your Career Palace currently faces obstacles—the forehead may appear narrow, dark, or marked with blemishes. "
            "There are conflicts with authority, unstable employment, or unclear direction. This phase requires humility and patience. "
            "Avoid confrontation with superiors. Focus on skill development and inner growth rather than external advancement. "
            "The career path clears as maturity and self-awareness increase.", b)


def fortune_house_scan(crop):
    l = get_brightness(crop, 0.18, 0.30, 0.18, 0.45)
    r = get_brightness(crop, 0.18, 0.30, 0.55, 0.82)
    b = (l + r) / 2

    if b > 160:
        return (
            "Your eyebrows are thick, glossy, and beautifully shaped — the highest sign of the Palace of Longevity. "
            "You are loyal, intelligent, and surrounded by noble help. Middle age brings rank, wealth, and deep respect. "
            "Your relationships are harmonious and lasting.", b)
    elif b > 150:
        return (
            "Your eyebrows possess the rare quality of 'silkworm brows'—perfectly curved, long, and lustrous as if painted by celestial hands. "
            "This is the mark of exceptional social fortune and profound wisdom. You are beloved by all, trusted implicitly, and your word carries weight. "
            "Siblings are loyal, marriage is blissful, and children bring honor. Your life is blessed with peace, prosperity, and exceptional longevity exceeding 90 years.", b)
    elif b > 145:
        return (
            "Your eyebrows are perfectly arched, lustrous, and well-proportioned—the ultimate sign of longevity and social blessing. "
            "You are surrounded by loyal friends and noble helpers throughout life. Your emotional intelligence is high, and people naturally trust and confide in you. "
            "Family harmony is strong, and your relationships are lasting. Wealth through partnerships and your network is abundant.", b)
    elif b > 130:
        return (
            "Your eyebrows are strong and heroic — flat, dashing, or well-formed. You are righteous, courageous, and destined for recognition. "
            "Family is harmonious, marriage enduring, and your life path is one of power, honor, and long life.", b)
    elif b > 120:
        return (
            "Your eyebrows are strong, orderly, and expressive—showing courage, integrity, and social confidence. "
            "You speak your truth and defend what is right. Your friendships are solid, built on mutual respect and shared values. "
            "In career, you command attention and inspire others. Marriage and family life are stable. Your reputation for honesty brings long-term success and honor.", b)
    elif b > 105:
        return (
            "Your eyebrows are gentle, flowing, and artistic—like willow branches or crescent moons. "
            "You are kind-hearted, empathetic, and spiritually inclined. People feel comfortable around you and seek your counsel. "
            "Your social circle is diverse and supportive. While you may not seek fame, you attract love and loyalty naturally. Creative endeavors and helping professions suit you well.", b)
    elif b > 100:
        return (
            "You have gentle, kind, and artistic eyebrows — crescent, willow, or upward. People love and help you. "
            "Your heart is warm, your connections many. Happiness in love and friendship follows you naturally.", b)
    elif b > 85:
        return (
            "Your eyebrows show some irregularity—perhaps they grow together, are uneven, or have gaps. "
            "This indicates a strong independent streak but possible social challenges. You may feel misunderstood or isolated at times. "
            "Friendships require more effort to maintain. Success comes through perseverance and self-reliance rather than connections. "
            "Choose companions carefully—quality over quantity matters for you.", b)
    elif b > 80:
        return (
            "Your social luck has ups and downs. Eyebrows may be joined or irregular — showing strong will but some isolation. "
            "Success comes through perseverance. Choose friends carefully. In time, your effort will be rewarded.", b)
    else:
        return (
            "Your Fortune Palace faces current strain—eyebrows may be sparse, very thin, or lacking definition. "
            "This suggests loneliness, reputation challenges, or relationship conflicts. There may be misunderstandings with siblings or friends. "
            "Health may also need attention, particularly regarding liver or stress-related issues. Distance yourself from toxic people. "
            "Focus on self-care, meditation, and rebuilding boundaries. This phase is temporary—your luck improves with conscious effort and healing.", b)

# ===================== GLOBAL VAR =====================

output_box = None
camera_label = None
detector = None
cap = None
current_frame = None
current_faces = None

frame_count=0

# ===================== CAMERA LOOP =====================
def camera_loop():
    global cap, detector

    detector = cv.FaceDetectorYN.create(
        model=r"C:\Users\em\face_detection_yunet_2023mar.onnx",
        config="",
        input_size=(320, 320),
        score_threshold=0.9,
        nms_threshold=0.3,
        top_k=10
    )

    cap = cv.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        h, w = frame.shape[:2]
        detector.setInputSize((w, h))

    update_frame()

# ===================== FRAME_UPDATE =====================
def update_frame():
    global current_frame, current_faces, frame_count

    ret, frame = cap.read()
    if not ret:
        return

    current_frame = frame.copy()

    frame_count += 1
    if frame_count % 3 == 0:
        detector.setInputSize((frame.shape[1], frame.shape[0]))
        faces = detector.detect(frame)
        faces = faces[1] if faces is not None else None
        current_faces = faces

    if current_faces is not None and len(current_faces) > 0:
        x, y, w_box, h_box = map(int, current_faces[0][:4])

        landmarks = current_faces[0][4:14].reshape((5, 2)).astype(int)
        left_eye, right_eye, nose_tip, mouth_l, mouth_r = landmarks

# ---------- MARKERS ----------

        overlay = frame.copy()
        
        cv.circle(overlay, tuple(nose_tip), 5, (90, 90, 255), -1)

        fx = int((left_eye[0] + right_eye[0]) / 2)  
        fy = int(min(left_eye[1], right_eye[1]) - h_box * 0.35)
        cv.circle(overlay, (fx, fy), 5, (100, 255, 255), -1)

        lb = (left_eye[0], int(left_eye[1] - h_box * 0.12))
        rb = (right_eye[0], int(right_eye[1] - h_box * 0.12))
        cv.circle(overlay, lb, 5, (80, 180, 255), -1)
        cv.circle(overlay, rb, 5, (80, 180, 255), -1)
        
        frame = cv.addWeighted(overlay, 0.9, frame, 0.6, 0)

    img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    camera_label.img = img
    camera_label.config(image=img)
    camera_label.after(30, update_frame)

# ===================== SPACE BAR =====================
def on_space(event):
    if current_frame is None or current_faces is None or len(current_faces) == 0:
        return

    x, y, w_box, h_box = map(int, current_faces[0][:4])
    crop = current_frame[y:y+h_box, x:x+w_box]
    if crop.size == 0:
        return

    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)

    output_box.insert(tk.END, "═" * 39 + "\n")
    
    title_start = output_box.index(tk.END)
    output_box.insert(tk.END, "                           YOUR FACE READING\n")
    output_box.tag_add("title", title_start, output_box.index(tk.END))
    output_box.tag_config("title", font=("Poppins", 12, "bold"), foreground="#B24536")
    
    date_start = output_box.index(tk.END)
    output_box.insert(tk.END, f"                        {datetime.now().strftime('%B %d, %Y - %I:%M %p')}\n")
    output_box.tag_add("date", date_start, output_box.index(tk.END))
    output_box.tag_config("date", font=("Poppins", 10), foreground="#B24536")
    
    output_box.insert(tk.END, "═" * 39 + "\n\n")

    w, wv = wealth_house_scan(crop)
    c, cvv = career_house_scan(crop)
    f, fv = fortune_house_scan(crop)

    # WEALTH 
    wealth_start = output_box.index(tk.END)
    output_box.insert(tk.END, f"WEALTH [{wv:.1f}]\n")
    output_box.tag_add("section_title", wealth_start, output_box.index(tk.END))
    
    output_box.insert(tk.END, f"{w}\n\n")

    # CAREER 
    career_start = output_box.index(tk.END)
    output_box.insert(tk.END, f"CAREER [{cvv:.1f}]\n")
    output_box.tag_add("section_title", career_start, output_box.index(tk.END))
    
    output_box.insert(tk.END, f"{c}\n\n")

    # FORTUNE 
    fortune_start = output_box.index(tk.END)
    output_box.insert(tk.END, f"FORTUNE [{fv:.1f}]\n")
    output_box.tag_add("section_title", fortune_start, output_box.index(tk.END))
    
    output_box.insert(tk.END, f"{f}\n")

    output_box.tag_config("section_title", font=("Poppins", 11, "bold"), foreground="#B24536", spacing1=3)
    
    output_box.see("1.0")
    output_box.config(state=tk.DISABLED)

# ===================== UI =====================
root = tk.Tk()
root.title("Chinese Face Reading")
root.geometry("1200x650")
root.configure(bg="#F8D68A")
root.bind("<space>", on_space)

root.attributes('-toolwindow', True)

TITLE_COLOR = "#B24536"

left = tk.Frame(root, bg="#FFF6EB", highlightthickness=2, highlightbackground="#E3C9B4")
left.place(x=40, y=40, width=650, height=560)

tk.Label(left, text="Live Camera Feed",
         font=("Poppins", 18, "bold"),
         fg=TITLE_COLOR, bg="#FFF6EB").pack(pady=15)

camera_label = tk.Label(left, bg="#FFF6EB")
camera_label.pack(expand=True)

right = tk.Frame(root, bg="#FFF6EB", highlightthickness=2, highlightbackground="#E3C9B4")
right.place(x=720, y=40, width=430, height=560)

tk.Label(right, text="Face Reading Output",
         font=("Poppins", 18, "bold"),
         fg=TITLE_COLOR, bg="#FFF6EB").pack(pady=15)

output_box = scrolledtext.ScrolledText(
    right, 
    wrap=tk.WORD, 
    font=("Poppins", 10),
    bg="#FFFDF8", 
    fg="#3A2D28",
    padx=12,
    pady=12,
    spacing1=2,
    spacing2=1,
    spacing3=3,
    relief=tk.FLAT,
    borderwidth=0
)
output_box.pack(expand=True, fill=tk.BOTH, padx=15, pady=(0, 15))

# ========== INITIAL_INSTRUCTIONS  ==========
output_box.insert(tk.END, "\n\n\n     ✨ Align your face with the markers\n\n")
output_box.insert(tk.END, "     Press SPACEBAR to receive\n     your personalized reading\n\n\n")
output_box.tag_add("placeholder", "1.0", tk.END)
output_box.tag_config("placeholder", font=("Poppins", 11, "italic"), justify="center", foreground="#999999")
output_box.config(state=tk.DISABLED)

threading.Thread(target=camera_loop, daemon=True).start() 

root.mainloop()

