#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni.dat", 1000000);

//Gaussian random numbers
gaussian("gau.dat", 1000000);

//Mean of uniform
//printf("Mean = %lf\n",mean("uni.dat"));

//Variance of uniform
//printf("Variance = %lf\n",variance("uni.dat", mean("uni.dat"))); 

//Mean of gaussian
printf("Mean = %lf\n",mean("gau.dat"));

//Variance of gaussian
printf("Variance = %lf\n",variance("gau.dat", mean("gau.dat")));
return 0;

}
