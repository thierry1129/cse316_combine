B=[-2/7 5/7 4/7 -3/7 -2/7 -2/7
    5/7 -2/7 4/7 -3/7 -2/7 -2/7
    4/7 4/7 -9/14 5/14 -3/7 -3/7
    -3/7 -3/7 5/14 -9/14 4/7 4/7
    -2/7 -2/7 -3/7 4/7 -2/7 5/7
    -2/7 -2/7 -3/7 4/7 5/7 -2/7];



[V,D] = eig(B);
maxEigValue = D(end)
maxEigVector = V(:,6)