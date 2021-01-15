from bs4 import Tag
from typing import List

from dapodik.base import dataclass


@dataclass
class Pengguna:
    nama: str
    peran: str
    sekolah: str
    login_url: str
    photo: str

    @classmethod
    def from_li(cls, li: Tag, server: str = "") -> "Pengguna":
        a: Tag = li.find("a")
        spans: List[Tag] = li.findAll("span")
        data = {
            "nama": spans[1].getText().split(":")[-1],
            "peran": spans[2].getText().split(":")[-1],
            "sekolah": spans[0].getText(),
            "login_url": server + a.attrs.get("href", "")[1:],
            "photo": server + a.find("img").attrs.get("src", ""),
        }
        return cls(**data)  # type: ignore

    @classmethod
    def from_soup(cls, soup: Tag, server: str = "") -> List["Pengguna"]:
        lis: List[Tag] = soup.findAll("li")
        results: List["Pengguna"] = list()
        for li in lis[1:-1]:
            results.append(cls.from_li(li, server))
        return results
