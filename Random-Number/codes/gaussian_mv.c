#include <stdio.h>
#include <math.h>
#include "gaussian_mv.h"

int main()
{
    printf("Mean = %lf\n",mean("gau.dat"));
    printf("Variance = %lf\n",variance("gau.dat", mean("gau.dat")));
}