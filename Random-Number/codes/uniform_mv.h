//Defining the function for calculating the mean of random numbers
double mean(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x;
}
fclose(fp);
temp = temp/(i-1);
return temp;

}
//End function for calculating the mean of random numbers

// Defining the function for calculating the variance of random numbers
double variance(char *str, double mean)
{
int i=0;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+(pow(x-mean,2));
}
fclose(fp);
temp = temp/(i-1);
return temp;

}
//End function for calculating the variance of random numbers