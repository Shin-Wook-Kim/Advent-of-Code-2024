#include <stdio.h>

#define PLEN 16
#define INPLEN 31


char program[INPLEN] = "2,4,1,1,7,5,1,5,4,5,0,3,5,5,3,0";

unsigned long A = 30344604;
unsigned long B = 0;
unsigned long C = 0;


unsigned long combo(char operand);



main()
{
    int i;
    int l=0;
    char prog[16], opcode, operand, ans[40];
    for (i = 0; i < 16; i++) {
        prog[i] = (program[2*i] - '0');
    }
    i = 0;
    while (i < PLEN) {
        opcode = prog[i];
        operand = prog[i+1];
        if (opcode == '\000') {
            A >>= combo(operand);
        }
        else if (opcode == '\001') {
            B ^= ((unsigned long) operand);
        }
        else if (opcode == '\002') {
            B = (combo(operand) & 07);
        }
        else if (opcode == '\003') {
            if (A != 0) {
                i = (int) operand;
                continue;
            }
        }
        else if (opcode == '\004') {
            B ^= C;
        }
        else if (opcode == '\005') {
            if (l == 0) {
                ans[l++] = (combo(operand) & '\007') + '0';
            }
            else{
                ans[l++] = ',';
                ans[l++] = (combo(operand) & '\007') + '0';
            }
        }
        else if (opcode == '\006') {
            B = A >> combo(operand);
        }
        else {
            C = A >> combo(operand);
        }
        i += 2;
    }
    ans[l] = '\0';
    printf("%s\n%s\n%d", program, ans, l);
}





unsigned long combo(char operand)
{
    if (operand == '\004')
        return A;
    else if (operand == '\005')
        return B;
    else if (operand == '\006')
        return C;
    else
        return (unsigned long) operand;    
}