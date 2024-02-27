from pathlib import Path
import pytest
from uppgift2 import palindromish

# Ska fixa denna


def test_palindromish_radar_2():
    assert (
        palindromish("radar", 2) == True
    ), "Testfall 1 misslyckades: 'radar' med grad 2 bör vara True"


def test_palindromish_list_3_true():
    assert (
        palindromish([1, 2, 3, 50, 60, 3, 2, 1], 3) == True
    ), "Testfall 2 misslyckades: Listan med grad 3 bör vara True"


def test_palindromish_list_4_false():
    assert (
        palindromish([1, 2, 3, 50, 60, 3, 2, 1], 4) == False
    ), "Testfall 3 misslyckades: Listan med grad 4 bör vara False"


def test_palindromish_example_3():
    assert (
        palindromish("example", 3) == False
    ), "Testfall 4 misslyckades: 'example' med grad 3 bör vara False"


def test_palindromish_naturrutan():
    # Antag att funktionen automatiskt hanterar halva längden av sekvensen om inget gradvärde anges
    assert (
        palindromish("Naturrutan") == True
    ), "Testfall 5 misslyckades: 'Naturrutan' bör vara True som ett fullständigt palindrom"


def test_palindromish_empty_string():
    assert (
        palindromish("") == True
    ), "Testfall 6 misslyckades: En tom sträng bör anses vara ett palindrom"
