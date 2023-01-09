// Učitavanje adrese početka polja u RAM-u u privremenu varijablu R1
@100
D=A
@R1
M=D

// Učitavanje duljine polja u privremenu varijablu R2
@R0
D=M
@R2
M=D

// Početak sortiranja polja
(label_sort_loop)
    // Provjera za izlaz iz petlje. Ako je R2 = 0, sortiranje je završeno.
    @R2
    D=M
    @label_sort_done
    D;JEQ
    
    // Učitavanje prvog elementa polja u privremenu varijablu R3
    @R1
    D=M
    @R3
    M=D
    // Učitavanje drugog elementa polja u privremenu varijablu R4
    @R1
    D=M
    @1
    D=D+A
    @R4
    M=D
    
    // Usmjeravanje na odgovarajuću rutinu za sortiranje elementa R3 i R4
    @routine_sort
    0;JMP

(label_sort_done)

// Ispis sortiranog polja
@R1
D=M
@R0
D=D+A
@R2
M=D
(label_print_loop)
    // Provjera za izlaz iz petlje. Ako je R2 = R1, ispis je završen.
    @R2
    D=M
    @R1
    D=D-M
    @label_print_done
    D;JEQ
    
    // Ispis elementa polja
    @R1
    A=M
    D=M
    @output
    M=D
    @1
    D=A
    @R1
    M=M+D
    
    // Povećavanje brojača za 1
    @R2
    M=M-1
    @label_print_loop
    0;JMP

(label_print_done)

// Kraj
@end
0;J