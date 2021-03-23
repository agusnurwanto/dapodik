from requests import Session

from dapodik import __semester__

from . import BaseAuth
from . import BaseRest
from . import BaseValidasi
from . import BasePesertaDidik
from . import BaseRombonganBelajar
from . import BaseSekolah
from .constants import HEADERS


class Dapodik(
    BaseAuth,
    BaseRest,
    BaseValidasi,
    BasePesertaDidik,
    BaseRombonganBelajar,
    BaseSekolah,
):
    def __init__(
        self,
        username: str,
        password: str,
        semester_id: str = __semester__,
        server: str = "http://localhost:5774/",
        session: Session = Session(),
        pengguna: int = 0,
        rememberme: bool = True,
    ):
        super(Dapodik, self).__init__(server)
        self.session.headers.update(HEADERS)
        self.daftar_pengguna = self.login(
            username, password, rememberme, semester_id, pengguna
        )
        if self.daftar_pengguna:
            self.logger.info(f"Berhasil login {username}")

    def __del__(self):
        self.logout()
