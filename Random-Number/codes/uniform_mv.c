#include <stdio.h>
#include <math.h>
#include "uniform_mv.h"

int main()
{
    printf("Mean = %lf\n",mean("uni.dat"));
    printf("Variance = %lf\n",variance("uni.dat", mean("uni.dat")));
}