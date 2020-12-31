import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("id_gmd")
@attr.dataclass(frozen=True)
class Gmd(DapodikObject):
    id_gmd: str
    nm_gmd: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
