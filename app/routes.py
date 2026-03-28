from flask import Blueprint, render_template, request
import random

main = Blueprint('main', __name__)

palette_dict = {
    "happy": [
        ["#FFD700", "#FFA500", "#FF69B4", "#FFFF00"],
        ["#FFE066", "#FAB1A0", "#FF7675", "#FD79A8"]
    ],
    "calm": [
        ["#A8DADC", "#457B9D", "#1D3557", "#F1FAEE"],
        ["#B5EAEA", "#EDF6F9", "#83C5BE", "#006D77"]
    ],
    "dark": [
        ["#2B2D42", "#1A1A2E", "#000000", "#3A0CA3"],
        ["#22223B", "#4A4E69", "#9A8C98", "#C9ADA7"]
    ],
    "romantic": [
        ["#FF1493", "#FF69B4", "#FFC0CB", "#DB7093"],
        ["#FF6B81", "#FF4757", "#FFB6C1", "#FFC1CC"]
    ],
    "pastel": [
        ["#FFD1DC", "#FFE4E1", "#E0BBE4", "#C1E1C1"],
        ["#FFDAC1", "#B5EAD7", "#C7CEEA", "#FFB7B2"]
    ],
    "neon": [
        ["#39FF14", "#FF073A", "#04D9FF", "#FCEE0C"],
        ["#FF00FF", "#00FFFF", "#FFFF00", "#FF4500"]
    ],
    "sunset": [
        ["#FF7E5F", "#FEB47B", "#FD3A69", "#F9D423"],
        ["#FDC830", "#F37335", "#FF512F", "#DD2476"]
    ],
    "ocean": [
        ["#0077B6", "#00B4D8", "#90E0EF", "#CAF0F8"],
        ["#023E8A", "#0096C7", "#48CAE4", "#ADE8F4"]
    ],
    "forest": [
        ["#2D6A4F", "#40916C", "#52B788", "#95D5B2"],
        ["#1B4332", "#2D6A4F", "#40916C", "#74C69D"]
    ],
    "minimal": [
        ["#000000", "#333333", "#777777", "#FFFFFF"],
        ["#111111", "#444444", "#888888", "#DDDDDD"]
    ]
}

@main.route("/", methods=["GET", "POST"])
def home():
    mood = "happy"
    palettes = palette_dict["happy"]

    if request.method == "POST":
        mood = request.form.get("mood").lower()

        if mood == "random":
            palettes = [
                [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(4)]
                for _ in range(3)
            ]
        else:
            palettes = palette_dict.get(mood, palette_dict["happy"])

    return render_template("index.html", palettes=palettes, mood=mood)