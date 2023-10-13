// 최소, 최대
#include <stdio.h>

void swap(int *a, int *b) {
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;
}

// void sort(int *arr, int n) {
//     int i, j;

//     for (i = 0; i < n; i++) {
//         for (j = 0; j < n; j++) {
//             if (arr[i] > arr[j]) {
//                 swap(&arr[i], &arr[j]);
//             }
//         }
//     }
// }

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    
    int nums[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    // scanf("%d %d %d %d %d", &nums[0], &nums[1], &nums[2], &nums[3], &nums[4]);
    
    quickSort(nums, 0, n-1);

    printf("%d %d\n", nums[0], nums[n-1]);

    return 0;    
}