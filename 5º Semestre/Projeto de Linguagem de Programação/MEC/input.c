main()
{
	int N,K;
	int F1,F2,F3;

	scanf("%d", &N);
	F1=0; F2=1; K=1;
	while (K <= N)
	{
		F3=F1+F2;
		F1=F2;
		F2=F3;
		K=K+1;
	}
	printf("%d", N);
    printf("%d",  F1);
}
