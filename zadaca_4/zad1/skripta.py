from zad1 import Parser

# Lista sa imenima datoteka koje se parsiraju
files_to_parse = ["test1", "test2", "test3", "test4", "test5", "test6"]

for file in files_to_parse:
    parser = Parser()
    parser.parseFile(file)
    if parser._flag:
        parser.writeFile(file)
        print(f"Parsiranje i zapisivanje datoteke {file}.vm je uspjesno zavrseno")
    else:
        print(f"Parsiranje datoteke {file}.vm nije uspjelo")
