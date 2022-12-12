@128
D = A
@n
M = D;
@i
M = 0;
@18439
D = A
@scr
M = D
(LOOP_START)
    @n
    D = M;
    @i
    D = M - D;
    @LOOP_END
    D; JGE

    @scr  
    A=M
    M=1

    @32 
    D=A;
    @scr
    M=M+D;
  
    @i
    M = M + 1;
    @LOOP_START
    0; JMP
(LOOP_END)


@i
M=0;
@8
D = A
@n
M = D;

(LOOP_START2)
    @n
    D = M;
    @i
    D = M - D;
    @LOOP_END2
    D; JGE

    @scr
    A = M
    M = -1    
    
    @scr
    M=M+1;

    @i
    M = M + 1;
    @LOOP_START2
    0; JMP
(LOOP_END2)


@i
M=0;
@8
D = A
@n
M = D;
@18439
D = A
@scr
M= D
@br
M=0
@dupler
M=1
(LOOP_START4)
    @n
    D = M;
    @i
    D = M - D;
    @END
    D; JGE
    
    @dupler
    D=M;
    @scr
    A=M;
    M=M|D;

    @32
    D=A;
    @scr
    M=M+D;

    @i
    D=M;
    @PRVI
    D ; JEQ
    @OSTALI
    D ; JNE
  
    (DALJE)
    @br
    D=M-D
    @RESETBR
    D;JEQ
    @DUPLAJBR
    D;JLT
    
    (NASTAVI)
    @br
    M=M+1

    @LOOP_START4
    0; JMP


(RESETBR)
@br
M=0
@dupler
M=1
@i
M = M + 1;
@scr
M=M+1;
@NASTAVI
0;JMP

(DUPLAJBR)
@dupler
D=M;
M=M+D;
@NASTAVI
0;JMP

(PRVI)
@15
D=A;
@DALJE
0; JMP

(OSTALI)
@16
D=A;
@DALJE
0; JMP

(END)
@END
0;JMP