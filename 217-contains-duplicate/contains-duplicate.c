#include <stdlib.h>
#include <stdbool.h>

// פונקציית השוואה ל-qsort
int cmpInt(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;

    if (ia < ib) return -1;
    if (ia > ib) return 1;
    return 0;
}

bool containsDuplicate(int* nums, int numsSize) {
    if (numsSize < 2) {
        return false;
    }

    // ממיין את המערך במקום (in-place)
    qsort(nums, numsSize, sizeof(int), cmpInt);

    // בודק כפילויות על ידי השוואת איברים סמוכים
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i - 1]) {
            return true;
        }
    }

    return false;
}