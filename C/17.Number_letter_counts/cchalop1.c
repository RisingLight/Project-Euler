//Euler Number_letter_count_17
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char **intiAllUnits() {
    char **allUnits = malloc(sizeof(char *) * 10);
    allUnits[0] = "one";
    allUnits[1] = "two";
    allUnits[2] = "three";
    allUnits[3] = "four";
    allUnits[4] = "five";
    allUnits[5] = "six";
    allUnits[6] = "seven";
    allUnits[7] = "eight";
    allUnits[8] = "nine";
    return allUnits;
}

char **initAllTen() {
    char **allTen = malloc(sizeof(char *) * 10);
    allTen[0] = "ten";
    allTen[1] = "twenty";
    allTen[2] = "thirty";
    allTen[3] = "forty";
    allTen[4] = "fifty";
    allTen[5] = "sixty";
    allTen[6] = "seventy";
    allTen[7] = "eighty";
    allTen[8] = "ninety";
    return allTen;
}

char *concat(const char *s1, const char *s2)
{
    char *result = malloc(strlen(s1) + strlen(s2) + 1);
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

char **initAllHundred() {
    char **allHundred = malloc(sizeof(char *) * 10);
    char **allUnits = intiAllUnits();

    for (int i = 0; i < 9; i++) {
        allHundred[i] = concat(allUnits[i], "hundred");
    }
    return allHundred;
}

char **intiAllTens() {
    char **allTens = malloc(sizeof(char *) * 10);
    allTens[0] = "ten";
    allTens[1] = "eleven";
    allTens[2] = "twelve";
    allTens[3] = "thirteen";
    allTens[4] = "fourteen";
    allTens[5] = "fifteen";
    allTens[6] = "sixteen";
    allTens[7] = "seventeen";
    allTens[8] = "eighteen";
    allTens[9] = "nineteen";
    return allTens;
}

int getNbr(char **av) {
    if (av[1] != NULL) {
        return atoi(av[1]);
    } else {
        return 0;
    }
}

int lenghtNum(int nbr) {
    int tmp = 10;
    while (nbr / tmp) {
        tmp *= 10;
    }
    return tmp;
}

int countLetter(int nbr) {
    char **allUnits = intiAllUnits();
    char **allTen = initAllTen();
    char **allHundred = initAllHundred();
    char **allTens = intiAllTens();
    int size = 0;
    int save = nbr;
    bool displayAnd = false;

    if (nbr < 10) {
        return strlen(allUnits[nbr - 1]);
    }
    for (int x = lenghtNum(nbr); nbr % x >= 10; x /= 10) {
        if (x == 1000) {
            size = strlen(allHundred[(nbr / 100) - 1]);
            displayAnd = true;
        }
        if (x == 100) {
            if ((nbr / 10) % 10 >= 0) {
                if (displayAnd) {
                    size += 3;
                    displayAnd = false;
                }
                if (nbr % 100 >= 10 && nbr % 100 < 20) {
                    size += strlen(allTens[nbr % 10]);
                    free(allUnits);
                    free(allTen);
                    free(allTens);
                    free(allHundred);
                    return size;
                }
                size += strlen(allTen[((nbr / 10) % 10) - 1]);
            }
        }
    }
    if ((nbr % 10) > 0) {
        size += strlen(allUnits[(nbr % 10) - 1]);
    }
    free(allUnits);
    free(allTen);
    free(allTens);
    free(allHundred);
    return size;
}

int main(int ac, char **av) {
    int nbr = getNbr(av);

    if (nbr < 1 || nbr >= 1000) {
        return 0;
    }
    int size = countLetter(nbr);
    printf("size = %d\n", size);
    return size;
}
