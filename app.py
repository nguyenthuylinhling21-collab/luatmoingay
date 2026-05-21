from flask import Flask, render_template, jsonify, request
import random
from datetime import date
from laws_data import LAWS

app = Flask(__name__)

# ── Thông điệp động lực theo ngày trong tuần ──────────────────────────────────
MOTIVATIONS = {
    0: {
        "title": "Khởi đầu tuần mới — Bứt phá!",
        "message": "Thứ Hai là tờ giấy trắng của tuần. Mỗi quyết định bạn đưa ra hôm nay sẽ định hình cả 6 ngày còn lại. Hãy đặt ra 3 mục tiêu cụ thể và bắt đầu ngay từ bây giờ.",
        "tip": "Tip: Xử lý nhiệm vụ khó nhất trước 10 giờ sáng — não bộ hoạt động tốt nhất buổi sáng.",
        "emoji": "🚀", "color": "#2563eb"
    },
    1: {
        "title": "Thứ Ba — Xây dựng đà tốc độ",
        "message": "Hôm qua bạn đã tạo ra đà, hôm nay hãy giữ vững nó. Hiệu suất không đến từ những ngày xuất sắc, mà đến từ sự kiên trì mỗi ngày. Một bước nhỏ đều đặn hơn một bước lớn thất thường.",
        "tip": "Tip: Dùng kỹ thuật Pomodoro — 25 phút tập trung, 5 phút nghỉ để duy trì năng lượng.",
        "emoji": "⚡", "color": "#7c3aed"
    },
    2: {
        "title": "Giữa tuần — Đánh giá & Điều chỉnh",
        "message": "Thứ Tư là thời điểm vàng để nhìn lại: Bạn đã hoàn thành bao nhiêu % mục tiêu tuần? Nếu chưa đủ, đừng nản — hãy điều chỉnh kế hoạch và tăng tốc từ hôm nay.",
        "tip": "Tip: Dành 15 phút cuối ngày để review và cập nhật to-do list cho ngày mai.",
        "emoji": "🎯", "color": "#059669"
    },
    3: {
        "title": "Thứ Năm — Nước rút về đích",
        "message": "Chỉ còn 2 ngày nữa là hết tuần. Đây là lúc tập trung hoàn thành những việc quan trọng nhất. Đừng để 'gần xong' trở thành 'chưa xong' — hãy đẩy nhanh nhịp độ hôm nay.",
        "tip": "Tip: Ưu tiên theo ma trận Eisenhower — quan trọng & gấp làm trước, quan trọng & không gấp lên lịch.",
        "emoji": "🔥", "color": "#dc2626"
    },
    4: {
        "title": "Thứ Sáu — Về đích mạnh mẽ!",
        "message": "Cuối tuần gần kề, nhưng đừng để tâm lý 'cuối tuần rồi' làm bạn mất đà. Những người thành công không có ngày dễ dãi với bản thân. Hãy kết thúc tuần này thật ấn tượng!",
        "tip": "Tip: Hoàn thành tuần bằng cách viết 3 việc đã làm tốt — tạo thói quen nhìn vào thành tựu.",
        "emoji": "🏆", "color": "#d97706"
    },
    5: {
        "title": "Thứ Bảy — Học sâu & Phát triển",
        "message": "Cuối tuần là thời gian để đầu tư vào bản thân — đọc sách, học kỹ năng mới, mở rộng kiến thức. Người tiến xa nhất không phải người làm nhiều nhất, mà là người học nhiều nhất.",
        "tip": "Tip: Học 1 giờ mỗi cuối tuần = 52 giờ/năm — đủ để trở thành chuyên gia một lĩnh vực mới.",
        "emoji": "📚", "color": "#0891b2"
    },
    6: {
        "title": "Chủ Nhật — Sạc lại & Lên kế hoạch",
        "message": "Nghỉ ngơi không phải lười biếng — đó là đầu tư cho tuần kế tiếp. Hãy dành thời gian phục hồi năng lượng, nhìn lại bài học tuần qua và vạch ra chiến lược cho tuần mới.",
        "tip": "Tip: Lên kế hoạch 3 mục tiêu lớn nhất cho tuần tới ngay hôm nay — đừng để sáng Thứ Hai mới tính.",
        "emoji": "🌅", "color": "#7c3aed"
    }
}

# ── Lịch học luật theo thứ ────────────────────────────────────────────────────
WEEKLY_SCHEDULE = {
    0: {"day": "Thứ Hai",   "category": "ke_toan",    "label": "Kế Toán & Thuế"},
    1: {"day": "Thứ Ba",    "category": "lao_dong",   "label": "Lao Động"},
    2: {"day": "Thứ Tư",    "category": "dan_su",     "label": "Dân Sự"},
    3: {"day": "Thứ Năm",   "category": "kinh_te",    "label": "Kinh Tế & Doanh Nghiệp"},
    4: {"day": "Thứ Sáu",   "category": "hon_nhan",   "label": "Hôn Nhân Gia Đình"},
    5: {"day": "Thứ Bảy",   "category": "giao_duc",   "label": "Giáo Dục"},
    6: {"day": "Chủ Nhật",  "category": "hanh_chinh", "label": "Hành Chính & Hiến Pháp"},
}

CATEGORIES = {
    "ke_toan":    {"label": "Kế Toán & Thuế",  "icon": "📊", "color": "#2563eb"},
    "lao_dong":   {"label": "Lao Động",         "icon": "👷", "color": "#7c3aed"},
    "dan_su":     {"label": "Dân Sự",           "icon": "⚖️", "color": "#059669"},
    "kinh_te":    {"label": "Kinh Tế & DN",     "icon": "🏢", "color": "#d97706"},
    "hon_nhan":   {"label": "Hôn Nhân GĐ",      "icon": "👨‍👩‍👧", "color": "#dc2626"},
    "giao_duc":   {"label": "Giáo Dục",         "icon": "🎓", "color": "#0891b2"},
    "hanh_chinh": {"label": "Hành Chính",       "icon": "🏛️", "color": "#6d28d9"},
}

@app.route("/")
def index():
    today = date.today()
    weekday = today.weekday()
    return render_template("index.html",
        motivation=MOTIVATIONS[weekday],
        scheduled=WEEKLY_SCHEDULE[weekday],
        scheduled_week=WEEKLY_SCHEDULE,
        categories=CATEGORIES,
        today=today.strftime("%A, %d/%m/%Y"),
        weekday=weekday
    )

@app.route("/api/law")
def get_law():
    category = request.args.get("category", "dan_su")
    laws = LAWS.get(category, LAWS["dan_su"])
    return jsonify({"law": random.choice(laws), "category_info": CATEGORIES.get(category, {})})

@app.route("/api/motivation")
def get_motivation():
    return jsonify(MOTIVATIONS[date.today().weekday()])

if __name__ == "__main__":
    total = sum(len(v) for v in LAWS.values())
    print("\n" + "="*50)
    print("  🏛️  HỌC LUẬT MỖI NGÀY")
    print(f"  📚 Tổng số điều luật: {total}")
    print("  Mở trình duyệt: http://localhost:5000")
    print("="*50 + "\n")
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
