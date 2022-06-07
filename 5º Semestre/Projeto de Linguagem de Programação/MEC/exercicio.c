main()
{
	int A,S,NUM;
	A = 1;
	S = 0;

	while (A <= 100) {
        scanf("%d", &NUM);

        if (NUM > 0) {
            S = S + NUM;
        } else {
			S = S + 200;
		}
        A = A + 1;
	}
	printf("%d", S);
}