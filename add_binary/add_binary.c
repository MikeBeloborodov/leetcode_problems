#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * add_binary(char * a, char * b);

int main()
{
    char num1[] = "111";
    char num2[] = "10";

    char * result = add_binary(num1, num2);
    printf("%s + %s = %s", num1, num2, result);

    return 0;
}

char * add_binary(char * a, char * b)
{
    int i = strlen(a) - 1;
    int j = strlen(b) - 1;
    int carry = 0;
    int numA, numB, sum, longest;

    longest = i + 1;
    if (j + 1 > longest)
        longest = j + 1;
    int index_result = longest - 1;

    char * result = malloc(sizeof(char) * longest);

    while (i >= 0 || j >= 0){
        numA = 0; // default
        if (i >= 0)
            if (a[i] == '1')
                numA = 1;

        numB = 0; // default
        if (j >= 0)
            if (b[j] == '1')
                numB = 1;

        sum = numA + numB + carry;

        result[index_result] = '0';
        if (sum % 2 != 0){
            result[index_result] = '1';
        }
        index_result--;

        carry = sum / 2;

        i--;
        j--;
    }

    if (carry == 0){
        return result;
    } else {
        char * new_result = malloc(sizeof(char) * (longest + 1));

        for (int i = longest; i >= 0; i--){
            new_result[i] = result[i - 1];
        }

        new_result[0] = '1';

        free(result);
        return new_result;
    }
}
