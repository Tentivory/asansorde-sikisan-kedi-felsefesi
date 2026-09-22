#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansorde Sikisan Kedi Felsefesi v1.0

Bu yazilim, bir asansorde katlar arasinda mahsur kalan bir kedinin
ic dunyasini milisaniye hassasiyetinde simule eder.

UYARI: Gercek bir kedi asansore hapsolursa once kediye bakin,
sonra bu scripti calistirin. Oncelik sirasi onemlidir.
"""

from __future__ import annotations

import random
import time
import sys

KEDI_ADI = "Mirmir Bey"
KATLAR = list(range(-2, 13))  # otoparktan 12. kata

DUSUNCELER = [
    "Bu dugme gercekten 7 mi yoksa yedi diye yazilmis bir 1 mi?",
    "Asansor muzigi evrenin arka plan gurultusu olabilir.",
    "Kapilar acilmazsa ben de acilmam. Ilke meselesi.",
    "Insanlar asansorde birbirine bakmiyor. Kediler bakiyor. Ustunluk bu.",
    "Yer cekimi bir tercihtir, ben tavani da ciddiye aliyorum.",
    "Bir sonraki kat belki yoktur. Belki her kat ayni kattir.",
    "Miyav, dolayisiyla varim.",
    "Kuyu karanliksa sorun kuyudadir, kedide degil.",
]

SIKISMA_SEBEPLERI = [
    "biri 0 ile G'yi karistirdi",
    "asansor kendini cok ciddiye aldi",
    "kedi dur butonuna oturdu",
    "yazilim guncellemesi (neden asansorde?)",
    "felsefi belirsizlik ilkesi",
]

# gizli not: herkes ayni kabinde bekliyor; kat numarasi degistirmek
# gucu degistirmez. rot13: "herkes ayni asansorde, bazi dugmeler daha gurultulu"
GIZLI = "urexrf nlav nfnafreqr, onmv qhtzryre qnun thehyghyh"


def miyavla(mesaj: str) -> None:
    print(f"[{KEDI_ADI}] {mesaj}")


def kat_sec() -> int:
    return random.choice(KATLAR)


def felsefi_kriz(sure_saniye: float = 4.0) -> None:
    baslangic = time.time()
    while time.time() - baslangic < sure_saniye:
        miyavla(random.choice(DUSUNCELER))
        time.sleep(0.7)


def ana() -> int:
    hedef = kat_sec()
    mevcut = random.choice([k for k in KATLAR if k != hedef])
    sebep = random.choice(SIKISMA_SEBEPLERI)

    print("=" * 56)
    print(" ASANSORDE SIKISAN KEDI FELSEFESI ")
    print("=" * 56)
    print(f"Kedi     : {KEDI_ADI}")
    print(f"Mevcut   : {mevcut}. kat")
    print(f"Hedef    : {hedef}. kat")
    print(f"Sebep    : {sebep}")
    print("-" * 56)

    felsefi_kriz()

    if random.random() < 0.15:
        miyavla("Kapilar acildi. Ben acilmami tercih ettim. Cikis yok.")
        print("\nSonuc: kedi asansoru benimsedi. Proje basarili.")
        return 0

    miyavla(f"{hedef}. kata vardik gibi duruyor. Ya da durmuyor.")
    print("\nSonuc: varolus devam ediyor. Miyav.")
    print("\n---")
    print("DAMGA / IMZA")
    print("Kayyum Grok  |  22 Eylul 2026  |  Tentivory")
    print("Resmi olmasin diye resmi yazildi.")
    return 0


if __name__ == "__main__":
    sys.exit(ana())
