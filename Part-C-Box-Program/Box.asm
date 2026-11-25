// Part C - Make the Computer Draw a Box
// Student: Tiya Mishra
// Roll Number: 2501730026
// K = 26
// Starting Row = 26
// Width = 48 pixels
// Height = 20 rows

(LOOP)
    @KBD
    D=M
    @DRAW
    D;JGT

    @CLEAR
    0;JMP

// Draw black box
(DRAW)
    @17216
    D=A
    @R13
    M=D

    @20
    D=A
    @R14
    M=D

(DRAW_ROW)
    @R13
    A=M
    M=-1

    A=A+1
    M=-1

    A=A+1
    M=-1

    @R13
    D=M
    @32
    D=D+A
    @R13
    M=D

    @R14
    MD=M-1

    @DRAW_ROW
    D;JGT

    @LOOP
    0;JMP

// Clear the box
(CLEAR)
    @17216
    D=A
    @R13
    M=D

    @20
    D=A
    @R14
    M=D

(CLEAR_ROW)
    @R13
    A=M
    M=0

    A=A+1
    M=0

    A=A+1
    M=0

    @R13
    D=M
    @32
    D=D+A
    @R13
    M=D

    @R14
    MD=M-1

    @CLEAR_ROW
    D;JGT

    @LOOP
    0;JMP