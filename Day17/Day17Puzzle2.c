
// I saw online that people were trying to figure out what the register A had to look like.
// Then, I realized that I can break up the search.



#include <stdio.h>

#define PLEN 16
#define INPLEN 32
#define INTERVAL (1 << 24)

// #define PLEN 6
// #define INPLEN 12


char program[INPLEN] = "2,4,1,1,7,5,1,5,4,5,0,3,5,5,3,0";

// char program[INPLEN] = "0,3,5,4,3,0";

unsigned long long A = 0;
unsigned long long B = 0;
unsigned long long C = 0;

unsigned long long ans = 0;

char res[17];


unsigned long long combo(char operand);



main()
{
    unsigned long long j;
    int i, l;
    char prog[PLEN], opcode, operand, target1[8], target2[8];
    target1[0] = 4;
    target1[1] = 5;
    target1[2] = 0;
    target1[3] = 3;
    target1[4] = 5;
    target1[5] = 5;
    target1[6] = 3;
    target1[7] = 0;
    target2[0] = 2;
    target2[1] = 4;
    target2[2] = 1;
    target2[3] = 1;
    target2[4] = 7;
    target2[5] = 5;
    target2[6] = 1;
    target2[7] = 5;
    for (i = 0; i < PLEN; i++) {
        prog[i] = (program[2*i] - '0');
    }
    j = 0;
    while (j < INTERVAL) {
        i = 0;
        l = 0;
        A = j;
        B = 0;
        C = 0;
        while (i < PLEN) {
            opcode = prog[i];
            operand = prog[i+1];
            if (opcode == '\000') {
                A >>= combo(operand);
            }
            else if (opcode == '\001') {
                B ^= ((unsigned long long) operand);
            }
            else if (opcode == '\002') {
                B = (unsigned long long) (combo(operand) & '\007');
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
                if (l == 8) {
                    l++;
                    printf("size limit reached\n");
                    break;
                }
                else {
                    if (target1[l] != (((char) combo(operand)) & '\007')) {
                        break;
                    }
                    l++; 
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
        if ((l == 8)) {
            printf("found!\n%llu\n", j);
            break;
        }
        j++;
    }
    ans = j;
    ans <<= 24;
    j = 0;
    while (j < INTERVAL) {
        i = 0;
        l = 0;
        A = ans + j;
        B = 0;
        C = 0;
        while (i < PLEN) {
            opcode = prog[i];
            operand = prog[i+1];
            if (opcode == '\000') {
                A >>= combo(operand);
            }
            else if (opcode == '\001') {
                B ^= ((unsigned long long) operand);
            }
            else if (opcode == '\002') {
                B = (unsigned long long) (combo(operand) & '\007');
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
                if (l == 16) {
                    l++;
                    printf("size limit reached\n");
                    break;
                }
                else {
                    if (prog[l] != (((char) combo(operand)) & '\007')) {
                        break;
                    }
                    res[l] = (((char) combo(operand)) & '\007') + '0';
                    l++; 
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
        if ((l == 16)) {
            printf("found!\n%llu\n", j);
            break;
        }
        j++;
    }
    res[16] = '\0';
    printf("%s\n", res);
    ans += j;
    printf("answer is %llu\n", ans);
}




unsigned long long combo(char operand)
{
    if (operand == '\004')
        return A;
    else if (operand == '\005')
        return B;
    else if (operand == '\006')
        return C;
    else
        return (unsigned long long) operand;    
}