# ── Dữ liệu điều luật — 20 điều/mục × 7 mục = 140 điều ──────────────────────

LAWS = {

# ═══════════════════════════════════════════════════════════════
#  KẾ TOÁN & THUẾ
# ═══════════════════════════════════════════════════════════════
"ke_toan": [
    {
        "so_dieu": "Điều 10", "ten_luat": "Luật Kế toán 2015",
        "tieu_de": "Nguyên tắc kế toán cơ bản",
        "noi_dung": "Kế toán phải phản ánh đầy đủ, trung thực các nghiệp vụ kinh tế phát sinh. Doanh nghiệp không được hạch toán sai lệch làm sai lệch kết quả tài chính.",
        "vi_du": "Công ty A bán hàng tháng 12 nhưng chưa thu tiền — vẫn phải ghi nhận doanh thu tháng 12 theo nguyên tắc dồn tích.",
        "biet_them": "Vi phạm nguyên tắc này có thể bị phạt từ 20-30 triệu đồng theo Nghị định 41/2018/NĐ-CP."
    },
    {
        "so_dieu": "Điều 14", "ten_luat": "Luật Kế toán 2015",
        "tieu_de": "Chứng từ kế toán là bắt buộc",
        "noi_dung": "Mọi nghiệp vụ kinh tế phát sinh phải có chứng từ kế toán hợp lệ. Chứng từ phải đủ yếu tố: tên, số hiệu, ngày tháng, nội dung, số tiền, chữ ký.",
        "vi_du": "Chi tiền mặt mua văn phòng phẩm mà không có hóa đơn hoặc phiếu chi hợp lệ — khoản chi đó không được hạch toán vào chi phí.",
        "biet_them": "Chứng từ kế toán phải lưu trữ tối thiểu 5 năm (chứng từ hàng năm) hoặc 10 năm (chứng từ liên quan đến tài sản)."
    },
    {
        "so_dieu": "Điều 41", "ten_luat": "Luật Kế toán 2015",
        "tieu_de": "Kiểm kê tài sản bắt buộc cuối năm",
        "noi_dung": "Đơn vị kế toán phải thực hiện kiểm kê tài sản vào cuối kỳ kế toán năm. Kết quả kiểm kê phải được phản ánh vào sổ kế toán và báo cáo tài chính.",
        "vi_du": "Cuối năm công ty phải đếm thực tế hàng tồn kho, so sánh với số sách — nếu thừa/thiếu phải điều chỉnh sổ sách.",
        "biet_them": "Kiểm kê đột xuất được thực hiện khi có quyết định của cơ quan nhà nước có thẩm quyền hoặc khi bàn giao."
    },
    {
        "so_dieu": "Điều 26", "ten_luat": "Luật Thuế GTGT 2008 (sửa đổi 2013)",
        "tieu_de": "Hóa đơn điện tử bắt buộc từ 2022",
        "noi_dung": "Từ ngày 01/07/2022, tất cả doanh nghiệp, hộ kinh doanh phải sử dụng hóa đơn điện tử theo Nghị định 123/2020/NĐ-CP. Hóa đơn giấy không còn giá trị pháp lý.",
        "vi_du": "Cửa hàng bán lẻ dù nhỏ cũng phải đăng ký phần mềm hóa đơn điện tử và xuất hóa đơn cho khách hàng.",
        "biet_them": "Phạt từ 10-20 triệu nếu không dùng hóa đơn điện tử theo quy định."
    },
    {
        "so_dieu": "Điều 14", "ten_luat": "Luật Thuế GTGT 2024",
        "tieu_de": "Mọi giao dịch phải chuyển khoản mới được khấu trừ GTGT",
        "noi_dung": "Từ 01/7/2025, tất cả hàng hóa dịch vụ mua vào — kể cả dưới 20 triệu đồng — đều phải có chứng từ thanh toán không dùng tiền mặt mới được khấu trừ thuế GTGT đầu vào.",
        "vi_du": "Mua văn phòng phẩm 5 triệu bằng tiền mặt từ 01/7/2025 — không được khấu trừ thuế GTGT đầu vào 500.000đ.",
        "biet_them": "Đây là thay đổi lớn so với quy định cũ (cho phép thanh toán tiền mặt dưới 20 triệu). Doanh nghiệp cần điều chỉnh quy trình thanh toán."
    },
    {
        "so_dieu": "Điều 44", "ten_luat": "Luật Thuế TNDN 2008",
        "tieu_de": "Thuế suất thu nhập doanh nghiệp",
        "noi_dung": "Thuế suất thuế TNDN phổ thông là 20%. Doanh nghiệp vừa và nhỏ được áp dụng thuế suất ưu đãi 17% nếu đáp ứng điều kiện. Doanh nghiệp khai thác dầu khí chịu thuế suất 32-50%.",
        "vi_du": "Doanh nghiệp có lợi nhuận 1 tỷ đồng/năm nộp thuế TNDN = 200 triệu đồng (20%).",
        "biet_them": "Nộp tờ khai tạm tính quý và quyết toán năm trước ngày 31/3 năm sau."
    },
    {
        "so_dieu": "Điều 20", "ten_luat": "Luật Thuế TNCN 2007 (sửa đổi 2012)",
        "tieu_de": "Giảm trừ gia cảnh khi tính thuế TNCN",
        "noi_dung": "Người nộp thuế được giảm trừ 11 triệu đồng/tháng cho bản thân và 4,4 triệu đồng/tháng cho mỗi người phụ thuộc đủ điều kiện.",
        "vi_du": "Thu nhập 20 triệu/tháng, có 2 con phụ thuộc: thu nhập chịu thuế = 20tr - 11tr - 8,8tr = 0,2tr → thuế rất thấp.",
        "biet_them": "Người phụ thuộc phải được đăng ký với cơ quan thuế. Mỗi người chỉ được đăng ký một lần tại một người nộp thuế."
    },
    {
        "so_dieu": "Điều 31", "ten_luat": "Luật Quản lý thuế 2019",
        "tieu_de": "Khai thuế điện tử bắt buộc",
        "noi_dung": "Doanh nghiệp, tổ chức phải thực hiện khai thuế điện tử. Nộp tờ khai qua Cổng thông tin điện tử của Tổng cục Thuế hoặc qua tổ chức trung gian được ủy quyền.",
        "vi_du": "Công ty không nộp tờ khai VAT tháng qua mạng mà nộp bản giấy — bị từ chối, phải nộp lại online.",
        "biet_them": "Deadline nộp tờ khai VAT tháng: ngày 20 tháng sau. Khai theo quý: ngày 30 tháng đầu quý sau."
    },
    {
        "so_dieu": "Điều 59", "ten_luat": "Luật Quản lý thuế 2019",
        "tieu_de": "Tiền phạt chậm nộp thuế 0,03%/ngày",
        "noi_dung": "Người nộp thuế chậm nộp tiền thuế phải nộp tiền chậm nộp với mức 0,03% số tiền thuế chậm nộp tính trên mỗi ngày chậm nộp.",
        "vi_du": "Chậm nộp thuế 100 triệu trong 30 ngày: tiền phạt = 100tr × 0,03% × 30 = 900.000đ.",
        "biet_them": "Không có mức tối đa — chậm càng lâu phạt càng nhiều. Nên nộp đúng hạn hoặc xin gia hạn."
    },
    {
        "so_dieu": "Điều 110", "ten_luat": "Luật Quản lý thuế 2019",
        "tieu_de": "Hoàn thuế GTGT trong 6 ngày làm việc",
        "noi_dung": "Cơ quan thuế phải quyết định hoàn thuế trong vòng 6 ngày làm việc đối với trường hợp hoàn trước kiểm tra sau. Trường hợp kiểm tra trước hoàn sau: không quá 40 ngày.",
        "vi_du": "Công ty xuất khẩu nộp hồ sơ hoàn thuế GTGT — nếu đủ điều kiện hoàn trước, sẽ nhận tiền trong 6 ngày làm việc.",
        "biet_them": "Doanh nghiệp xuất khẩu thường được hoàn trước kiểm tra sau nếu không có rủi ro cao về thuế."
    },
    {
        "so_dieu": "Điều 3", "ten_luat": "Luật Kế toán 2015",
        "tieu_de": "Đơn vị tiền tệ trong kế toán là VNĐ",
        "noi_dung": "Đơn vị tiền tệ sử dụng trong kế toán là đồng Việt Nam. Trường hợp nghiệp vụ kinh tế phát sinh bằng ngoại tệ phải quy đổi ra đồng Việt Nam theo tỷ giá hối đoái.",
        "vi_du": "Mua hàng từ nước ngoài trả bằng USD — phải quy đổi sang VNĐ theo tỷ giá ngân hàng tại ngày giao dịch để hạch toán.",
        "biet_them": "Chênh lệch tỷ giá hối đoái cuối năm phải được xử lý theo chuẩn mực kế toán VAS 10."
    },
    {
        "so_dieu": "Điều 48", "ten_luat": "Luật Kế toán 2015",
        "tieu_de": "Báo cáo tài chính năm phải kiểm toán",
        "noi_dung": "Doanh nghiệp có vốn đầu tư nước ngoài, tổ chức tín dụng, doanh nghiệp nhà nước bắt buộc phải kiểm toán báo cáo tài chính hàng năm bởi công ty kiểm toán độc lập.",
        "vi_du": "Công ty TNHH có vốn FDI 100% phải thuê công ty kiểm toán như Deloitte, PwC, KPMG... kiểm toán BCTC mỗi năm.",
        "biet_them": "Báo cáo tài chính kiểm toán phải nộp cho cơ quan thuế trong vòng 90 ngày sau khi kết thúc năm tài chính."
    },
    {
        "so_dieu": "Điều 17", "ten_luat": "Luật Thuế GTGT 2024",
        "tieu_de": "Ngưỡng doanh thu chịu thuế GTGT hộ kinh doanh",
        "noi_dung": "Hộ kinh doanh, cá nhân kinh doanh có doanh thu từ 200 triệu đồng/năm trở lên mới thuộc diện chịu thuế GTGT. Dưới ngưỡng này được miễn thuế GTGT.",
        "vi_du": "Chị A bán hàng online doanh thu 150 triệu/năm — không phải nộp thuế GTGT. Nếu đạt 200 triệu thì phải đăng ký nộp.",
        "biet_them": "Ngưỡng này tăng từ 100 triệu (luật cũ) lên 200 triệu theo Luật Thuế GTGT 2024 có hiệu lực 1/1/2026."
    },
    {
        "so_dieu": "Điều 9", "ten_luat": "Luật Thuế TNDN 2008",
        "tieu_de": "Chi phí được trừ khi tính thuế TNDN",
        "noi_dung": "Chi phí được trừ khi tính thuế TNDN là các khoản chi thực tế phát sinh, liên quan đến hoạt động sản xuất kinh doanh, có đủ hóa đơn chứng từ hợp lệ và không thuộc danh mục không được trừ.",
        "vi_du": "Chi phí tiếp khách không có hóa đơn GTGT, hoặc vượt quá 10% tổng chi phí — phần vượt không được trừ khi tính thuế TNDN.",
        "biet_them": "Tiền phạt vi phạm hành chính, tiền nộp phạt do vi phạm hợp đồng thuộc danh mục không được trừ."
    },
    {
        "so_dieu": "Điều 23", "ten_luat": "Luật Thuế TNCN 2007",
        "tieu_de": "Biểu thuế lũy tiến từng phần",
        "noi_dung": "Thu nhập từ tiền lương tiền công áp dụng biểu thuế lũy tiến 7 bậc: 5%, 10%, 15%, 20%, 25%, 30%, 35% tương ứng với các mức thu nhập tính thuế khác nhau.",
        "vi_du": "Thu nhập tính thuế 20 triệu/tháng: 5tr × 5% + 5tr × 10% + 8tr × 15% + 2tr × 20% = 250k + 500k + 1,2tr + 400k = 2,35 triệu thuế.",
        "biet_them": "Thu nhập từ đầu tư vốn, bất động sản, trúng thưởng chịu thuế suất riêng biệt từ 5-10%."
    },
    {
        "so_dieu": "Điều 4", "ten_luat": "Luật Thuế GTGT 2008",
        "tieu_de": "Hàng hóa không chịu thuế GTGT",
        "noi_dung": "26 nhóm hàng hóa dịch vụ không chịu thuế GTGT gồm: sản phẩm nông nghiệp chưa chế biến, máy móc thiết bị nhập khẩu chưa sản xuất được trong nước, dịch vụ y tế, giáo dục, bảo hiểm nhân thọ...",
        "vi_du": "Học sinh mua sách giáo khoa, bệnh nhân trả tiền viện phí — đều không bị cộng thuế GTGT vào giá.",
        "biet_them": "Hàng không chịu thuế GTGT khác với hàng chịu thuế suất 0% — hàng 0% được hoàn thuế đầu vào, hàng không chịu thuế thì không."
    },
    {
        "so_dieu": "Điều 7", "ten_luat": "Luật Thuế GTGT 2008",
        "tieu_de": "Hai phương pháp tính thuế GTGT",
        "noi_dung": "Có 2 phương pháp tính thuế GTGT: (1) Phương pháp khấu trừ (thuế đầu ra trừ thuế đầu vào); (2) Phương pháp trực tiếp (5% hoặc 2% doanh thu tùy ngành).",
        "vi_du": "Hộ kinh doanh nhỏ thường dùng phương pháp trực tiếp: bán dịch vụ ăn uống 100 triệu → nộp GTGT = 100tr × 5% = 5 triệu.",
        "biet_them": "Doanh nghiệp mới thành lập chọn phương pháp khấu trừ nếu có đủ điều kiện — được hoàn thuế đầu vào khi mua sắm ban đầu."
    },
    {
        "so_dieu": "Điều 56", "ten_luat": "Luật Kế toán 2015",
        "tieu_de": "Kỳ kế toán năm từ 1/1 đến 31/12",
        "noi_dung": "Kỳ kế toán năm bắt đầu từ ngày 01/01 và kết thúc ngày 31/12 dương lịch. Doanh nghiệp có thể chọn kỳ kế toán năm khác nhưng phải thông báo cho cơ quan thuế.",
        "vi_du": "Công ty tài chính chọn kỳ kế toán từ 01/4 đến 31/3 năm sau — hợp lệ nhưng phải đăng ký với cơ quan thuế.",
        "biet_them": "Năm tài chính đầu tiên của doanh nghiệp mới thành lập có thể ngắn hơn 12 tháng."
    },
    {
        "so_dieu": "Điều 68", "ten_luat": "Luật Kế toán 2015",
        "tieu_de": "Kế toán trưởng phải có chứng chỉ hành nghề",
        "noi_dung": "Kế toán trưởng doanh nghiệp nhà nước, công ty đại chúng, tổ chức tín dụng phải có chứng chỉ kế toán trưởng do Bộ Tài chính cấp sau khi qua khóa đào tạo và thi sát hạch.",
        "vi_du": "Công ty cổ phần niêm yết bổ nhiệm kế toán trưởng chưa có chứng chỉ — vi phạm quy định, có thể bị xử phạt hành chính.",
        "biet_them": "Chứng chỉ kế toán trưởng phải được cập nhật kiến thức định kỳ để duy trì hiệu lực."
    },
    {
        "so_dieu": "Điều 6", "ten_luat": "Luật Thuế xuất nhập khẩu 2016",
        "tieu_de": "Thời hạn nộp thuế xuất nhập khẩu",
        "noi_dung": "Hàng hóa nhập khẩu để sản xuất xuất khẩu được ân hạn thuế 275 ngày. Hàng nhập khẩu thông thường phải nộp thuế trước khi thông quan hoặc trong 30 ngày.",
        "vi_du": "Công ty may mặc nhập vải về để may áo xuất khẩu — được nợ thuế nhập khẩu tối đa 275 ngày kể từ ngày đăng ký tờ khai.",
        "biet_them": "Quá thời hạn ân hạn mà chưa nộp thuế sẽ bị tính lãi chậm nộp 0,03%/ngày và có thể bị cưỡng chế."
    },
],

# ═══════════════════════════════════════════════════════════════
#  LAO ĐỘNG
# ═══════════════════════════════════════════════════════════════
"lao_dong": [
    {
        "so_dieu": "Điều 112", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Ngày nghỉ hằng năm tối thiểu 12 ngày",
        "noi_dung": "Người lao động làm việc đủ 12 tháng được nghỉ phép năm tối thiểu 12 ngày (làm việc nặng nhọc, độc hại: 14 ngày; đặc biệt nặng nhọc: 16 ngày). Cứ 5 năm thêm 1 ngày.",
        "vi_du": "Nhân viên văn phòng làm đủ 5 năm được nghỉ 13 ngày/năm. Làm đủ 10 năm được nghỉ 14 ngày/năm.",
        "biet_them": "Người sử dụng lao động phải thanh toán tiền lương những ngày chưa nghỉ nếu người lao động thôi việc."
    },
    {
        "so_dieu": "Điều 35", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Quyền đơn phương chấm dứt hợp đồng lao động",
        "noi_dung": "Người lao động có quyền đơn phương chấm dứt hợp đồng bất cứ lúc nào nhưng phải báo trước: 45 ngày (hợp đồng không xác định thời hạn), 30 ngày (hợp đồng 12-36 tháng), 3 ngày (dưới 12 tháng).",
        "vi_du": "Nhân viên ký hợp đồng không thời hạn muốn nghỉ việc phải báo trước 45 ngày — không thể nghỉ ngay lập tức.",
        "biet_them": "Không cần lý do khi đơn phương chấm dứt — đây là quyền cơ bản của người lao động."
    },
    {
        "so_dieu": "Điều 94", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Trả lương đúng hạn — nghĩa vụ bắt buộc",
        "noi_dung": "Người sử dụng lao động phải trả lương trực tiếp, đầy đủ, đúng hạn cho người lao động. Trường hợp đặc biệt không thể trả đúng hạn, không được chậm quá 1 tháng và phải trả thêm lãi suất.",
        "vi_du": "Công ty chậm lương tháng 1 sang tháng 3 phải trả thêm lãi = số tiền lương × lãi suất ngân hàng × số ngày chậm.",
        "biet_them": "Phạt tiền từ 5-10 triệu đồng nếu trả lương chậm theo Nghị định 12/2022/NĐ-CP."
    },
    {
        "so_dieu": "Điều 105", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Thời giờ làm việc tối đa 8 giờ/ngày",
        "noi_dung": "Thời giờ làm việc bình thường không quá 8 giờ/ngày, 48 giờ/tuần. Người sử dụng lao động có quyền quy định làm việc theo ngày hoặc tuần nhưng phải thông báo cho người lao động biết.",
        "vi_du": "Công ty quy định làm 6 ngày/tuần, mỗi ngày 8 tiếng = 48 tiếng/tuần — hợp lệ. Nếu làm 50 tiếng/tuần thì 2 tiếng vượt là làm thêm giờ.",
        "biet_them": "Người làm việc 6 giờ liên tục phải được nghỉ giữa ca ít nhất 30 phút, tính vào giờ làm việc."
    },
    {
        "so_dieu": "Điều 107", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Làm thêm giờ tối đa 40 giờ/tháng",
        "noi_dung": "Tổng số giờ làm thêm không quá 40 giờ/tháng và 200 giờ/năm (một số ngành đặc thù được tối đa 300 giờ/năm). Phải có sự thỏa thuận với người lao động.",
        "vi_du": "Công ty yêu cầu nhân viên làm thêm 50 giờ trong tháng cao điểm mà không có thỏa thuận — vi phạm luật, bị phạt từ 20-40 triệu.",
        "biet_them": "Từ 01/01/2022, giới hạn làm thêm tháng tăng từ 30 lên 40 giờ/tháng. Lương làm thêm tối thiểu 150% ngày thường."
    },
    {
        "so_dieu": "Điều 98", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Lương làm thêm giờ tối thiểu 150%",
        "noi_dung": "Lương làm thêm giờ ngày thường tối thiểu 150%, ngày nghỉ hàng tuần tối thiểu 200%, ngày lễ tết tối thiểu 300% so với lương giờ làm việc bình thường.",
        "vi_du": "Lương giờ bình thường 50.000đ. Làm thêm ngày Tết Nguyên Đán: tối thiểu 50.000 × 300% = 150.000đ/giờ.",
        "biet_them": "Mức 300% đã bao gồm tiền lương ngày lễ. Nếu nghỉ lễ mà đi làm mới được tính thêm phần này."
    },
    {
        "so_dieu": "Điều 134", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Nghỉ thai sản 6 tháng cho lao động nữ",
        "noi_dung": "Lao động nữ sinh con được nghỉ thai sản 6 tháng. Trường hợp sinh đôi trở lên, mỗi con thêm 1 tháng. Trong thời gian nghỉ thai sản, người lao động được hưởng chế độ thai sản từ BHXH.",
        "vi_du": "Chị B sinh đôi được nghỉ thai sản 7 tháng (6 + 1 tháng cho con thứ hai) và nhận 100% lương bình quân 6 tháng trước từ BHXH.",
        "biet_them": "Sau nghỉ thai sản, lao động nữ được bố trí làm việc cũ hoặc công việc tương đương, không được sa thải."
    },
    {
        "so_dieu": "Điều 138", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Lao động nữ không bị sa thải khi mang thai",
        "noi_dung": "Người sử dụng lao động không được sa thải hoặc đơn phương chấm dứt hợp đồng với lao động nữ đang mang thai, nghỉ thai sản, nuôi con dưới 12 tháng tuổi.",
        "vi_du": "Công ty sa thải nhân viên nữ vì lý do đang mang thai — vi phạm nghiêm trọng, phải nhận lại và bồi thường ít nhất 2 tháng lương.",
        "biet_them": "Trừ trường hợp doanh nghiệp chấm dứt hoạt động theo quy định của pháp luật."
    },
    {
        "so_dieu": "Điều 46", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Trợ cấp thôi việc khi chấm dứt hợp đồng",
        "noi_dung": "Người sử dụng lao động phải trả trợ cấp thôi việc cho người lao động đã làm việc thường xuyên từ đủ 12 tháng trở lên: mỗi năm làm việc = 0,5 tháng lương bình quân.",
        "vi_du": "Nhân viên làm 4 năm, lương bình quân 12 tháng cuối = 10 triệu. Trợ cấp thôi việc = 4 × 0,5 × 10 triệu = 20 triệu.",
        "biet_them": "Thời gian làm việc tính trợ cấp không tính thời gian đã tham gia BHXH bắt buộc (đã được tính vào trợ cấp thất nghiệp)."
    },
    {
        "so_dieu": "Điều 36", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Người sử dụng lao động không được đơn phương chấm dứt tùy tiện",
        "noi_dung": "Người sử dụng lao động chỉ được đơn phương chấm dứt hợp đồng trong các trường hợp luật định: NLĐ thường xuyên không hoàn thành công việc, ốm đau kéo dài, thiên tai bất khả kháng, NLĐ không có mặt sau thời hạn...",
        "vi_du": "Công ty sa thải nhân viên vì 'tái cơ cấu' nhưng không đúng trình tự — NLĐ có thể khởi kiện đòi bồi thường.",
        "biet_them": "Sa thải trái luật phải nhận NLĐ trở lại, trả lương trong thời gian bị sa thải và bồi thường thêm ít nhất 2 tháng lương."
    },
    {
        "so_dieu": "Điều 117", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Hợp đồng lao động phải bằng văn bản",
        "noi_dung": "Hợp đồng lao động phải được giao kết bằng văn bản và làm thành 2 bản, mỗi bên giữ 1 bản. Riêng công việc tạm thời dưới 1 tháng có thể giao kết bằng lời nói.",
        "vi_du": "Thuê nhân viên bán hàng bằng miệng rồi cho nghỉ sau 2 tháng — họ vẫn có quyền đòi các quyền lợi như hợp đồng văn bản.",
        "biet_them": "Giao kết hợp đồng qua phương tiện điện tử có giá trị như hợp đồng bằng văn bản theo BLLĐ 2019."
    },
    {
        "so_dieu": "Điều 90", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Lương tối thiểu vùng — sàn không thể thỏa thuận thấp hơn",
        "noi_dung": "Lương tối thiểu là mức thấp nhất mà người sử dụng lao động phải trả cho người lao động làm việc trong điều kiện bình thường. Không được thỏa thuận lương thấp hơn lương tối thiểu vùng.",
        "vi_du": "Năm 2024, lương tối thiểu vùng 1 (Hà Nội, TP.HCM) là 4.960.000đ/tháng. Hợp đồng ghi lương 4 triệu — vô hiệu phần thấp hơn.",
        "biet_them": "Lương tối thiểu điều chỉnh định kỳ theo Nghị định của Chính phủ, thường vào đầu năm."
    },
    {
        "so_dieu": "Điều 149", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Cấm lao động trẻ em dưới 15 tuổi",
        "noi_dung": "Nghiêm cấm sử dụng người dưới 15 tuổi làm việc. Người từ 13-15 tuổi chỉ được làm một số công việc nhẹ nhàng không ảnh hưởng đến sức khỏe và học tập, phải có sự đồng ý của cha mẹ.",
        "vi_du": "Nhà hàng thuê học sinh 14 tuổi rửa bát sau giờ học — vi phạm nếu không có ý kiến phụ huynh và giấy phép của Sở LĐTBXH.",
        "biet_them": "Sử dụng lao động dưới 13 tuổi là vi phạm nghiêm trọng, có thể bị truy cứu trách nhiệm hình sự."
    },
    {
        "so_dieu": "Điều 155", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Người lao động nước ngoài phải có giấy phép lao động",
        "noi_dung": "Người lao động nước ngoài làm việc tại Việt Nam phải có giấy phép lao động do Bộ LĐTBXH hoặc Sở LĐTBXH cấp, trừ một số trường hợp miễn trừ.",
        "vi_du": "Công ty thuê chuyên gia người Nhật làm việc 3 tháng mà không xin giấy phép lao động — bị phạt từ 30-45 triệu đồng.",
        "biet_them": "Giấy phép lao động có hiệu lực tối đa 2 năm, được gia hạn một lần. Nhà quản lý cấp cao có thể xin giấy phép dễ hơn."
    },
    {
        "so_dieu": "Điều 64", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Thử việc không quá 180 ngày",
        "noi_dung": "Thời gian thử việc không quá: 180 ngày với công việc quản lý doanh nghiệp; 60 ngày với công việc có chuyên môn kỹ thuật cao; 30 ngày với các vị trí còn lại.",
        "vi_du": "Công ty cho nhân viên kế toán thử việc 3 tháng — hợp lệ (≤60 ngày với chuyên môn cao). Nếu kéo dài 4 tháng — vi phạm.",
        "biet_them": "Lương thử việc tối thiểu 85% mức lương chính thức. Không được thử việc quá 1 lần với cùng một công việc."
    },
    {
        "so_dieu": "Điều 125", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Kỷ luật sa thải chỉ trong 3 trường hợp",
        "noi_dung": "Sa thải chỉ được áp dụng khi: (1) Trộm cắp, tham ô, cố ý gây thiệt hại nghiêm trọng; (2) Tiết lộ bí mật kinh doanh; (3) Bị xử lý kỷ luật nâng mức mà tái phạm trong thời hạn xử lý.",
        "vi_du": "Nhân viên nghỉ không phép liên tiếp 5 ngày — không phải trường hợp sa thải trực tiếp, phải qua quy trình xử lý kỷ luật từng bước.",
        "biet_them": "Sa thải phải tuân thủ trình tự: họp hội đồng kỷ luật, thông báo trước, có mặt NLĐ và đại diện công đoàn."
    },
    {
        "so_dieu": "Điều 168", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Tham gia BHXH, BHYT, BHTN bắt buộc",
        "noi_dung": "Người lao động làm việc theo hợp đồng lao động từ đủ 1 tháng trở lên bắt buộc tham gia BHXH, BHYT, bảo hiểm thất nghiệp. Người sử dụng lao động đóng phần lớn.",
        "vi_du": "NLĐ đóng BHXH 8%, BHYT 1,5%, BHTN 1% = 10,5% lương. Doanh nghiệp đóng thêm 17,5% BHXH + 3% BHYT + 1% BHTN = 21,5%.",
        "biet_them": "Trốn đóng BHXH bị phạt 12-20% tổng số tiền chưa đóng và trả đủ cho người lao động."
    },
    {
        "so_dieu": "Điều 79", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Đình công phải đúng trình tự",
        "noi_dung": "Người lao động có quyền đình công nhưng phải qua trình tự: hòa giải không thành → trọng tài không thành → ban chấp hành công đoàn ra quyết định đình công với thông báo trước 5 ngày.",
        "vi_du": "Công nhân tự phát bỏ việc tập thể mà không qua trình tự — là đình công bất hợp pháp, thủ lĩnh có thể bị xử lý kỷ luật.",
        "biet_them": "Đình công hợp pháp: doanh nghiệp không được sa thải, trả thù hoặc phân biệt đối xử người tham gia."
    },
    {
        "so_dieu": "Điều 113", "ten_luat": "Bộ luật Lao động 2019",
        "tieu_de": "Nghỉ lễ, Tết được hưởng nguyên lương",
        "noi_dung": "Người lao động được nghỉ làm việc, hưởng nguyên lương trong 11 ngày lễ, tết/năm: Tết Dương lịch 1 ngày, Tết Âm lịch 5 ngày, Giỗ Tổ 1 ngày, Giải phóng 30/4 và Quốc tế 1/5 mỗi 1 ngày, Quốc khánh 2 ngày.",
        "vi_du": "Năm 2025, Tết Nguyên Đán nghỉ từ 28/1 đến 1/2 (5 ngày) được hưởng lương đầy đủ. Nếu đi làm phải trả 300% lương.",
        "biet_them": "Nếu ngày lễ trùng ngày nghỉ hàng tuần, được nghỉ bù vào ngày tiếp theo."
    },
    {
        "so_dieu": "Điều 55", "ten_luat": "Luật BHXH 2024",
        "tieu_de": "Điều kiện hưởng lương hưu giảm xuống 15 năm đóng",
        "noi_dung": "Từ 01/7/2025, người lao động chỉ cần đóng BHXH đủ 15 năm (thay vì 20 năm như trước) và đủ tuổi nghỉ hưu là đủ điều kiện nhận lương hưu hàng tháng.",
        "vi_du": "Người đóng BHXH từ năm 30 tuổi, đến 45 tuổi đã đủ 15 năm — khi đến tuổi nghỉ hưu (60 nữ, 62 nam) sẽ được nhận lương hưu.",
        "biet_them": "Mức lương hưu tối thiểu bằng lương cơ sở. Mức tối đa 75% lương bình quân đóng BHXH."
    },
],

# ═══════════════════════════════════════════════════════════════
#  DÂN SỰ
# ═══════════════════════════════════════════════════════════════
"dan_su": [
    {
        "so_dieu": "Điều 117", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Điều kiện để giao dịch dân sự có hiệu lực",
        "noi_dung": "Giao dịch dân sự có hiệu lực khi: (1) Chủ thể có năng lực pháp luật; (2) Ý chí tự nguyện, không bị lừa dối, cưỡng ép; (3) Mục đích và nội dung không vi phạm điều cấm của pháp luật.",
        "vi_du": "Hợp đồng bán đất do bị ép buộc ký dưới áp lực có thể bị tuyên vô hiệu vì thiếu điều kiện tự nguyện.",
        "biet_them": "Giao dịch vô hiệu không làm phát sinh quyền và nghĩa vụ — các bên phải khôi phục lại tình trạng ban đầu."
    },
    {
        "so_dieu": "Điều 429", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Thời hạn khởi kiện về hợp đồng là 3 năm",
        "noi_dung": "Thời hiệu khởi kiện yêu cầu Tòa án giải quyết tranh chấp hợp đồng là 3 năm kể từ ngày người có quyền yêu cầu biết hoặc phải biết quyền và lợi ích của mình bị vi phạm.",
        "vi_du": "Bạn cho vay tiền tháng 1/2020, đến 1/2023 người vay vẫn chưa trả — hết hạn khởi kiện. Cần kiện trước 1/2023.",
        "biet_them": "Thời hiệu không áp dụng cho tranh chấp về quyền nhân thân, yêu cầu bảo vệ quyền sở hữu."
    },
    {
        "so_dieu": "Điều 584", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Bồi thường thiệt hại ngoài hợp đồng",
        "noi_dung": "Người nào có hành vi xâm phạm tính mạng, sức khỏe, danh dự, nhân phẩm, tài sản của người khác mà gây thiệt hại thì phải bồi thường, trừ trường hợp pháp luật có quy định khác.",
        "vi_du": "Xe máy đang đậu bỗng đổ vào xe ô tô gây hõm — chủ xe máy phải bồi thường thiệt hại dù không cố ý.",
        "biet_them": "Mức bồi thường có thể được giảm nếu người bị thiệt hại cũng có lỗi."
    },
    {
        "so_dieu": "Điều 168", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Quyền sở hữu được pháp luật bảo vệ",
        "noi_dung": "Chủ sở hữu có quyền chiếm hữu, sử dụng, định đoạt tài sản của mình. Không ai có thể bị hạn chế, bị tước đoạt trái luật quyền chiếm hữu, sử dụng, định đoạt tài sản.",
        "vi_du": "Hàng xóm tự ý vào dùng xe của bạn khi bạn đi vắng — dù không gây hư hại, vẫn vi phạm quyền sở hữu.",
        "biet_them": "Chủ sở hữu có quyền đòi lại tài sản từ người chiếm hữu không có căn cứ pháp luật."
    },
    {
        "so_dieu": "Điều 463", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Hợp đồng vay tài sản",
        "noi_dung": "Hợp đồng vay tài sản là sự thỏa thuận giữa các bên, theo đó bên cho vay giao tài sản cho bên vay. Bên vay phải trả lại tài sản cùng loại, đúng số lượng, chất lượng và chỉ phải trả lãi nếu có thỏa thuận.",
        "vi_du": "Cho bạn vay tiền không ghi lãi suất — mặc nhiên là vay không lãi. Muốn tính lãi phải ghi rõ trong giấy vay.",
        "biet_them": "Lãi suất cho vay không được vượt quá 20%/năm theo BLDS 2015. Vượt mức này phần lãi vượt không có hiệu lực."
    },
    {
        "so_dieu": "Điều 472", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Lãi suất cho vay tối đa 20%/năm",
        "noi_dung": "Trường hợp các bên có thỏa thuận về lãi suất thì lãi suất theo thỏa thuận không được vượt quá 20%/năm. Trường hợp lãi suất theo thỏa thuận vượt quá mức này thì mức lãi suất vượt quá không có hiệu lực.",
        "vi_du": "Cho vay 100 triệu với lãi suất 3%/tháng (36%/năm) — chỉ được tính lãi tối đa 20%/năm, phần vượt không có cơ sở đòi.",
        "biet_them": "Cho vay lãi nặng vượt 5 lần mức lãi suất pháp định (>100%/năm) có thể bị truy cứu hình sự theo Điều 201 BLHS."
    },
    {
        "so_dieu": "Điều 320", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Thế chấp tài sản phải đăng ký",
        "noi_dung": "Thế chấp tài sản là dùng tài sản để bảo đảm nghĩa vụ trả nợ. Thế chấp bất động sản phải đăng ký tại cơ quan đăng ký giao dịch bảo đảm mới có hiệu lực đối kháng với người thứ ba.",
        "vi_du": "Thế chấp nhà để vay ngân hàng — ngân hàng phải đăng ký thế chấp tại Văn phòng đăng ký đất đai, nếu không sẽ không có quyền ưu tiên khi xử lý.",
        "biet_them": "Một tài sản có thể thế chấp cho nhiều chủ nợ, ưu tiên thanh toán theo thứ tự đăng ký."
    },
    {
        "so_dieu": "Điều 562", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Hợp đồng tặng cho tài sản",
        "noi_dung": "Hợp đồng tặng cho tài sản là sự thỏa thuận giữa các bên, theo đó bên tặng cho giao tài sản và chuyển quyền sở hữu cho bên được tặng cho mà không yêu cầu đền bù. Tặng cho bất động sản phải công chứng.",
        "vi_du": "Cha tặng cho con mảnh đất — phải lập hợp đồng tặng cho có công chứng và sang tên tại cơ quan đăng ký đất đai.",
        "biet_them": "Tặng cho có điều kiện: bên tặng có thể đặt ra điều kiện, bên được tặng vi phạm điều kiện thì bên tặng có thể đòi lại."
    },
    {
        "so_dieu": "Điều 651", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Thừa kế theo pháp luật — 3 hàng thừa kế",
        "noi_dung": "Hàng thừa kế thứ nhất: vợ/chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi. Hàng thứ hai: ông bà nội ngoại, anh chị em ruột. Hàng thứ ba: cụ nội ngoại, bác, chú, cô, dì, cậu, cháu ruột.",
        "vi_du": "Người chết không để lại di chúc, có vợ và 2 con — tài sản chia đều cho 3 người (mỗi người 1/3). Cha mẹ không được chia vì hàng 1 có người.",
        "biet_them": "Hàng sau chỉ được hưởng khi hàng trước không còn ai hoặc từ chối nhận thừa kế."
    },
    {
        "so_dieu": "Điều 626", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Di chúc hợp pháp cần đủ điều kiện",
        "noi_dung": "Di chúc hợp pháp khi: người lập đủ 18 tuổi, minh mẫn, tự nguyện; nội dung không vi phạm pháp luật; hình thức đúng quy định (tự viết tay hoặc công chứng).",
        "vi_du": "Di chúc viết tay phải do người lập tự viết toàn bộ và ký tên — không được đánh máy, không cần người làm chứng.",
        "biet_them": "Di chúc công chứng cần 2 người làm chứng, ký trước công chứng viên. Di chúc có công chứng có giá trị pháp lý cao hơn."
    },
    {
        "so_dieu": "Điều 644", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Di chúc không thể tước quyền thừa kế bắt buộc",
        "noi_dung": "Những người sau được hưởng di sản bằng 2/3 suất thừa kế theo pháp luật dù không được đề cập trong di chúc: con chưa thành niên, cha mẹ, vợ/chồng, con thành niên mà không có khả năng lao động.",
        "vi_du": "Ông lập di chúc cho cháu toàn bộ tài sản, không nhắc đến con trai tàn tật — con trai vẫn được nhận tối thiểu 2/3 suất luật định.",
        "biet_them": "Đây là quy định bảo vệ người thân thiết, đề phòng trường hợp bị tác động khi lập di chúc."
    },
    {
        "so_dieu": "Điều 236", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Xác lập quyền sở hữu theo thời hiệu chiếm hữu",
        "noi_dung": "Người chiếm hữu không có căn cứ pháp luật nhưng ngay tình, liên tục, công khai trong 30 năm (bất động sản) hoặc 10 năm (động sản) thì được xác lập quyền sở hữu.",
        "vi_du": "Gia đình canh tác mảnh đất bỏ hoang liên tục 30 năm, ngay tình — có thể yêu cầu tòa án công nhận quyền sở hữu.",
        "biet_them": "Phải chiếm hữu liên tục, công khai, không bị phản đối. Nếu bị phủ nhận trong thời gian đó, thời hiệu bị gián đoạn."
    },
    {
        "so_dieu": "Điều 275", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Nghĩa vụ phát sinh từ hợp đồng",
        "noi_dung": "Nghĩa vụ là việc mà theo đó một hoặc nhiều chủ thể (bên có nghĩa vụ) phải chuyển giao vật, chuyển giao quyền, trả tiền hoặc giấy tờ có giá, thực hiện công việc hoặc không thực hiện công việc nhất định.",
        "vi_du": "Ký hợp đồng mua bán: người bán có nghĩa vụ giao hàng, người mua có nghĩa vụ trả tiền — vi phạm một trong hai đều phải bồi thường.",
        "biet_them": "Nghĩa vụ có thể phát sinh từ hợp đồng, hành vi pháp lý đơn phương, gây thiệt hại, được lợi không có căn cứ pháp luật..."
    },
    {
        "so_dieu": "Điều 351", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Vi phạm nghĩa vụ phải bồi thường",
        "noi_dung": "Bên có nghĩa vụ mà vi phạm nghĩa vụ thì phải chịu trách nhiệm dân sự đối với bên có quyền. Vi phạm nghĩa vụ là không thực hiện, thực hiện không đúng hoặc không đầy đủ nghĩa vụ.",
        "vi_du": "Nhà thầu xây nhà không đúng tiến độ — vi phạm nghĩa vụ, chủ nhà có quyền đòi phạt vi phạm và bồi thường thiệt hại.",
        "biet_them": "Bên vi phạm không phải chịu trách nhiệm nếu chứng minh được do sự kiện bất khả kháng (thiên tai, dịch bệnh...)."
    },
    {
        "so_dieu": "Điều 450", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Hợp đồng mua bán tài sản",
        "noi_dung": "Hợp đồng mua bán tài sản là sự thỏa thuận giữa các bên, bên bán chuyển quyền sở hữu tài sản cho bên mua và bên mua trả tiền cho bên bán. Rủi ro tài sản chuyển từ người bán sang người mua kể từ thời điểm chuyển giao.",
        "vi_du": "Mua xe máy, trả tiền xong nhưng chưa lấy xe về — xe bị mưa làm hỏng thì người bán vẫn phải chịu trách nhiệm vì chưa giao xe.",
        "biet_them": "Quyền sở hữu bất động sản chuyển từ thời điểm đăng ký, không phải thời điểm công chứng hay nộp tiền."
    },
    {
        "so_dieu": "Điều 513", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Hợp đồng thuê tài sản",
        "noi_dung": "Bên thuê phải trả tiền thuê đúng thời hạn và sử dụng tài sản đúng mục đích. Bên thuê không được cho thuê lại trừ khi bên cho thuê đồng ý. Sau khi hết hạn phải hoàn trả tài sản đúng tình trạng.",
        "vi_du": "Thuê nhà rồi tự ý cho người khác thuê lại mà không xin phép chủ nhà — chủ nhà có quyền đơn phương chấm dứt hợp đồng.",
        "biet_them": "Bên cho thuê phải sửa chữa tài sản hư hỏng không do lỗi của bên thuê. Nếu không sửa, bên thuê có thể tự sửa và trừ vào tiền thuê."
    },
    {
        "so_dieu": "Điều 596", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Cha mẹ bồi thường thay cho con dưới 15 tuổi",
        "noi_dung": "Cha mẹ phải bồi thường thiệt hại do con chưa đủ 15 tuổi gây ra. Con từ đủ 15 đến dưới 18 tuổi gây thiệt hại thì phải bồi thường bằng tài sản của mình, nếu không đủ thì cha mẹ bồi thường phần còn thiếu.",
        "vi_du": "Bé 10 tuổi đá bóng làm vỡ cửa kính nhà hàng xóm — bố mẹ phải bồi thường toàn bộ thiệt hại.",
        "biet_them": "Nếu con gây thiệt hại khi đang ở trường thì trường học phải bồi thường (trừ khi chứng minh không có lỗi)."
    },
    {
        "so_dieu": "Điều 609", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Bồi thường thiệt hại do súc vật gây ra",
        "noi_dung": "Chủ sở hữu súc vật phải bồi thường thiệt hại do súc vật gây ra. Nếu người thứ ba hoàn toàn có lỗi làm súc vật gây thiệt hại thì người thứ ba phải bồi thường.",
        "vi_du": "Chó nhà bạn cắn người đi đường — bạn phải bồi thường chi phí y tế, thu nhập bị mất và bồi thường tổn thất tinh thần.",
        "biet_them": "Ngay cả khi chó bị thả rông mà người bị cắn tự ý vào nhà, chủ vẫn có thể phải chịu trách nhiệm một phần."
    },
    {
        "so_dieu": "Điều 124", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Giao dịch dân sự giả tạo vô hiệu",
        "noi_dung": "Khi các bên xác lập giao dịch dân sự một cách giả tạo nhằm che giấu một giao dịch khác thì giao dịch giả tạo vô hiệu. Giao dịch bị che giấu có hiệu lực trừ trường hợp nó cũng vi phạm pháp luật.",
        "vi_du": "Hợp đồng tặng cho nhà (để tránh thuế) thực chất là mua bán — hợp đồng tặng cho vô hiệu, giao dịch mua bán thực được xem xét riêng.",
        "biet_them": "Đây là cơ sở pháp lý để cơ quan thuế truy thu thuế khi phát hiện các giao dịch mua bán ngụy trang thành tặng cho."
    },
    {
        "so_dieu": "Điều 155", "ten_luat": "Bộ luật Dân sự 2015",
        "tieu_de": "Một số trường hợp không áp dụng thời hiệu",
        "noi_dung": "Thời hiệu khởi kiện không áp dụng trong các trường hợp: yêu cầu bảo vệ quyền nhân thân không gắn với tài sản; yêu cầu bảo vệ quyền sở hữu trừ trường hợp luật có quy định khác.",
        "vi_du": "Nhà bị lấn chiếm từ 20 năm trước — chủ nhà vẫn có thể kiện đòi lại bất kỳ lúc nào vì quyền sở hữu không bị giới hạn thời hiệu.",
        "biet_them": "Nhưng nếu người chiếm hữu đủ điều kiện xác lập quyền sở hữu theo thời hiệu (30 năm), thì quyền của chủ cũ có thể bị ảnh hưởng."
    },
],

# ═══════════════════════════════════════════════════════════════
#  KINH TẾ & DOANH NGHIỆP
# ═══════════════════════════════════════════════════════════════
"kinh_te": [
    {
        "so_dieu": "Điều 46", "ten_luat": "Luật Doanh nghiệp 2020",
        "tieu_de": "Trách nhiệm hữu hạn của thành viên công ty TNHH",
        "noi_dung": "Thành viên công ty TNHH chịu trách nhiệm về các khoản nợ và nghĩa vụ tài sản khác của doanh nghiệp trong phạm vi số vốn đã góp vào doanh nghiệp.",
        "vi_du": "Bạn góp 500 triệu vào công ty TNHH. Nếu công ty phá sản nợ 2 tỷ, bạn chỉ mất tối đa 500 triệu, không mất tài sản cá nhân.",
        "biet_them": "Đây là ưu điểm lớn nhất của mô hình công ty TNHH so với doanh nghiệp tư nhân."
    },
    {
        "so_dieu": "Điều 25", "ten_luat": "Luật Cạnh tranh 2018",
        "tieu_de": "Cấm thỏa thuận ấn định giá bán",
        "noi_dung": "Các doanh nghiệp cạnh tranh bị nghiêm cấm thỏa thuận ấn định giá hàng hóa, dịch vụ một cách trực tiếp hoặc gián tiếp. Đây là hành vi phản cạnh tranh nghiêm trọng nhất.",
        "vi_du": "3 siêu thị trong khu vực thỏa thuận không bán gạo dưới 20.000đ/kg — vi phạm luật cạnh tranh, bị phạt đến 10% tổng doanh thu.",
        "biet_them": "Cục Quản lý cạnh tranh và Bảo vệ người tiêu dùng (VCCA) chịu trách nhiệm điều tra."
    },
    {
        "so_dieu": "Điều 13", "ten_luat": "Luật Đầu tư 2020",
        "tieu_de": "Bảo đảm quyền sở hữu tài sản của nhà đầu tư",
        "noi_dung": "Nhà nước bảo đảm quyền sở hữu tài sản hợp pháp, vốn đầu tư, thu nhập và các quyền lợi hợp pháp khác của nhà đầu tư. Không quốc hữu hóa hoặc tịch thu tài sản trái pháp luật.",
        "vi_du": "Doanh nghiệp nước ngoài đầu tư vào Việt Nam được bảo đảm không bị sung công tài sản tùy tiện.",
        "biet_them": "Trường hợp nhà nước thu hồi vì lợi ích quốc gia phải bồi thường theo giá thị trường."
    },
    {
        "so_dieu": "Điều 17", "ten_luat": "Luật Doanh nghiệp 2020",
        "tieu_de": "Quyền tự do kinh doanh của doanh nghiệp",
        "noi_dung": "Doanh nghiệp có quyền tự do kinh doanh tất cả ngành nghề mà pháp luật không cấm. Đối với ngành nghề kinh doanh có điều kiện, doanh nghiệp được kinh doanh sau khi đáp ứng đủ điều kiện.",
        "vi_du": "Muốn mở công ty kinh doanh dược phẩm — phải có giấy phép của Bộ Y tế, giấy phép GDP/GSP trước khi hoạt động.",
        "biet_them": "Danh mục ngành nghề kinh doanh có điều kiện gồm 227 ngành theo Phụ lục IV Luật Đầu tư 2020."
    },
    {
        "so_dieu": "Điều 112", "ten_luat": "Luật Doanh nghiệp 2020",
        "tieu_de": "Cổ đông sở hữu 10% có quyền triệu tập ĐHCĐ",
        "noi_dung": "Cổ đông hoặc nhóm cổ đông sở hữu từ 10% tổng số cổ phần phổ thông trở lên có quyền triệu tập họp ĐHCĐ, đề cử người vào HĐQT và Ban kiểm soát.",
        "vi_du": "Nhóm cổ đông nhỏ nắm 12% cổ phần không đồng ý với quyết định của HĐQT — có thể triệu tập ĐHCĐ bất thường để xem xét lại.",
        "biet_them": "Điều lệ công ty có thể quy định tỷ lệ thấp hơn 10% nhưng không được cao hơn."
    },
    {
        "so_dieu": "Điều 208", "ten_luat": "Luật Doanh nghiệp 2020",
        "tieu_de": "Công ty cổ phần có thể phát hành cổ phiếu ưu đãi",
        "noi_dung": "Công ty cổ phần có thể phát hành các loại cổ phần ưu đãi: ưu đãi cổ tức, ưu đãi hoàn lại, ưu đãi biểu quyết, và cổ phần ưu đãi khác theo Điều lệ. Cổ phần ưu đãi biểu quyết chỉ tổ chức được uỷ quyền của Chính phủ mới được nắm.",
        "vi_du": "Startup phát hành cổ phần ưu đãi cổ tức cho nhà đầu tư thiên thần — nhà đầu tư nhận cổ tức ưu tiên trước cổ đông thường.",
        "biet_them": "Cổ phần ưu đãi biểu quyết chỉ tổ chức được ủy quyền của Chính phủ mới được nắm giữ."
    },
    {
        "so_dieu": "Điều 29", "ten_luat": "Luật Cạnh tranh 2018",
        "tieu_de": "Tập trung kinh tế phải thông báo khi đạt ngưỡng",
        "noi_dung": "Doanh nghiệp thực hiện tập trung kinh tế (mua bán, sáp nhập) phải thông báo cho Ủy ban Cạnh tranh Quốc gia nếu tổng tài sản hoặc doanh thu vượt ngưỡng thông báo do Chính phủ quy định.",
        "vi_du": "Tập đoàn A mua lại công ty B có doanh thu 3.000 tỷ — phải thông báo và được Ủy ban Cạnh tranh chấp thuận trước khi hoàn tất thương vụ.",
        "biet_them": "Tập trung kinh tế bị cấm nếu gây tác động hạn chế cạnh tranh đáng kể trên thị trường Việt Nam."
    },
    {
        "so_dieu": "Điều 39", "ten_luat": "Luật Doanh nghiệp 2020",
        "tieu_de": "Con dấu doanh nghiệp — không bắt buộc mẫu",
        "noi_dung": "Doanh nghiệp có quyền quyết định về hình thức, số lượng và nội dung con dấu. Doanh nghiệp có thể có nhiều con dấu với hình thức và nội dung như nhau. Không cần đăng ký mẫu con dấu với cơ quan nhà nước.",
        "vi_du": "Công ty tự thiết kế con dấu với logo riêng mà không cần xin phép — hợp lệ theo Luật Doanh nghiệp 2020.",
        "biet_them": "Đây là cải cách lớn so với trước đây khi phải đăng ký và được cơ quan công an chấp thuận mẫu con dấu."
    },
    {
        "so_dieu": "Điều 204", "ten_luat": "Luật Doanh nghiệp 2020",
        "tieu_de": "Chia cổ tức chỉ khi công ty có lãi",
        "noi_dung": "Công ty cổ phần chỉ được trả cổ tức cho cổ đông khi công ty đã hoàn thành nghĩa vụ thuế và các nghĩa vụ tài chính khác, đảm bảo thanh toán đủ các khoản nợ và nghĩa vụ tài sản đến hạn.",
        "vi_du": "Công ty lỗ nhưng HĐQT vẫn quyết định chia cổ tức — vi phạm luật, thành viên HĐQT phải chịu trách nhiệm liên đới.",
        "biet_them": "Cổ tức phải được trả trong vòng 6 tháng kể từ ngày kết thúc cuộc họp ĐHCĐ thông qua quyết định trả cổ tức."
    },
    {
        "so_dieu": "Điều 47", "ten_luat": "Luật Đầu tư 2020",
        "tieu_de": "Thủ tục thành lập doanh nghiệp tối đa 3 ngày",
        "noi_dung": "Cơ quan đăng ký kinh doanh phải cấp Giấy chứng nhận đăng ký doanh nghiệp trong vòng 3 ngày làm việc kể từ khi nhận đủ hồ sơ hợp lệ.",
        "vi_du": "Nộp hồ sơ đăng ký thành lập công ty TNHH trực tuyến thứ Hai — chứa nhật muộn nhất phải được cấp giấy đăng ký.",
        "biet_them": "Hiện nay có thể đăng ký trực tuyến 100% qua Cổng thông tin quốc gia về đăng ký doanh nghiệp: dangkykinhdoanh.gov.vn."
    },
    {
        "so_dieu": "Điều 45", "ten_luat": "Luật Cạnh tranh 2018",
        "tieu_de": "Bán hàng dưới giá thành để triệt tiêu đối thủ là vi phạm",
        "noi_dung": "Hành vi bán hàng hóa dưới giá thành toàn bộ nhằm loại bỏ đối thủ cạnh tranh là hành vi lạm dụng vị trí thống lĩnh thị trường, bị nghiêm cấm.",
        "vi_du": "Grab/Gojek giảm giá cuốc xe xuống 0đ trong thời gian dài để diệt đối thủ — có thể bị điều tra vi phạm luật cạnh tranh.",
        "biet_them": "Cần phân biệt: khuyến mãi có thời hạn hợp lệ vs bán dưới giá thành liên tục với mục đích loại bỏ đối thủ."
    },
    {
        "so_dieu": "Điều 55", "ten_luat": "Luật Doanh nghiệp 2020",
        "tieu_de": "Hợp đồng với người liên quan phải được HĐTV chấp thuận",
        "noi_dung": "Hợp đồng, giao dịch giữa công ty với thành viên HĐTV, Giám đốc hoặc người liên quan của những người này phải được HĐTV chấp thuận với đa số phiếu của thành viên không có lợi ích liên quan.",
        "vi_du": "Giám đốc muốn ký hợp đồng thuê văn phòng của công ty vợ mình — phải báo cáo HĐTV và được đa số phiếu chấp thuận.",
        "biet_them": "Vi phạm quy định này, hợp đồng có thể bị tuyên vô hiệu và người ký phải bồi thường thiệt hại cho công ty."
    },
    {
        "so_dieu": "Điều 214", "ten_luat": "Luật Doanh nghiệp 2020",
        "tieu_de": "Giải thể doanh nghiệp phải thanh toán hết nợ",
        "noi_dung": "Doanh nghiệp chỉ được giải thể khi đảm bảo thanh toán hết các khoản nợ và nghĩa vụ tài sản khác. Sau khi thanh lý tài sản và trả hết nợ mới được xóa tên trong đăng ký kinh doanh.",
        "vi_du": "Công ty muốn giải thể nhưng còn nợ nhà cung cấp 500 triệu — không được giải thể cho đến khi trả hết nợ.",
        "biet_them": "Nếu không đủ tài sản để trả nợ, phải tiến hành phá sản theo Luật Phá sản 2014 thay vì giải thể."
    },
    {
        "so_dieu": "Điều 6", "ten_luat": "Luật Phá sản 2014",
        "tieu_de": "Doanh nghiệp mất khả năng thanh toán có thể bị mở thủ tục phá sản",
        "noi_dung": "Doanh nghiệp mất khả năng thanh toán là doanh nghiệp không thực hiện nghĩa vụ thanh toán khoản nợ trong thời hạn 3 tháng kể từ ngày đến hạn thanh toán.",
        "vi_du": "Công ty nợ nhà cung cấp 200 triệu quá hạn 4 tháng — chủ nợ có quyền nộp đơn yêu cầu Tòa án mở thủ tục phá sản.",
        "biet_them": "Bản thân doanh nghiệp, chủ nợ hoặc người lao động đều có quyền nộp đơn yêu cầu mở thủ tục phá sản."
    },
    {
        "so_dieu": "Điều 12", "ten_luat": "Luật Thương mại 2005",
        "tieu_de": "Thương nhân phải đăng ký kinh doanh",
        "noi_dung": "Thương nhân bao gồm tổ chức kinh tế được thành lập hợp pháp, cá nhân hoạt động thương mại một cách độc lập, thường xuyên và có đăng ký kinh doanh.",
        "vi_du": "Người buôn bán tại chợ thường xuyên, có thu nhập ổn định từ việc buôn bán — là thương nhân, phải đăng ký hộ kinh doanh.",
        "biet_them": "Cá nhân hoạt động thương mại nhỏ lẻ không thường xuyên được miễn đăng ký kinh doanh nhưng vẫn phải nộp thuế."
    },
    {
        "so_dieu": "Điều 292", "ten_luat": "Luật Thương mại 2005",
        "tieu_de": "Phạt vi phạm hợp đồng thương mại tối đa 8%",
        "noi_dung": "Mức phạt vi phạm hợp đồng trong thương mại do các bên thỏa thuận nhưng không vượt quá 8% giá trị phần nghĩa vụ hợp đồng bị vi phạm.",
        "vi_du": "Hợp đồng xây dựng 1 tỷ, điều khoản phạt vi phạm giao hàng muộn 10% — chỉ có hiệu lực tối đa 8%, phần vượt (2%) không có giá trị.",
        "biet_them": "Phạt vi phạm và bồi thường thiệt hại là 2 chế tài khác nhau, có thể áp dụng đồng thời nếu hợp đồng có quy định."
    },
    {
        "so_dieu": "Điều 318", "ten_luat": "Luật Thương mại 2005",
        "tieu_de": "Tạm ngừng thực hiện hợp đồng khi đối tác vi phạm",
        "noi_dung": "Một bên có quyền tạm ngừng thực hiện hợp đồng nếu bên kia vi phạm cơ bản hợp đồng. Bên tạm ngừng phải thông báo ngay cho bên kia biết về việc tạm ngừng và lý do.",
        "vi_du": "Bên mua không thanh toán tiền hàng đợt 1 — bên bán có quyền dừng giao hàng đợt 2, 3 cho đến khi được thanh toán.",
        "biet_them": "Tạm ngừng hợp đồng khác hủy hợp đồng — hợp đồng vẫn còn hiệu lực, chỉ tạm dừng việc thực hiện."
    },
    {
        "so_dieu": "Điều 339", "ten_luat": "Luật Thương mại 2005",
        "tieu_de": "Bất khả kháng — miễn trách nhiệm vi phạm",
        "noi_dung": "Bên vi phạm hợp đồng được miễn trách nhiệm nếu sự vi phạm do sự kiện bất khả kháng: không thể lường trước, không thể khắc phục được, xảy ra sau khi ký hợp đồng.",
        "vi_du": "Nhà máy bị bão lũ không thể giao hàng đúng hạn — được miễn phạt vi phạm nếu thông báo kịp thời và cung cấp bằng chứng.",
        "biet_them": "Phải thông báo ngay khi xảy ra sự kiện bất khả kháng. Nếu thông báo chậm, vẫn phải bồi thường phần thiệt hại do thông báo chậm gây ra."
    },
    {
        "so_dieu": "Điều 3", "ten_luat": "Luật Doanh nghiệp 2020",
        "tieu_de": "4 loại hình doanh nghiệp tại Việt Nam",
        "noi_dung": "Pháp luật Việt Nam công nhận 4 loại hình: (1) Doanh nghiệp tư nhân; (2) Công ty hợp danh; (3) Công ty TNHH (1 thành viên hoặc 2+ thành viên); (4) Công ty cổ phần.",
        "vi_du": "Khởi nghiệp solo: chọn DNTN (đơn giản) hoặc Công ty TNHH 1TV (bảo vệ tài sản cá nhân). Muốn huy động vốn rộng: chọn Công ty CP.",
        "biet_them": "DNTN không được phát hành chứng khoán, chủ DNTN chịu trách nhiệm vô hạn bằng toàn bộ tài sản."
    },
    {
        "so_dieu": "Điều 8", "ten_luat": "Luật Đầu tư 2020",
        "tieu_de": "Danh mục ngành nghề cấm đầu tư kinh doanh",
        "noi_dung": "Cấm đầu tư kinh doanh các ngành: kinh doanh chất ma túy, kinh doanh các loài động vật hoang dã nguy cấp, mại dâm, mua bán người, kinh doanh pháo nổ, đòi nợ thuê...",
        "vi_du": "Dịch vụ đòi nợ thuê bị cấm từ 01/01/2021 theo Luật Đầu tư 2020 — các công ty đang hoạt động phải chuyển đổi hoặc giải thể.",
        "biet_them": "Danh mục cấm đầu tư được quy định tại Điều 8 và Phụ lục I Luật Đầu tư 2020, cập nhật theo từng thời kỳ."
    },
],

# ═══════════════════════════════════════════════════════════════
#  HÔN NHÂN GIA ĐÌNH
# ═══════════════════════════════════════════════════════════════
"hon_nhan": [
    {
        "so_dieu": "Điều 8", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Điều kiện kết hôn hợp lệ",
        "noi_dung": "Nam từ đủ 20 tuổi, nữ từ đủ 18 tuổi. Việc kết hôn do nam và nữ tự nguyện quyết định. Không bị mất năng lực hành vi dân sự. Không thuộc trường hợp bị cấm kết hôn.",
        "vi_du": "Cặp đôi 19 tuổi (nam) và 17 tuổi (nữ) không thể đăng ký kết hôn hợp lệ — thiếu điều kiện về tuổi.",
        "biet_them": "Kết hôn không đủ điều kiện sẽ bị hủy, không làm phát sinh quyền và nghĩa vụ vợ chồng."
    },
    {
        "so_dieu": "Điều 33", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Tài sản chung của vợ chồng",
        "noi_dung": "Tài sản chung bao gồm tài sản do vợ, chồng tạo ra, thu nhập từ lao động, kinh doanh, hoa lợi, lợi tức phát sinh trong thời kỳ hôn nhân. Việc định đoạt tài sản chung cần sự đồng ý của cả hai.",
        "vi_du": "Chồng bán mảnh đất (tài sản chung) mà không có chữ ký vợ — hợp đồng mua bán có thể bị vô hiệu.",
        "biet_them": "Vợ chồng có thể lập hôn ước (thỏa thuận tài sản trước hôn nhân) theo Điều 47-50."
    },
    {
        "so_dieu": "Điều 56", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Ly hôn đơn phương khi bạo lực gia đình",
        "noi_dung": "Một bên vợ hoặc chồng có quyền yêu cầu Tòa án giải quyết ly hôn nếu bạo lực gia đình nghiêm trọng, ngược đãi, hành hạ khiến cuộc sống chung không thể kéo dài.",
        "vi_du": "Người vợ bị chồng đánh đập có bằng chứng (giám định thương tích, biên bản công an) có thể đơn phương ly hôn.",
        "biet_them": "Không cần đồng thuận của bên kia khi có căn cứ ly hôn — Tòa sẽ xem xét và quyết định."
    },
    {
        "so_dieu": "Điều 10", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Các trường hợp cấm kết hôn",
        "noi_dung": "Cấm kết hôn giữa: người đang có vợ/chồng; người mất năng lực hành vi dân sự; người cùng dòng máu trực hệ; anh chị em ruột; anh chị em cùng cha khác mẹ hoặc cùng mẹ khác cha; cha mẹ nuôi với con nuôi.",
        "vi_du": "Anh họ (bác ruột — cháu ruột) kết hôn — vi phạm vì là người có họ hàng trong phạm vi 3 đời theo phong tục.",
        "biet_them": "Người đang có vợ hoặc có chồng mà kết hôn hoặc chung sống như vợ chồng với người khác có thể bị truy cứu hình sự."
    },
    {
        "so_dieu": "Điều 48", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Hôn ước — thỏa thuận tài sản trước hôn nhân",
        "noi_dung": "Trước khi kết hôn, nam nữ có quyền lập văn bản thỏa thuận chế độ tài sản. Hôn ước phải được công chứng và có hiệu lực từ ngày đăng ký kết hôn.",
        "vi_du": "Cặp đôi thỏa thuận tài sản riêng của mỗi người trước hôn nhân vẫn là tài sản riêng dù kết hôn — hợp lệ nếu lập hôn ước có công chứng.",
        "biet_them": "Hôn ước là quy định mới của Luật HN&GĐ 2014, trước đây Việt Nam không có chế định này."
    },
    {
        "so_dieu": "Điều 35", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Tài sản riêng của vợ hoặc chồng",
        "noi_dung": "Tài sản riêng gồm: tài sản có trước khi kết hôn; tài sản được thừa kế riêng, được tặng cho riêng trong thời kỳ hôn nhân; tài sản phục vụ nhu cầu thiết yếu của riêng mình; tài sản được thỏa thuận là tài sản riêng.",
        "vi_du": "Vợ được bố mẹ tặng cho riêng căn hộ trong thời kỳ hôn nhân — đây là tài sản riêng của vợ, chồng không có quyền định đoạt.",
        "biet_them": "Hoa lợi, lợi tức phát sinh từ tài sản riêng trong thời kỳ hôn nhân là tài sản chung, trừ khi có thỏa thuận khác."
    },
    {
        "so_dieu": "Điều 81", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Quyền nuôi con sau ly hôn",
        "noi_dung": "Sau ly hôn, vợ chồng thỏa thuận về người trực tiếp nuôi con. Nếu không thỏa thuận được, Tòa án quyết định giao con cho một bên nuôi dựa trên lợi ích tốt nhất của con. Con dưới 36 tháng tuổi được giao cho mẹ nuôi.",
        "vi_du": "Con 2 tuổi: mặc định giao mẹ nuôi trừ khi mẹ không đủ điều kiện. Con 7 tuổi: Tòa xem xét nguyện vọng của con và điều kiện của cả hai bên.",
        "biet_them": "Con từ đủ 7 tuổi trở lên, Tòa án phải lấy ý kiến của con trước khi quyết định giao cho bên nào nuôi."
    },
    {
        "so_dieu": "Điều 82", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Nghĩa vụ cấp dưỡng nuôi con sau ly hôn",
        "noi_dung": "Cha hoặc mẹ không trực tiếp nuôi con phải có nghĩa vụ cấp dưỡng cho con. Mức cấp dưỡng do các bên thỏa thuận; nếu không thỏa thuận được, Tòa quyết định căn cứ vào thu nhập và nhu cầu thực tế của con.",
        "vi_du": "Sau ly hôn, chồng không nuôi con nhưng từ chối cấp dưỡng — vợ có thể yêu cầu Tòa cưỡng chế thi hành, khấu trừ từ lương chồng.",
        "biet_them": "Nghĩa vụ cấp dưỡng kéo dài đến khi con đủ 18 tuổi hoặc đến khi con có thu nhập ổn định nếu con thành niên mà không có khả năng lao động."
    },
    {
        "so_dieu": "Điều 59", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Chia tài sản khi ly hôn",
        "noi_dung": "Tài sản chung được chia đôi, có xét đến công sức đóng góp của mỗi bên, hoàn cảnh gia đình, tình trạng tài sản. Tài sản riêng của bên nào thì bên đó giữ.",
        "vi_du": "Vợ ở nhà nội trợ không có thu nhập — vẫn được chia 1/2 tài sản chung vì công sức nội trợ được pháp luật công nhận.",
        "biet_them": "Bên khó khăn hơn sau ly hôn có thể được chia nhiều hơn. Bên có lỗi dẫn đến ly hôn có thể bị chia ít hơn."
    },
    {
        "so_dieu": "Điều 57", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Thuận tình ly hôn — nhanh hơn ly hôn đơn phương",
        "noi_dung": "Khi vợ chồng cùng yêu cầu ly hôn và thỏa thuận được về tài sản, con cái, Tòa án công nhận thuận tình ly hôn. Thủ tục đơn giản hơn, thường giải quyết trong 1-2 tháng.",
        "vi_du": "Vợ chồng đồng ý ly hôn, thỏa thuận xong tài sản và nuôi con — nộp đơn thuận tình ly hôn, Tòa ra quyết định mà không cần xét xử.",
        "biet_them": "Không hòa giải thành tại Tòa thì mới tiến hành xét xử. Hòa giải là bước bắt buộc trước khi Tòa giải quyết."
    },
    {
        "so_dieu": "Điều 74", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Nuôi con nuôi phải đăng ký tại cơ quan nhà nước",
        "noi_dung": "Việc nhận nuôi con nuôi phải được đăng ký tại UBND cấp xã nơi thường trú của cha mẹ nuôi hoặc con nuôi. Chưa đăng ký thì không phát sinh quan hệ cha mẹ nuôi — con nuôi theo pháp luật.",
        "vi_du": "Nuôi trẻ từ nhỏ như con ruột nhưng không đăng ký — về pháp lý không phải con nuôi, không được thừa kế theo hàng thừa kế.",
        "biet_them": "Người nhận con nuôi phải hơn con nuôi ít nhất 20 tuổi. Một người chỉ được làm con nuôi của một người độc thân hoặc của hai vợ chồng."
    },
    {
        "so_dieu": "Điều 107", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Nghĩa vụ cấp dưỡng giữa anh chị em",
        "noi_dung": "Anh, chị, em có nghĩa vụ cấp dưỡng cho nhau nếu không còn cha mẹ hoặc cha mẹ không có khả năng lao động và không có tài sản để cấp dưỡng, mà người cần cấp dưỡng là người chưa thành niên hoặc không có khả năng lao động.",
        "vi_du": "Cha mẹ mất sớm, anh trai có thu nhập ổn định trong khi em gái còn học đại học — anh có nghĩa vụ hỗ trợ em theo quy định.",
        "biet_them": "Người có nghĩa vụ cấp dưỡng mà trốn tránh có thể bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự."
    },
    {
        "so_dieu": "Điều 113", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Cha mẹ phải cấp dưỡng nuôi con khi không sống cùng",
        "noi_dung": "Cha mẹ không sống chung với con phải thực hiện nghĩa vụ cấp dưỡng theo khả năng kinh tế. Mức cấp dưỡng tối thiểu phải đáp ứng nhu cầu thiết yếu của con về ăn, ở, học hành, chăm sóc sức khỏe.",
        "vi_du": "Cha đi làm ăn xa, không cấp tiền cho mẹ nuôi con — mẹ có quyền yêu cầu Tòa án buộc cha phải cấp dưỡng.",
        "biet_them": "Khác với cấp dưỡng sau ly hôn — đây áp dụng ngay cả khi vợ chồng chưa ly hôn nhưng không sống cùng."
    },
    {
        "so_dieu": "Điều 64", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Xác định cha mẹ cho con ngoài giá thú",
        "noi_dung": "Con sinh ra trong thời kỳ hôn nhân hoặc do người vợ có thai trong thời kỳ hôn nhân là con chung của vợ chồng. Con sinh ngoài giá thú được xác định cha qua thỏa thuận, thừa nhận hoặc quyết định của Tòa án.",
        "vi_du": "Người đàn ông phủ nhận là cha của đứa trẻ — mẹ hoặc đứa trẻ có quyền yêu cầu Tòa án xác định cha bằng xét nghiệm ADN.",
        "biet_them": "Kết quả xét nghiệm ADN được Tòa án chấp nhận là bằng chứng quan trọng trong các vụ kiện xác định cha mẹ con."
    },
    {
        "so_dieu": "Điều 21", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Kết hôn giữa người Việt Nam và người nước ngoài",
        "noi_dung": "Kết hôn có yếu tố nước ngoài phải tuân theo pháp luật Việt Nam về điều kiện kết hôn và thủ tục đăng ký. Người nước ngoài kết hôn tại Việt Nam cần đủ điều kiện theo pháp luật nước họ và pháp luật Việt Nam.",
        "vi_du": "Người Việt kết hôn với người Hàn Quốc tại Việt Nam — đăng ký tại Sở Tư pháp tỉnh/thành phố, cần giấy tờ chứng minh độc thân từ nước ngoài hợp pháp hóa lãnh sự.",
        "biet_them": "Hôn nhân giả để bảo lãnh định cư nước ngoài là hành vi lừa đảo, có thể bị xử lý hình sự."
    },
    {
        "so_dieu": "Điều 5", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Bảo vệ chế độ hôn nhân một vợ một chồng",
        "noi_dung": "Nhà nước bảo hộ hôn nhân và gia đình, bảo vệ quyền và lợi ích hợp pháp của các thành viên gia đình. Nghiêm cấm tảo hôn, cưỡng ép kết hôn, lừa dối kết hôn, cản trở kết hôn hợp pháp.",
        "vi_du": "Ép buộc con gái 16 tuổi lấy chồng theo phong tục địa phương (tảo hôn) — cha mẹ có thể bị xử phạt hành chính từ 1-3 triệu đồng.",
        "biet_them": "Tái phạm tảo hôn có thể bị xử lý hình sự. Toà án có thể hủy hôn nhân tảo hôn theo yêu cầu."
    },
    {
        "so_dieu": "Điều 29", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Quyền bình đẳng giữa vợ và chồng",
        "noi_dung": "Vợ, chồng bình đẳng với nhau, có quyền, nghĩa vụ ngang nhau về mọi mặt trong gia đình, trong việc thực hiện các quyền, nghĩa vụ của công dân. Vợ có quyền mang họ cha hoặc tiếp tục mang họ của mình.",
        "vi_du": "Chồng không được tự ý quyết định chuyển nhà gia đình đến địa chỉ khác mà không có ý kiến vợ — vi phạm quyền bình đẳng.",
        "biet_them": "Bạo lực gia đình là hành vi vi phạm nghiêm trọng, bị xử lý theo Luật Phòng chống bạo lực gia đình 2022."
    },
    {
        "so_dieu": "Điều 54", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Hòa giải trước khi Tòa xét xử ly hôn",
        "noi_dung": "Trước khi thụ lý hoặc tại phiên tòa xét xử, Tòa án tiến hành hòa giải để vợ chồng đoàn tụ. Nếu hòa giải thành, Tòa đình chỉ giải quyết vụ án. Nếu hòa giải không thành mới tiến hành xét xử.",
        "vi_du": "Vợ nộp đơn ly hôn — Tòa triệu tập hòa giải, hai bên đồng ý ở lại với nhau — Tòa ra quyết định đình chỉ, không ly hôn.",
        "biet_them": "Hòa giải là bước bắt buộc dù là ly hôn đơn phương hay thuận tình. Nếu bên kia vắng mặt có lý do, Tòa có thể hòa giải vắng mặt."
    },
    {
        "so_dieu": "Điều 66", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Giám hộ cho người mất năng lực hành vi",
        "noi_dung": "Người mất năng lực hành vi dân sự cần có người giám hộ. Ưu tiên: vợ/chồng, cha/mẹ, con thành niên, anh/chị/em. Người giám hộ phải bảo vệ quyền, lợi ích hợp pháp của người được giám hộ.",
        "vi_du": "Chồng bị tai nạn mất khả năng nhận thức — vợ đương nhiên là người giám hộ, có thể thực hiện các giao dịch thay chồng sau khi Tòa tuyên bố mất NLHVDS.",
        "biet_them": "Người giám hộ phải lập danh sách tài sản của người được giám hộ khi bắt đầu giám hộ, quản lý tài sản theo quy định."
    },
    {
        "so_dieu": "Điều 73", "ten_luat": "Luật Hôn nhân và Gia đình 2014",
        "tieu_de": "Cha mẹ không được cản trở quyền thăm con sau ly hôn",
        "noi_dung": "Sau khi ly hôn, người không trực tiếp nuôi con có quyền thăm nom con; không ai được cản trở người đó thực hiện quyền này. Người cản trở có thể bị xử phạt theo pháp luật.",
        "vi_du": "Vợ nuôi con sau ly hôn, cố tình không cho chồng gặp con vào cuối tuần — chồng có thể yêu cầu Tòa án can thiệp buộc thi hành.",
        "biet_them": "Nếu việc thăm nom con ảnh hưởng nghiêm trọng đến lợi ích của con, Tòa có thể hạn chế quyền thăm nom."
    },
],

# ═══════════════════════════════════════════════════════════════
#  GIÁO DỤC
# ═══════════════════════════════════════════════════════════════
"giao_duc": [
    {
        "so_dieu": "Điều 11", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Phổ cập giáo dục bắt buộc đến THCS",
        "noi_dung": "Nhà nước thực hiện phổ cập giáo dục mầm non cho trẻ 5 tuổi, phổ cập giáo dục tiểu học và phổ cập giáo dục THCS. Gia đình có trách nhiệm tạo điều kiện cho thành viên trong độ tuổi đi học đúng quy định.",
        "vi_du": "Cha mẹ không cho con đến trường tiểu học có thể bị cơ quan chức năng nhắc nhở và xử phạt vi phạm hành chính.",
        "biet_them": "Nhà nước hỗ trợ học phí cho học sinh THCS công lập, đảm bảo mọi trẻ em đều được học."
    },
    {
        "so_dieu": "Điều 83", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Học phí phải công khai, minh bạch",
        "noi_dung": "Cơ sở giáo dục công lập không được thu các khoản ngoài quy định của pháp luật. Học phí phải được công khai, minh bạch. Nghiêm cấm thu tiền học thêm bắt buộc trong giờ chính khóa.",
        "vi_du": "Trường công thu tiền 'quỹ lớp' không rõ mục đích, phụ huynh có quyền yêu cầu giải trình và tố cáo nếu sai quy định.",
        "biet_them": "Đường dây nóng Bộ GD&ĐT: 1800.9090 để phản ánh thu tiền trái quy định."
    },
    {
        "so_dieu": "Điều 69", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Quyền và nghĩa vụ của người học",
        "noi_dung": "Người học có quyền được học tập, tiếp cận thông tin học tập, tham gia các hoạt động giáo dục. Có quyền được đánh giá khách quan, được bảo vệ trước mọi hành vi bạo lực, phân biệt đối xử.",
        "vi_du": "Giáo viên xúc phạm học sinh bằng ngôn từ thô tục — học sinh và phụ huynh có thể khiếu nại lên hiệu trưởng hoặc Phòng GD&ĐT.",
        "biet_them": "Nhà trường phải có cơ chế tiếp nhận khiếu nại từ học sinh và phụ huynh."
    },
    {
        "so_dieu": "Điều 72", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Nhà giáo được bảo vệ nhân phẩm, danh dự",
        "noi_dung": "Nhà giáo có quyền được tôn trọng, bảo vệ nhân phẩm, danh dự và thân thể. Được hưởng lương, phụ cấp ưu đãi theo quy định. Được đào tạo nâng cao trình độ chuyên môn.",
        "vi_du": "Phụ huynh lăng mạ, xúc phạm giáo viên trong trường — vi phạm pháp luật, có thể bị xử phạt hành chính hoặc truy cứu hình sự về tội làm nhục người khác.",
        "biet_them": "Giáo viên cũng có nghĩa vụ: không xúc phạm, không bạo lực học sinh, không dạy thêm trái quy định."
    },
    {
        "so_dieu": "Điều 22", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Hệ thống giáo dục quốc dân 5 cấp",
        "noi_dung": "Hệ thống giáo dục quốc dân gồm: giáo dục mầm non (nhà trẻ + mẫu giáo), giáo dục phổ thông (tiểu học + THCS + THPT), giáo dục nghề nghiệp, giáo dục đại học, giáo dục thường xuyên.",
        "vi_du": "Học sinh học xong THCS có thể chọn: học THPT hoặc học nghề (trung cấp nghề 2-3 năm) — cả hai đều thuộc hệ thống giáo dục quốc dân.",
        "biet_them": "Văn bằng giáo dục nghề nghiệp và giáo dục đại học có giá trị pháp lý ngang nhau trong hệ thống tuyển dụng nhà nước."
    },
    {
        "so_dieu": "Điều 55", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Giáo viên tư thục có quyền ngang giáo viên công lập",
        "noi_dung": "Nhà giáo trong cơ sở giáo dục tư thục có quyền và nghĩa vụ như nhà giáo trong cơ sở giáo dục công lập, trừ quy định về chế độ công chức viên chức.",
        "vi_du": "Giáo viên trường tư có quyền tham gia hội đồng trường, được đào tạo bồi dưỡng, được phong danh hiệu như giáo viên giỏi như trường công.",
        "biet_them": "Trường tư phải đóng BHXH, BHYT cho giáo viên theo đúng quy định của Luật Lao động."
    },
    {
        "so_dieu": "Điều 99", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Cơ sở giáo dục phải công khai điều kiện đảm bảo chất lượng",
        "noi_dung": "Cơ sở giáo dục phải công khai mục tiêu, chương trình giáo dục, điều kiện đảm bảo chất lượng giáo dục, kết quả kiểm định, học phí và các khoản thu khác trên trang web của trường.",
        "vi_du": "Trường đại học không công khai tỷ lệ sinh viên có việc làm sau tốt nghiệp trên website — vi phạm nghĩa vụ minh bạch thông tin.",
        "biet_them": "Phụ huynh và học sinh có quyền yêu cầu nhà trường cung cấp thông tin về chất lượng giảng dạy."
    },
    {
        "so_dieu": "Điều 106", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Kiểm định chất lượng giáo dục định kỳ",
        "noi_dung": "Cơ sở giáo dục phải được kiểm định chất lượng định kỳ để duy trì và nâng cao chất lượng giáo dục. Kết quả kiểm định phải được công bố công khai.",
        "vi_du": "Trường đại học không qua kiểm định hoặc kiểm định không đạt — không được tuyển sinh, bị đình chỉ hoạt động.",
        "biet_them": "Cục Kiểm định chất lượng giáo dục (Bộ GD&ĐT) quản lý các tổ chức kiểm định được công nhận."
    },
    {
        "so_dieu": "Điều 14", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Cấm phân biệt đối xử trong giáo dục",
        "noi_dung": "Nghiêm cấm phân biệt đối xử người học theo giới tính, dân tộc, tôn giáo, hoàn cảnh gia đình. Mọi người đều bình đẳng trong tiếp cận giáo dục. Người khuyết tật được ưu tiên hỗ trợ.",
        "vi_du": "Trường từ chối nhận học sinh vì lý do dân tộc thiểu số, khuyết tật — vi phạm nghiêm trọng Luật Giáo dục và Luật Người khuyết tật.",
        "biet_them": "Học sinh khuyết tật được học hòa nhập và nhà nước hỗ trợ chi phí học tập theo Luật Người khuyết tật 2010."
    },
    {
        "so_dieu": "Điều 37", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Giáo dục tiểu học là bắt buộc và miễn phí",
        "noi_dung": "Giáo dục tiểu học là cấp học bắt buộc. Học sinh tiểu học trong các cơ sở giáo dục công lập không phải đóng học phí. Nhà nước đảm bảo điều kiện cho mọi trẻ em hoàn thành giáo dục tiểu học.",
        "vi_du": "Trường tiểu học công lập thu học phí — vi phạm pháp luật. Phụ huynh có quyền từ chối và khiếu nại.",
        "biet_them": "Miễn học phí cũng áp dụng cho học sinh THCS công lập theo Nghị định 81/2021/NĐ-CP."
    },
    {
        "so_dieu": "Điều 61", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Giảng viên đại học phải có bằng thạc sĩ",
        "noi_dung": "Giảng viên đại học phải có bằng tốt nghiệp đại học trở lên và có chứng chỉ bồi dưỡng nghiệp vụ sư phạm. Giảng viên giảng dạy trình độ đại học phải có bằng thạc sĩ trở lên.",
        "vi_du": "Giảng viên chỉ có bằng cử nhân dạy bậc đại học — cơ sở giáo dục vi phạm điều kiện về tiêu chuẩn giảng viên.",
        "biet_them": "Giáo sư và Phó giáo sư là danh hiệu do Hội đồng Chức danh Giáo sư Nhà nước phong tặng, không bắt buộc để giảng dạy."
    },
    {
        "so_dieu": "Điều 74", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Học bổng và hỗ trợ tài chính cho người học",
        "noi_dung": "Nhà nước có chính sách học bổng, tín dụng sinh viên, miễn giảm học phí cho học sinh nghèo, dân tộc thiểu số, con liệt sĩ, thương binh. Cơ sở giáo dục ngoài công lập cũng phải dành tối thiểu 8% học phí thu được để cấp học bổng.",
        "vi_du": "Sinh viên hộ nghèo được vay vốn ngân hàng chính sách với lãi suất ưu đãi để đóng học phí, mức tối đa 4 triệu/tháng.",
        "biet_them": "Ngân hàng Chính sách Xã hội quản lý chương trình tín dụng sinh viên — lãi suất thấp, trả nợ sau khi ra trường 12 tháng."
    },
    {
        "so_dieu": "Điều 77", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Cha mẹ có quyền và nghĩa vụ trong giáo dục con",
        "noi_dung": "Cha mẹ có quyền lựa chọn trường, phương thức giáo dục phù hợp cho con. Có nghĩa vụ tạo điều kiện cho con học tập, phối hợp với nhà trường trong giáo dục con, không được ép buộc học sinh học thêm.",
        "vi_du": "Cha mẹ ép con học liên tục không cho nghỉ ngơi — vi phạm quyền được vui chơi, giải trí của trẻ em được bảo vệ bởi Luật Trẻ em.",
        "biet_them": "Cha mẹ có quyền giám sát chất lượng giáo dục của trường thông qua hội phụ huynh học sinh."
    },
    {
        "so_dieu": "Điều 42", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Cơ sở giáo dục tư thục được thành lập với điều kiện",
        "noi_dung": "Cơ sở giáo dục tư thục được thành lập khi có đủ: địa điểm, cơ sở vật chất, thiết bị dạy học; đội ngũ nhà giáo; chương trình giáo dục; nguồn vốn đủ để đảm bảo hoạt động. Phải được cơ quan có thẩm quyền cho phép.",
        "vi_du": "Mở trường mầm non tư thục cần xin phép Phòng GD&ĐT quận/huyện, phải đạt tiêu chuẩn về diện tích, số lượng giáo viên, an toàn thực phẩm.",
        "biet_them": "Trường tư thục hoạt động không vì lợi nhuận được ưu đãi thuế đất, thuế TNDN như các tổ chức giáo dục công lập."
    },
    {
        "so_dieu": "Điều 19", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Phát triển giáo dục vùng dân tộc thiểu số",
        "noi_dung": "Nhà nước ưu tiên phát triển giáo dục ở vùng dân tộc thiểu số, miền núi, vùng có điều kiện kinh tế đặc biệt khó khăn. Người dân tộc thiểu số có quyền dùng tiếng mẹ đẻ trong học tập ở cấp tiểu học.",
        "vi_du": "Học sinh người Tày ở Cao Bằng được học tiếng Tày song song tiếng Việt trong chương trình tiểu học.",
        "biet_them": "Nhà nước có chính sách cử tuyển, đào tạo theo địa chỉ ưu tiên cho học sinh dân tộc thiểu số vào đại học."
    },
    {
        "so_dieu": "Điều 50", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Tự chủ đại học — quyền và trách nhiệm",
        "noi_dung": "Cơ sở giáo dục đại học thực hiện quyền tự chủ trong tổ chức, nhân sự, tài chính, tài sản, hợp tác quốc tế, đảm bảo chất lượng. Tự chủ gắn liền với trách nhiệm giải trình với xã hội.",
        "vi_du": "Đại học Quốc gia Hà Nội được tự quyết định mức học phí, chương trình đào tạo mà không cần xin phép Bộ GD&ĐT — nhưng phải công khai để xã hội giám sát.",
        "biet_them": "Tự chủ đại học được mở rộng theo Nghị quyết 77/NQ-CP, nhiều trường đang trong lộ trình thực hiện."
    },
    {
        "so_dieu": "Điều 87", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Dạy thêm học thêm có điều kiện",
        "noi_dung": "Giáo viên được dạy thêm ngoài nhà trường nhưng không được dạy thêm học sinh chính khóa của mình. Tổ chức dạy thêm ngoài nhà trường phải được cấp phép. Nghiêm cấm ép buộc học sinh học thêm.",
        "vi_du": "Giáo viên A dạy lớp 10B, không được nhận học sinh lớp 10B vào lớp học thêm tư của mình — dù học sinh và phụ huynh tự nguyện.",
        "biet_them": "Vi phạm quy định dạy thêm, giáo viên có thể bị kỷ luật từ cảnh cáo đến buộc thôi việc tùy mức độ."
    },
    {
        "so_dieu": "Điều 93", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Văn bằng giáo dục được Nhà nước bảo hộ",
        "noi_dung": "Văn bằng, chứng chỉ giáo dục được cấp theo quy định có giá trị trong phạm vi cả nước. Nghiêm cấm làm giả, mua bán, sử dụng văn bằng chứng chỉ giả.",
        "vi_du": "Sử dụng bằng đại học giả để nộp hồ sơ xin việc — có thể bị truy cứu trách nhiệm hình sự về tội giả mạo trong công tác.",
        "biet_them": "Bộ GD&ĐT có hệ thống tra cứu văn bằng trực tuyến để xác minh tính hợp lệ của bằng cấp."
    },
    {
        "so_dieu": "Điều 15", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Trách nhiệm của nhà nước với giáo dục",
        "noi_dung": "Nhà nước giữ vai trò chủ đạo trong phát triển sự nghiệp giáo dục; thực hiện đa dạng hóa các loại hình trường và hình thức giáo dục. Đầu tư cho giáo dục là đầu tư phát triển.",
        "vi_du": "Ngân sách nhà nước chi tối thiểu 20% cho giáo dục — đây là cam kết pháp lý được ghi trong Luật Giáo dục.",
        "biet_them": "Nhà nước khuyến khích và tạo điều kiện cho tổ chức, cá nhân trong và ngoài nước đầu tư vào giáo dục."
    },
    {
        "so_dieu": "Điều 30", "ten_luat": "Luật Giáo dục 2019",
        "tieu_de": "Chương trình giáo dục phổ thông do Bộ GD&ĐT ban hành",
        "noi_dung": "Chương trình giáo dục phổ thông do Bộ trưởng Bộ GD&ĐT ban hành sau khi được Hội đồng quốc gia thẩm định. Sách giáo khoa do các tổ chức, cá nhân biên soạn và được Bộ GD&ĐT phê duyệt.",
        "vi_du": "Chương trình GDPT 2018 được triển khai từ lớp 1 (2020), lớp 6 (2021), lớp 10 (2022) — tất cả trường trong cả nước phải thực hiện.",
        "biet_them": "Từ 2018, nhiều bộ sách giáo khoa khác nhau được lưu hành, trường tự chọn bộ sách phù hợp."
    },
],

# ═══════════════════════════════════════════════════════════════
#  HÀNH CHÍNH
# ═══════════════════════════════════════════════════════════════
"hanh_chinh": [
    {
        "so_dieu": "Điều 14", "ten_luat": "Hiến pháp 2013",
        "tieu_de": "Quyền con người không thể bị xâm phạm tùy tiện",
        "noi_dung": "Ở nước CHXHCN Việt Nam, các quyền con người, quyền công dân chỉ có thể bị hạn chế theo quy định của luật trong trường hợp cần thiết vì lý do quốc phòng, an ninh quốc gia, trật tự công cộng, sức khỏe, đạo đức xã hội.",
        "vi_du": "Cơ quan nhà nước không thể tùy tiện hạn chế quyền tự do đi lại, biểu đạt của công dân mà không có căn cứ pháp luật cụ thể.",
        "biet_them": "Đây là nguyên tắc cơ bản nhất của nhà nước pháp quyền — mọi giới hạn quyền đều phải có luật."
    },
    {
        "so_dieu": "Điều 30", "ten_luat": "Luật Xử lý vi phạm hành chính 2012",
        "tieu_de": "Thời hiệu xử phạt vi phạm hành chính",
        "noi_dung": "Thời hiệu xử phạt VPHC là 1 năm (trừ vi phạm kế toán, thuế, phí, lệ phí: 2 năm). Quá thời hiệu, không được ra quyết định xử phạt — chỉ áp dụng biện pháp khắc phục hậu quả.",
        "vi_du": "Vi phạm về xây dựng không phép xảy ra tháng 1/2022. Đến tháng 2/2023 cơ quan chức năng mới phát hiện — hết thời hiệu phạt tiền.",
        "biet_them": "Nhưng vẫn có thể buộc tháo dỡ công trình vi phạm như biện pháp khắc phục hậu quả."
    },
    {
        "so_dieu": "Điều 5", "ten_luat": "Luật Tiếp cận thông tin 2016",
        "tieu_de": "Công dân có quyền yêu cầu cung cấp thông tin",
        "noi_dung": "Công dân có quyền yêu cầu cơ quan nhà nước cung cấp thông tin do cơ quan đó tạo ra hoặc nắm giữ. Cơ quan nhà nước phải trả lời trong vòng 15 ngày, trường hợp phức tạp không quá 25 ngày.",
        "vi_du": "Bạn muốn biết dự án quy hoạch đất gần nhà — có quyền yêu cầu UBND phường/xã cung cấp thông tin quy hoạch.",
        "biet_them": "Chỉ có 3 loại thông tin bị giới hạn: bí mật nhà nước, bí mật đời tư, thông tin chưa đủ điều kiện công bố."
    },
    {
        "so_dieu": "Điều 2", "ten_luat": "Hiến pháp 2013",
        "tieu_de": "Nhà nước của dân, do dân, vì dân",
        "noi_dung": "Nhà nước Cộng hòa xã hội chủ nghĩa Việt Nam là nhà nước pháp quyền xã hội chủ nghĩa của Nhân dân, do Nhân dân, vì Nhân dân. Quyền lực nhà nước thuộc về nhân dân.",
        "vi_du": "Mọi quyết định hành chính ảnh hưởng đến quyền lợi người dân phải có căn cứ pháp lý — không thể tùy tiện ban hành.",
        "biet_them": "Nhà nước pháp quyền đòi hỏi mọi hoạt động nhà nước đều phải tuân theo pháp luật, chịu sự giám sát của nhân dân."
    },
    {
        "so_dieu": "Điều 8", "ten_luat": "Luật Tố cáo 2018",
        "tieu_de": "Quyền tố cáo của công dân",
        "noi_dung": "Công dân có quyền tố cáo với cơ quan, tổ chức, cá nhân có thẩm quyền về hành vi vi phạm pháp luật của cán bộ, công chức, viên chức trong việc thực hiện nhiệm vụ, công vụ.",
        "vi_du": "Phát hiện cán bộ UBND nhận hối lộ khi làm sổ đỏ — có thể tố cáo đến thanh tra, công an hoặc cơ quan cấp trên.",
        "biet_them": "Người tố cáo được bảo vệ danh tính và được bảo vệ khỏi sự trả thù. Tố cáo sai sự thật có thể bị xử lý."
    },
    {
        "so_dieu": "Điều 7", "ten_luat": "Luật Khiếu nại 2011",
        "tieu_de": "Quyền khiếu nại quyết định hành chính",
        "noi_dung": "Công dân có quyền khiếu nại quyết định hành chính, hành vi hành chính của cơ quan nhà nước, cán bộ công chức khi cho rằng quyết định đó vi phạm pháp luật, xâm phạm quyền lợi của mình.",
        "vi_du": "Bị từ chối cấp giấy phép xây dựng không có lý do hợp lệ — có thể khiếu nại lên cơ quan cấp trên trong 90 ngày.",
        "biet_them": "Có 2 cấp khiếu nại: lần 1 tại cơ quan ra quyết định, lần 2 tại cơ quan cấp trên hoặc khởi kiện ra Tòa hành chính."
    },
    {
        "so_dieu": "Điều 3", "ten_luat": "Luật Cán bộ công chức 2008",
        "tieu_de": "Công chức phải phục vụ nhân dân",
        "noi_dung": "Cán bộ, công chức phải trung thành với Đảng, Nhà nước và nhân dân; bảo vệ danh dự Tổ quốc và lợi ích quốc gia; tôn trọng nhân dân, tận tụy phục vụ nhân dân.",
        "vi_du": "Cán bộ gây khó dễ, hách dịch khi người dân đến làm thủ tục hành chính — vi phạm đạo đức công vụ, có thể bị kỷ luật.",
        "biet_them": "Người dân có quyền đánh giá sự hài lòng với dịch vụ hành chính công — đây là căn cứ xếp loại thi đua của cơ quan nhà nước."
    },
    {
        "so_dieu": "Điều 22", "ten_luat": "Luật Xử lý vi phạm hành chính 2012",
        "tieu_de": "Các hình thức xử phạt hành chính",
        "noi_dung": "Hình thức xử phạt chính: cảnh cáo hoặc phạt tiền. Hình thức bổ sung: tước giấy phép, tịch thu tang vật, trục xuất. Biện pháp khắc phục hậu quả: buộc khôi phục tình trạng ban đầu, buộc bồi thường...",
        "vi_du": "Vi phạm giao thông nhẹ: cảnh cáo hoặc phạt tiền. Tái phạm nhiều lần: tước bằng lái xe (hình thức bổ sung).",
        "biet_them": "Một vi phạm chỉ bị xử phạt một lần. Không được xử phạt hai lần về cùng một hành vi vi phạm hành chính."
    },
    {
        "so_dieu": "Điều 55", "ten_luat": "Luật Xử lý vi phạm hành chính 2012",
        "tieu_de": "Không xử phạt trường hợp phòng vệ chính đáng",
        "noi_dung": "Không xử phạt hành chính đối với hành vi vi phạm trong tình thế cấp thiết, phòng vệ chính đáng, sự kiện bất ngờ, người vi phạm chưa đủ tuổi, người mắc bệnh tâm thần.",
        "vi_du": "Đập vỡ cửa nhà hàng xóm để cứu người đang bị hỏa hoạn — không bị xử phạt vì tình thế cấp thiết.",
        "biet_them": "Người chưa đủ 14 tuổi không bị xử phạt hành chính. Từ 14-16 tuổi chỉ bị phạt cảnh cáo về một số vi phạm nhất định."
    },
    {
        "so_dieu": "Điều 18", "ten_luat": "Hiến pháp 2013",
        "tieu_de": "Người Việt Nam định cư ở nước ngoài là bộ phận của dân tộc",
        "noi_dung": "Người Việt Nam định cư ở nước ngoài là bộ phận không tách rời của cộng đồng dân tộc Việt Nam. Nhà nước bảo hộ quyền và lợi ích hợp pháp của người Việt Nam ở nước ngoài.",
        "vi_du": "Người Việt kiều bị gặp khó khăn ở nước ngoài có thể liên hệ Đại sứ quán Việt Nam để được hỗ trợ lãnh sự.",
        "biet_them": "Người Việt Nam định cư ở nước ngoài giữ quốc tịch Việt Nam (trừ khi từ bỏ) và được mua nhà ở tại Việt Nam."
    },
    {
        "so_dieu": "Điều 25", "ten_luat": "Hiến pháp 2013",
        "tieu_de": "Quyền tự do ngôn luận, báo chí, hội họp",
        "noi_dung": "Công dân có quyền tự do ngôn luận, tự do báo chí, tiếp cận thông tin, hội họp, lập hội, biểu tình. Việc thực hiện các quyền này do pháp luật quy định.",
        "vi_du": "Công dân có quyền phản ánh ý kiến về chính sách trên báo chí, mạng xã hội trong khuôn khổ pháp luật mà không bị ngăn cản.",
        "biet_them": "Quyền này bị giới hạn khi ảnh hưởng đến an ninh quốc gia, trật tự công cộng — giới hạn phải được quy định bằng luật."
    },
    {
        "so_dieu": "Điều 32", "ten_luat": "Hiến pháp 2013",
        "tieu_de": "Quyền sở hữu tài sản được Nhà nước bảo hộ",
        "noi_dung": "Mọi người có quyền sở hữu về thu nhập hợp pháp, của cải để dành, nhà ở, tư liệu sinh hoạt, tư liệu sản xuất và vốn góp trong doanh nghiệp. Tài sản hợp pháp của mọi người không bị quốc hữu hóa.",
        "vi_du": "Nhà nước không thể tịch thu căn nhà của bạn vì lý do tùy tiện — phải có quyết định hợp pháp với bồi thường thỏa đáng.",
        "biet_them": "Thu hồi đất phục vụ quốc phòng, an ninh, phát triển KT-XH là hợp pháp nhưng phải bồi thường theo giá thị trường."
    },
    {
        "so_dieu": "Điều 4", "ten_luat": "Luật Phòng chống tham nhũng 2018",
        "tieu_de": "Các hành vi tham nhũng bị nghiêm cấm",
        "noi_dung": "Hành vi tham nhũng gồm: tham ô tài sản; nhận hối lộ; lạm dụng chức vụ; lợi dụng ảnh hưởng đối với người có chức vụ để trục lợi; giả mạo trong công tác; đưa hối lộ, môi giới hối lộ để giải quyết công việc.",
        "vi_du": "Đưa tiền 'bồi dưỡng' cho thanh tra để không bị xử phạt — cả người đưa và người nhận đều vi phạm luật phòng chống tham nhũng.",
        "biet_them": "Người tự giác khai báo hành vi tham nhũng trước khi bị phát giác được xem xét giảm nhẹ trách nhiệm."
    },
    {
        "so_dieu": "Điều 45", "ten_luat": "Luật Phòng chống tham nhũng 2018",
        "tieu_de": "Kê khai tài sản thu nhập bắt buộc với cán bộ",
        "noi_dung": "Người có nghĩa vụ kê khai (cán bộ từ phó phòng trở lên) phải kê khai trung thực tài sản, thu nhập hàng năm. Kê khai không trung thực bị xử lý kỷ luật hoặc truy cứu trách nhiệm hình sự.",
        "vi_du": "Cán bộ không kê khai căn nhà mới mua hoặc khai thấp hơn thực tế — vi phạm nghĩa vụ kê khai, bị xử lý kỷ luật.",
        "biet_them": "Bản kê khai tài sản được lưu giữ và kiểm tra định kỳ, không công khai trừ trường hợp có điều tra."
    },
    {
        "so_dieu": "Điều 9", "ten_luat": "Luật Hộ tịch 2014",
        "tieu_de": "Đăng ký khai sinh cho trẻ trong 60 ngày",
        "noi_dung": "Cha, mẹ có trách nhiệm đăng ký khai sinh cho con trong thời hạn 60 ngày kể từ ngày sinh. Trường hợp quá hạn vẫn được đăng ký nhưng phải nộp phạt vi phạm hành chính.",
        "vi_du": "Bé sinh ngày 1/1 — phải đăng ký khai sinh trước ngày 1/3. Nếu đăng ký muộn bị phạt từ 100.000 đến 300.000đ.",
        "biet_them": "Khai sinh là giấy tờ gốc, là cơ sở cho tất cả giấy tờ tùy thân khác. Khai sinh trực tuyến đã được triển khai tại nhiều tỉnh."
    },
    {
        "so_dieu": "Điều 3", "ten_luat": "Luật Căn cước 2023",
        "tieu_de": "Căn cước điện tử có giá trị như thẻ căn cước vật lý",
        "noi_dung": "Căn cước điện tử trên ứng dụng VNeID có giá trị sử dụng tương đương thẻ Căn cước trong các giao dịch, thủ tục hành chính. Công dân có thể dùng căn cước điện tử thay thẻ vật lý.",
        "vi_du": "Đi máy bay, làm thủ tục hành chính, mở tài khoản ngân hàng — có thể dùng app VNeID thay thẻ căn cước vật lý.",
        "biet_them": "Luật Căn cước 2023 thay thế Luật CMND và Luật CCCD trước đây. Tên gọi thay đổi từ 'Căn cước công dân' thành 'Căn cước'."
    },
    {
        "so_dieu": "Điều 12", "ten_luat": "Luật Cư trú 2020",
        "tieu_de": "Xóa bỏ sổ hộ khẩu từ 01/01/2023",
        "noi_dung": "Từ 01/01/2023, sổ hộ khẩu, sổ tạm trú giấy không còn giá trị sử dụng. Thông tin cư trú được quản lý trên Cơ sở dữ liệu quốc gia về dân cư. Người dân không cần mang sổ hộ khẩu khi làm thủ tục.",
        "vi_du": "Đăng ký nhập học cho con, mua xe, làm thủ tục hành chính — không cần nộp sổ hộ khẩu, cơ quan tự tra cứu hệ thống.",
        "biet_them": "Quyền lợi trước đây gắn với hộ khẩu (trường học, bệnh viện...) không thể bị từ chối vì lý do thường trú."
    },
    {
        "so_dieu": "Điều 47", "ten_luat": "Luật Xử lý vi phạm hành chính 2012",
        "tieu_de": "Nguyên tắc xử phạt — công bằng, tương xứng",
        "noi_dung": "Mọi vi phạm phải được phát hiện, ngăn chặn và xử lý kịp thời. Việc xử lý phải công minh, triệt để. Hậu quả do vi phạm hành chính gây ra phải được khắc phục theo quy định của pháp luật.",
        "vi_du": "Cùng vi phạm như nhau nhưng một người bị phạt nặng hơn vì có quan hệ thù địch với cán bộ — vi phạm nguyên tắc công bằng trong xử phạt.",
        "biet_them": "Người bị xử phạt có quyền khiếu nại, tố cáo nếu thấy quyết định xử phạt không đúng pháp luật."
    },
    {
        "so_dieu": "Điều 40", "ten_luat": "Luật Phòng chống tham nhũng 2018",
        "tieu_de": "Cơ quan nhà nước phải công khai thông tin",
        "noi_dung": "Cơ quan nhà nước phải công khai trên trang thông tin điện tử: chức năng nhiệm vụ, thủ tục hành chính, quy hoạch kế hoạch phát triển, tình hình thu chi ngân sách, kết quả thanh kiểm tra.",
        "vi_du": "UBND tỉnh phải đăng công khai dự toán và quyết toán ngân sách hàng năm — người dân có quyền xem và giám sát.",
        "biet_them": "Minh bạch thông tin là biện pháp quan trọng nhất để phòng ngừa tham nhũng — ánh sáng công khai là thuốc diệt tham nhũng tốt nhất."
    },
    {
        "so_dieu": "Điều 5", "ten_luat": "Luật Thanh tra 2022",
        "tieu_de": "Nguyên tắc hoạt động thanh tra",
        "noi_dung": "Hoạt động thanh tra phải tuân theo pháp luật; bảo đảm chính xác, khách quan, trung thực, công khai, dân chủ, kịp thời; không làm cản trở hoạt động bình thường của đối tượng thanh tra.",
        "vi_du": "Đoàn thanh tra kéo dài thời gian thanh tra, gây ảnh hưởng nghiêm trọng đến hoạt động doanh nghiệp mà không có lý do — vi phạm nguyên tắc thanh tra.",
        "biet_them": "Thời hạn thanh tra thông thường không quá 30 ngày, trường hợp phức tạp không quá 60 ngày. Có thể gia hạn 1 lần."
    },
],
}
