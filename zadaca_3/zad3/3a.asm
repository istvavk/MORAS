 // spremamo bazu u registar R0, eksponent u registar R1, a rezultat počinjemo pohranjivati u D registar kao 1
  // zatim se pokreće ciklus u kojem se provjerava je li eksponent jednak 0. Ako je eksponent jednak 0, 
  // izlazimo iz ciklusa i spremamo rezultat u R2. Ako nije, množimo trenutni rezultat s bazom i smanjujemo 
  // eksponent za 1 te nastavljamo s ciklusom


  // Spremamo bazu u R0
    @R0
    D=M

    // Spremamo eksponent u R1
    @R1
    D=D-M

    // Postavljamo rezultat na 1
    @1
    D=A

    // Počinjemo ciklus
petlja:
    // Provjeravamo je li eksponent jednak 0
    @R1
    D=D-M
    @kraj
    D;JEQ

    // Množimo trenutni rezultat s bazom
    @R0
    D=D*M

    // Smanjujemo eksponent za 1
    @R1
    M=M-1

    // Nastavljamo s ciklusom
    @petlja
    0;JMP

kraj:
    // Spremamo rezultat u R2
    @R2
    M=D

    // Završavamo program
    @KRAJ
    0;JMP
