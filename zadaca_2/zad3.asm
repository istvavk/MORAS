@R0
D=M;

@R5
M=D;

@R5
D=M;

@R1
D=M-D;

@MAX
D;JGT

@NASTAVAK
D;JLT

(MAX)
@R1
D=M;

@R5
M=D;
(NASTAVAK)

@R5
D=M;

@R2
D=M-D;

@MAX1
D;JGT

@NASTAVAK1
D;JLT

(MAX1)
@R2
D=M;

@R5
M=D;
(NASTAVAK1)

@R5
D=M;

@R3
D=M-D;

@MAX2
D;JGT

@NASTAVAK2
D;JLT

(MAX2)
@R3
D=M;

@R5
M=D;
(DALJE2)

@R5
D=M;

@R4
D=M-D;

@MAX3
D;JGT

@NASTAVAK3
D;JLT

(MAX3)
@R4
D=M;

@R5
M=D;
(NASTAVAK3)

(END)
@END
0;JMP
