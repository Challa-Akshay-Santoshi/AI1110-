void GenerateSample(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",-2*(log(1-(double)rand()/RAND_MAX)));
}
fclose(fp);

}
