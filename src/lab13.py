"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về chi phí token, tool, chay_lai, xem_lai, lam_lai, tong,
    thanh_cong, cps và hoa_don_moi_yc ((token + tool) / số yêu cầu).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=tien_token.sum(), tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai, lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else math.inf,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs) if len(reqs) else math.inf,
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Chi phí từ trace (đồng)')
    nhan = {
        'xem_lai': 'xem_lai [simulated]',
        'lam_lai': 'lam_lai [simulated]',
        'tong': 'tong [có phần simulated]',
        'cps': 'cps [simulated]',
    }
    for ten, gia_tri in ket_qua.items():
        print(f'{nhan.get(ten, ten):30s} {gia_tri:>14,.1f}')
    print(f"CPS / hoá đơn mỗi yêu cầu [simulated]: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")

    print('\nA3 · Chi phí theo loại yêu cầu')
    bang_loai = []
    for loai, nhom in reqs.groupby('loai', sort=False):
        chi_phi = mo_hinh(runs, nhom)
        bang_loai.append({
            'loai': loai,
            'so_yeu_cau': len(nhom),
            'thanh_cong': f"{chi_phi['thanh_cong'] / len(nhom):.1%}",
            'lan_chay/yc': f"{nhom['so_lan_chay'].mean():.2f}",
            'cps [simulated]': f"{chi_phi['cps']:,.0f}",
            'cps/12000 [simulated]': f"{chi_phi['cps'] / BASELINE:.2f}",
        })
    print(pd.DataFrame(bang_loai).to_string(index=False))

    print('\nA4 · Phạm vi noi_dia + hang_nang [simulated]')
    trong_pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    chi_phi_pham_vi = mo_hinh(runs, trong_pham_vi)
    bang_co_dinh = []
    for khoi_luong_thang in (45000, 22500):
        # Mẫu gồm mọi loại; chỉ việc thành công trong phạm vi phân bổ chi phí cố định.
        thanh_cong_thang = khoi_luong_thang * chi_phi_pham_vi['thanh_cong'] / len(reqs)
        co_dinh_moi_viec = 40000000 / thanh_cong_thang
        cps_co_dinh = chi_phi_pham_vi['cps'] + co_dinh_moi_viec
        bang_co_dinh.append({
            'yeu_cau/thang': khoi_luong_thang,
            'thanh_cong/thang': f'{thanh_cong_thang:,.0f}',
            'co_dinh/viec': f'{co_dinh_moi_viec:,.0f}',
            'cps_bien_doi': f"{chi_phi_pham_vi['cps']:,.0f}",
            'cps_co_co_dinh': f'{cps_co_dinh:,.0f}',
            'cps/12000': f'{cps_co_dinh / BASELINE:.2f}',
        })
    print(pd.DataFrame(bang_co_dinh).to_string(index=False))

    # CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    print('\nB1 · Độ nhạy [simulated]')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2),
        'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=LUONG_PHUT * 1.25),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    cps_kich_ban = {ten: mo_hinh(runs, reqs, **kw)['cps'] for ten, kw in kich_ban.items()}
    print(f'{"Kịch bản":25s} {"CPS (đ)":>8s} {"Thay đổi":>8s}')
    print(f'{"Gốc (A2)":25s} {goc:8,.0f} {0:+7.1f}%')
    for ten, cps in cps_kich_ban.items():
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+7.1f}%')
    for yeu_to in ('Giá token', 'Xem lại', 'Làm lại'):
        assert math.isclose(cps_kich_ban[f'{yeu_to} gấp đôi'] - goc,
                            2 * (goc - cps_kich_ban[f'{yeu_to} giảm một nửa']))

    print('\nB2 · Đổi một cặp và xếp hạng [simulated]')
    cps_cap = mo_hinh(runs, reqs, gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2,
                      he_so_xem_lai=2)['cps']
    assert math.isclose(cps_cap - goc,
                        cps_kich_ban['Giá token gấp đôi'] + cps_kich_ban['Xem lại gấp đôi'] - 2 * goc)
    print(f'Token và xem lại gấp đôi: {cps_cap:,.0f} đ ({(cps_cap / goc - 1) * 100:+.1f}%)')
    xep_hang = sorted((ten for ten, cps in cps_kich_ban.items() if cps > goc),
                      key=lambda ten: cps_kich_ban[ten] - goc, reverse=True)
    for hang, ten in enumerate(xep_hang[:3], 1):
        print(f'{hang}. {ten}: {(cps_kich_ban[ten] / goc - 1) * 100:+.1f}%')

    print('\nB3 · Giới hạn chạy lại [simulated, đồng]')
    bang_gioi_han = []
    for gioi_han in (1, 2, 3):
        chi_phi = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - chi_phi['thanh_cong']
        bang_gioi_han.append({
            'gioi_han': gioi_han,
            'tong_tro_ly': chi_phi['tong'],
            'khong_thanh_cong': khong_thanh_cong,
            'ca_he_thong': chi_phi['tong'] + BASELINE * khong_thanh_cong,
            'cps': chi_phi['cps'],
        })
    print(pd.DataFrame(bang_gioi_han).to_string(index=False, float_format=lambda x: f'{x:,.0f}'))
    re_nhat_he_thong = min(bang_gioi_han, key=lambda dong: dong['ca_he_thong'])
    re_nhat_cps = min(bang_gioi_han, key=lambda dong: dong['cps'])
    print(f"Rẻ nhất cả hệ thống: {re_nhat_he_thong['gioi_han']} lần; CPS thấp nhất: {re_nhat_cps['gioi_han']} lần.")

    print('\nB4 · Xem lại 100% noi_dia + hang_nang [simulated]')
    yc_co_run_ok = runs.loc[runs['status'] == 'ok', 'request_id']
    reqs_xem_lai = trong_pham_vi.copy()
    reqs_xem_lai['phut_xem_lai_simulated'] = reqs_xem_lai['request_id'].isin(yc_co_run_ok) * 5
    so_yc_xem_lai = reqs_xem_lai['request_id'].isin(yc_co_run_ok).sum()
    phut_lam_lai_tb = round(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean(), 1)
    print(f'{so_yc_xem_lai} yêu cầu được xem lại, 5 phút/yêu cầu; {chi_phi_pham_vi["thanh_cong"]} việc thành công.')
    bang_xem_lai = []
    for phut_lam_lai in (9, phut_lam_lai_tb):
        reqs_xem_lai['phut_lam_lai_simulated'] = (reqs_xem_lai['ket_qua'] == 'lam_lai') * phut_lam_lai
        chi_phi = mo_hinh(runs, reqs_xem_lai)
        phut_hoa_von = (BASELINE * chi_phi['thanh_cong'] - chi_phi['token']
                        - chi_phi['tool'] - chi_phi['lam_lai']) / (so_yc_xem_lai * LUONG_PHUT)
        bang_xem_lai.append({
            'phut_lam_lai/ca': phut_lam_lai,
            'xem_lai': chi_phi['xem_lai'],
            'lam_lai': chi_phi['lam_lai'],
            'tong': chi_phi['tong'],
            'cps': chi_phi['cps'],
            'cps/12000': chi_phi['cps'] / BASELINE,
            'phut_xem_lai_hoa_von': phut_hoa_von,
        })
    print(pd.DataFrame(bang_xem_lai).to_string(index=False, formatters={
        'phut_lam_lai/ca': '{:.1f}'.format,
        'xem_lai': '{:,.0f}'.format, 'lam_lai': '{:,.0f}'.format,
        'tong': '{:,.0f}'.format, 'cps': '{:,.0f}'.format,
        'cps/12000': '{:.2f}'.format, 'phut_xem_lai_hoa_von': '{:.1f}'.format,
    }))

    # CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
    from statistics import NormalDist
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    def co_mau(p1, p2, alpha=0.05, power=0.8):
        za = NormalDist().inv_cdf(1 - alpha / 2)
        zb = NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    print('\nD1 · Cỡ mẫu mỗi nhóm (baseline 0,70; alpha 0,05; power 0,80; ICC 0,02)')
    icc = 0.02
    n_5_diem = co_mau(0.70, 0.75)
    print(f'a. Chia theo yêu cầu, chênh 5 điểm: {n_5_diem:,} yêu cầu/nhóm.')

    de_75 = 1 + (75 - 1) * icc
    n_theo_nhan_vien = math.ceil(n_5_diem * de_75)
    nhan_vien_moi_nhom = math.ceil(n_theo_nhan_vien / 75)
    print(f'b. 75 yêu cầu/người: DE = {de_75:.2f}; {n_theo_nhan_vien:,} yêu cầu/nhóm; '
          f'{nhan_vien_moi_nhom} người/nhóm, tổng {2 * nhan_vien_moi_nhom} > 40 người hiện có.')

    gioi_han_nhan_vien = 20 / icc
    gioi_han_depot = 6 / icc
    print(f'c. 20 nhân viên/nhóm: cỡ mẫu hiệu dụng luôn < {gioi_han_nhan_vien:,.0f} '
          f'< {n_5_diem:,}; không đủ cho chênh 5 điểm dù tăng yêu cầu/người.')
    print(f'd. 6 depot/nhóm: cỡ mẫu hiệu dụng luôn < {gioi_han_depot:,.0f}; '
          'chỉ 6 cụm/nhóm, dưới 20 cụm.')

    n_6_diem = co_mau(0.70, 0.76)
    m_can = math.ceil(n_6_diem * (1 - icc) / (20 - n_6_diem * icc))
    de_6_diem = 1 + (m_can - 1) * icc
    n_hieu_dung_6 = 20 * m_can / de_6_diem
    assert n_hieu_dung_6 >= n_6_diem
    assert 20 * (m_can - 1) / (1 + (m_can - 2) * icc) < n_6_diem
    print(f'e. Chênh 6 điểm: {n_6_diem:,} yêu cầu độc lập/nhóm; với 20 người/nhóm cần '
          f'ít nhất {m_can} yêu cầu/người; DE = {de_6_diem:.2f}; n hiệu dụng = {n_hieu_dung_6:.2f}.')

    power_5_diem = NormalIndPower().power(
        effect_size=abs(proportion_effectsize(0.70, 0.75)),
        nobs1=n_hieu_dung_6, alpha=0.05, ratio=1, alternative='two-sided',
    )
    print(f'Đánh đổi: thiết kế cho chênh 6 điểm có power {power_5_diem:.2f} nếu tác động thật chỉ là 5 điểm.')

    print('\nD3 · Tỉ lệ mở lại trong 7 ngày hiện tại')
    so_mo_lai = reqs['mo_lai_trong_7_ngay'].sum()
    ti_le_mo_lai = reqs['mo_lai_trong_7_ngay'].mean()
    so_mo_lai_pham_vi = trong_pham_vi['mo_lai_trong_7_ngay'].sum()
    ti_le_mo_lai_pham_vi = trong_pham_vi['mo_lai_trong_7_ngay'].mean()
    print(f'Toàn mẫu: {so_mo_lai}/{len(reqs)} = {ti_le_mo_lai:.2%}.')
    print(f'noi_dia + hang_nang: {so_mo_lai_pham_vi}/{len(trong_pham_vi)} = {ti_le_mo_lai_pham_vi:.2%}.')
