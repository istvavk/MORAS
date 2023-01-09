import re

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

    def _parseLines(self):
        lines = []
        label_count = 0
        for (line, n) in self._lines:
            # Provjera jel linija sadrzi "$SWP" makro naredbu
            match = re.match(r"\$SWP\s*\(\s*(\S+)\s*,\s*(\S+)\s*\)", line)
            if match:
                # Parsira argumente makro naredbe
                arg1, arg2 = match.groups()
                # Generira kod za zamjenu sadrzaja dviju varijabli
                lines.append("// Macro command: $SWP(" + arg1 + ", " + arg2 + ")")
                lines.append("@" + arg1)
                lines.append("D=M")
                lines.append("@" + arg2)
                lines.append("M=D")
                lines.append("@" + arg1)
                lines.append("M=D")
            else:
                # Inace, parsiraj liniju kao normalnu naredbu
                l = self._parseLine(line, n)
                if not self._flag:
                    return False
                if len(l) > 0:
                    lines.append(l)
        self._lines = lines
        return True

    def _parseLine(self, line, n):
        # Igrnorira jednolinijske komentare i prazne linije
        l = line.split("//")[0].strip()
        if len(l) == 0:
            return ""

        # Provjerava jel linija pocinje deklaracijom oznake
        words = l.split()
        if words[0][-1] == ":":
            # Ako postoji neki neprazan string nakon deklaracije oznake, gledamo na to kao pogresku
            if len(words) > 1:
                self._flag = False
                Parser._error("Parser", n, "Unexpected string after label declaration: " + " ".join(words[1:]))
                return ""
            # Inace, vratite deklaraciju oznake kao komentar.
            return "//" + l + "\n"

        # Inace, parsiraj liniju kao normalnu naredbu
        command_type = self._commandType(words[0])
        if command_type == "C_ARITHMETIC":
            return self._arithmetic(words[0], n)
        elif command_type == "C_PUSH":
            return self._push(words[1], words[2], n)
        elif command_type == "C_POP":
            return self._pop(words[1], words[2], n)
        else:
            self._flag = False
            Parser._error("Parser", n, "Unrecognized command: " + words[0])
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