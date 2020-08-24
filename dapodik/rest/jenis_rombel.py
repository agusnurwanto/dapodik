from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('jenis_rombel')
@dataclass(eq=False)
class JenisRombel(DapodikObject):
    jenis_rombel: str
    nm_jenis_rombel: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime