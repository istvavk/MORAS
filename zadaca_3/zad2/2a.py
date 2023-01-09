class Parser:

    def parseFile(self, filename):
        # Otvaramo datoteku s ekstenzijom ".vm".
        try:
            self._file = open(filename + ".vm", "r")
        except:
            Parser._error("File", -1, "Cannot open source file.")
            return

        self._name = filename # Ime datoteke.
        self._lines = [] # Linije koda.
        self._flag = True # Je li parsiranje uspjesno?
        self._lab = 0

        # Citamo linije koda iz VM datoteke.
        try:
            self._readFile()
        except:
            Parser._error("File", -1, "Cannot read source file.")
            return

        # Parsiramo VM kod liniju po liniju.
        if not self._parseLines():
            return

        # Zapisujemo asemblerski kod.
        try:
            self._file = open(filename + ".asm", "w")
        except:
            Parser._error("File", -1, "Cannot open destination file.")
            return

        try:
            self._writeFile()
        except:
            Parser._error("File", -1, "Cannot write to destination file.")
            return


    # U metodi _parseLines dodan je uvjet za prepoznavanje makro naredbe $MV 
    # Taj uvjet treba provjeravati nalazi li se u prvoj riječi linije "$MV"
    # Kod za parsiranje makro naredbe $MV treba pročitati 
    # dva argumenta iz linije s makro naredbom i pohraniti ih u odgovarajuće 
    # varijable.
    # Kod bi trebao zamijeniti liniju s makro naredbom s odgovarajućim linijama 
    # koda za kopiranje sadržaja iz jedne varijable u drugu.
    # Također bi trebao obraditi oznake makro naredbe na odgovarajući način, 
    # kako bi se izbjeglo poklapanje s oznakama iz ostalih dijelova programa
    def _parseLines(self):
        lines = []
        for (line, n) in self._lines:
            # Ako se u prvoj riječi nalazi "$MV", tretirajte liniju kao makro naredbu
            words = line.split()
            if words[0] == "$MV":
                # Parsirajte argumente makro naredbe.
                arg1, arg2 = words[1:]
                # Generirajte kod za kopiranje sadržaja iz jedne varijable u drugu
                lines.append("@" + arg1)
                lines.append("D=M")
                lines.append("@" + arg2)
                lines.append("M=D")
            else:
                # Inače, parsirajte liniju kao normalnu naredbu
                l = self._parseLine(line, n)
                if not self._flag:
                    return False
                if len(l) > 0:
                    lines.append(l)
        self._lines = lines
        return True


    # IMPLEMENTIRATI!
    # Za sada parsiramo SAMO push, pop i aritmeticko/logicke naredbe...
    
    # U ovako napisanoj _parseLine funkciji dodana je provjera da bismo 
    # vidjeli završava li prva riječ retka dvotockom, što označava da 
    # se radi o deklaraciji oznake. Ako se radi o deklaraciji oznake, 
    # provjeravamo postoji li jos rijeci iza nje. Ako postoji jos 
    # rijeci, postavljamo _flag na False i ispisujemo poruku o 
    # pogresci. Ako je deklaracija oznake valjana, pozivamo metodu _label 
    # da generiramo asemblerski kod za nju. Također ova funkcija ovako definirana
    # određuje vrstu naredbe na temelju prve ključne riječi i ignorira jednolinijske
    # komentare i prazne linije
    def _parseLine(self, line, n):
        # Ignoriramo jednolinijske komentare i prazne linije
        l = line.split("//")[0].strip()
        if len(l) == 0:
            return ""
    
        # Dijelimo liniju na rijeci
        words = l.split()
        
        # Provjeravamo pocinje li linija deklaracijom oznake
        if words[0][-1] == ":":
            # Ako postoji neki neprazan string nakon deklaracije oznake, tretiramo to kao pogrešku
            if len(words) > 1:
                self._flag = False
                Parser._error("Parser", n, "Unexpected string after label declaration: " + " ".join(words[1:]))
                return ""
            # Inace, vratite deklaraciju oznake kao komentar.
            return "//" + l + "\n"
    
        # Inace, parsiramo liniju kao normalnu naredbu.
        if words[0] == "push":
            if len(words) == 3:
                return "//" + " ".join(words) + "\n" + self._push(words[1], words[2], n)
            else:
                self._flag = False
                Parser._error("Parser", n, "Undefined command " + l);
                return ""
    
        elif words[0] == "pop":
            if len(words) == 3:
                return "//" + " ".join(words) + "\n" + self._pop(words[1], words[2], n)
            else:
                self._flag = False
                Parser._error("Parser", n, "Undefined command " + l);
                return ""
    
        elif len(words) == 1:
            return "//" + " ".join(words) + "\n" + self._comm(words[0], n)
    
        return ""


    # Funkcija zapisuje asemblerski kod push naredbe.
    # Argumenti:
    #   1. src - segment s kojeg se dogadja push (npr. constant),
    #   2. loc - lokacija push-a (npr. local 5, loc = 5),
    #   3. n - linija izvornog koda (radi vracanja greske).
    def _push(self, src, loc, n):
        return ""

    # Funkcija zapisuje asemblerski kod pop naredbe.
    # Argumenti:
    #   1. dst - segment na koji se vrsi pop (npr. local),
    #   2. loc - lokacija pop-a (npr. local 5, loc = 5),
    #   3. n - linija izvornog koda (radi vracanja greske).
    def _pop(self, dst, loc, n):
        return ""

    # Funkcija zapisuje asemblerski kod a/l naredbe.
    # Argumenti:
    #   1. comm - pozvana naredba (npr. sum),
    #   2. n - linija izvornog koda (radi vracanja greske).
    def _comm(self, comm, n):
        return ""

    def _readFile(self):
        n = 0
        for line in self._file:
            if len(line) > 0:
                self._lines.append((line, n))
            n += 1

    def _writeFile(self):
        for line in self._lines:
            self._file.write(line + "\n")

    @staticmethod
    def _error(src, line, msg):
        if len(src) > 0 and line > -1:
            print("[" + src + ", " + str(line + 1) + "] " + msg)
        elif len(src) > 0:
            print("[" + src + "] " + msg)
        else:
            print(msg)

def main():
    P = Parser()
    P.parseFile("test")

if __name__ == '__main__':
    main()