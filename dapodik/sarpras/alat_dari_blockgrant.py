from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject


@dataclass(eq=False)
class AlatDariBlockgrant(DapodikObject):
    blockgrant_id: str
    id_alat: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    blockgrant_id_str: str
    id_alat_str: str = ''
    alat_dari_blockgrant_id: Optional[str] = 'Admin.model.AlatDariBlockgrant-1'
    _id: str = 'alat_dari_blockgrant_id'
