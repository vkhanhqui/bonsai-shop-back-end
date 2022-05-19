from app.db.database import SessionLocal
from app.models.schemas.dong_vat import DongVatUpdate
from app.db.tables import DongVat


db = SessionLocal()


def update_dong_vat(_in: DongVatUpdate):
    try:
        db.query(DongVat).\
        filter(DongVat.id_dong_vat == _in.id_dong_vat).\
        update({
            DongVat.id_user: _in.id_user,
            DongVat.id_gioi: _in.id_gioi,
            DongVat.id_nganh: _in.id_nganh,
            DongVat.id_lop: _in.id_lop,
            DongVat.id_bo: _in.id_bo,
            DongVat.id_ho: _in.id_ho,
            DongVat.id_gia_tri: _in.id_gia_tri,
            DongVat.id_tinh_trang_bao_ton: _in.id_tinh_trang_bao_ton,
            DongVat.id_tinh_trang_mau_vat: _in.id_tinh_trang_mau_vat,
            DongVat.id_phan_bo: _in.id_phan_bo,
            DongVat.id_sinh_canh: _in.id_sinh_canh,
            DongVat.dia_diem: _in.dia_diem,
            DongVat.ngay_thu_mau: _in.ngay_thu_mau,
            DongVat.hinh_thai: _in.hinh_thai,
            DongVat.sinh_thai: _in.sinh_thai,
            DongVat.ten_dia_phuong: _in.ten_dia_phuong,
            DongVat.ten_khoa_hoc: _in.ten_khoa_hoc,
            DongVat.ten_tieng_viet: _in.ten_tieng_viet,
            DongVat.nguoi_thu_mau: _in.nguoi_thu_mau,
        })
        db.commit()
        return _in
    except:
        return None