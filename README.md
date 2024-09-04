# Excel, Ods na PDF

Tento nástroj ponúka výber stĺpcov pre vychovávateľov, čo im umožňuje jednoduchšie vytváranie rôznych tabuliek v PDF formáte.

## Stiahnutie projektu

1. **Okopírovanie Makefile:**
   - Stiahnite si súbor `Makefile` a umiestnite ho do priečinka, kde chcete mať program. Pre Windows si vyberte Makefile.win a potom mu odstráňte win koncovku.

2. **Nutné požiadavky:**
   - Uistite sa, že máte nainštalovaný `git`. Pre Windows si ho môžete stiahnuť [z tohto odkazu](https://git-scm.com/download/win).
   - Pre windows:
        - python3 (potrebné pridať do environmentálnych premenných),
        - pip (do cmd `python -m ensurepip --upgrade`),
        - make command (minGW [z tohto odkazu](https://sourceforge.net/projects/mingw/) a potom postupujte podľa [tohto návodu](https://medium.com/@samsorrahman/how-to-run-a-makefile-in-windows-b4d115d7c516))

3. **Vytvorenie projektu:**
   - Otvorte terminál a zadajte príkaz `make`.
   - Tento príkaz vytvorí priečinok s názvom `excel_to_pdf_project`.

4. **Nastavenie projektu:**
   - Otvorte súbor `init.py`, ktorý sa nachádza v priečinku `excel_to_pdf_project`, a nastavte všetky štyri premenné:
     - **Názov tabuľkového súboru**
     - **Názvy, ktoré budú generované nad tabuľkou vo výslednom dokumente**

5. **Presunutie tabuľkového súboru a init.py:**
   - Váš tabuľkový súbor presuňte do priečinka, kde sa nachádza aj priečinok `excel_to_pdf_project`.
   - init.py presuňte tiež tam, kde ste presunuli tabuľkový súbor (z pôvodného miesta ho zmažte)

6. **Spustenie programu:**
   - Vráťte sa do terminálu, cez ktorý ste spustili príkaz `make`, a zadajte príkaz `make run`.
   - Následne sa riaďte pokynmi, ktoré sa zobrazia na obrazovke.
