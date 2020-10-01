#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int N, K;
    cin >> N >> K;

    vector<int> A(N), S(K, 0);

    for(int i=0; i<N; i++)
    {
        cin >> A[i];
    }
    vector<vector<bool>> found(K + 1), duplicates(K + 1);


    for(int i=0; i <= K; i++)
    {
        size_t size = (100 * 100) + 1;

        found[i].resize(size, 0);
        duplicates[i].resize(size, 0);
    }

    found[0][0] = 1;

    for(int i=0; i<N; i++)
    {
        for(int count = K; count > 0; count--)
        {
            for(int j=0; j < found[count - 1].size(); j++)
            {
                if(!found[count-1][j]) continue;

                int sum = j + A[i];

                if(duplicates[count-1][j] || found[count][sum])
                {
                    duplicates[count][sum] = found[count][sum] = 1;
                }
                else
                {
                    found[count][sum] = 1;
                }
            }
        }
    }
    long ans = 0;

    for(int i=0; i < found[K].size(); i++)
    {
        if(found[K][i] && !duplicates[K][i])
        {
            ans += i;
        }
    }
    cout << ans;
    return 0;
}
