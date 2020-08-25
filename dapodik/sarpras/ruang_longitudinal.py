from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, Semester, Ruang
from dapodik.utils.decorator import set_meta


@set_meta('ruang_longitudinal_id')
@dataclass(eq=False)
class RuangLongitudinal(DapodikObject):
    id_ruang: str
    semester_id: str
    blob_id: Optional[str]
    rusak_lisplang_talang: str
    ket_lisplang_talang: str
    rusak_rangka_plafon: str
    ket_rangka_plafon: str
    rusak_tutup_plafon: str
    ket_tutup_plafon: str
    rusak_bata_dinding: str
    ket_bata_dinding: str
    rusak_plester_dinding: str
    ket_plester_dinding: str
    rusak_daun_jendela: str
    ket_daun_jendela: str
    rusak_daun_pintu: str
    ket_daun_pintu: str
    rusak_kusen: str
    ket_kusen: str
    rusak_tutup_lantai: str
    ket_penutup_lantai: str
    rusak_inst_listrik: str
    ket_inst_listrik: str
    rusak_inst_air: str
    ket_inst_air: str
    rusak_drainase: str
    ket_drainase: str
    rusak_finish_struktur: str
    ket_finish_struktur: str
    rusak_finish_plafon: str
    ket_finish_plafon: str
    rusak_finish_dinding: str
    ket_finish_dinding: str
    rusak_finish_kpj: str
    ket_finish_kpj: str
    berfungsi: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    id_ruang_str: str
    semester_id_str: str
    ruang_longitudinal_id: str

    @Semester.prop
    def semester(self) -> Semester:
        return self.semester_id  # type: ignore

    @property
    def blob(self):
        return self.blob_id

    @property
    def updater(self):
        return self.updater_id

    @property
    def ruang_longitudinal(self):
        return self

    @Ruang.prop
    def ruang(self) -> Ruang:
        return self.id_ruang  # type: ignore
