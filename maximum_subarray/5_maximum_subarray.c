#include <stdio.h>
#include <stdlib.h>

int max_sub_array(int* nums, int numsSize)
{
    // O(2n) == O(n) solution
    int sums[numsSize];
    sums[0] = nums[0];
    int max_sum;

    for (int i = 1; i < numsSize; i++){
        if (nums[i] > nums[i] + sums[i - 1]){
            sums[i] = nums[i];
        } else {
            sums[i] = sums[i - 1] + nums[i];
        }
    }
    max_sum = sums[0];
    for (int i = 1; i < numsSize; i++){
        if (sums[i] > max_sum){
            max_sum = sums[i];
        }
    }

    return max_sum;
}

int main()
{
    printf("Hello world");

    return 0;
}
