#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ULL;

ULL MAX = 11180329;
ULL limit;

char *sieve;

string s;
int q;

ULL Multiply(ULL a, ULL b, ULL mod)
{
    a %= mod;
    b %= mod;

    if(a <= 0xFFFFFFF && b <= 0xFFFFFFF) return (a * b) % mod;

    ULL res = 0;

    __asm__
    (
     "mulq %2\n"
     "divq %3"
     : "=&d" (res), "+%a" (a)
     : "rm" (b), "rm" (mod)
     : "cc"
     );
    return res;
}

ULL Power(ULL n, ULL e, ULL mod)
{
    ULL res = 1;

    while(e > 0)
    {
        if(e & 1) res = Multiply(res, n, mod);

        n = Multiply(n, n, mod);
        e >>= 1;
    }
    return res;
}

bool MillerRabin(ULL n)
{
    const unsigned int mask = 0x208A28Ac;

    vector<ULL> smallPrimes = {2, 3, 5, 7, 11, 13, 17};

    if(n < 31)
    {
        return (mask & (1 << n)) != 0;
    }
    for(auto p : smallPrimes)
    {
        if(n % p == 0) return 0;
    }
    if(n < 17 * 19) return 1;

    const unsigned int STOP = 0;
    const unsigned int A[] = {377687, STOP},
    B[] = {31, 73, STOP},
    C[] = {2, 7, 61, STOP},
    D[] = {2, 13, 23, 1662803, STOP},
    E[] = {2, 3, 5, 7, 11, STOP},
    F[] = {2, 3, 5, 7, 11, 13, STOP},
    G[] = {2, 3, 5, 7, 11, 13, 17, STOP},
    H[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, STOP},
    I[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, STOP},
    J[] = {2, 325, 9375, 28178, 450775, 978054, 1795265022, STOP};

    const unsigned int *test = J;

    if(n < 5329) test = A;
    else if(n < 9080191) test = B;
    else if(n < 4759123141ULL) test = C;
    else if(n < 1122004669633ULL) test = D;
    else if(n < 2152302898747ULL) test = E;
    else if(n < 3474749660383ULL) test = F;
    else if(n < 341550071728321ULL) test = G;
    else if(n < 3825123056546413051ULL) test = H;
    else if(n <= 18446744073709551615ULL) test = I;

    auto d = n - 1;
    d >>= 1;

    unsigned int shift = 0;

    while((d & 1) == 0)
    {
        shift++;
        d >>= 1;
    }

    do
    {
        auto x = Power(*test++, d, n);

        if(x == 1 || x == n - 1) continue;

        bool possible = false;

        for(unsigned int r = 0; r < shift; r++)
        {
            x = Multiply(x, x, n);

            if(x == 1) return 0;
            if(x == n - 1)
            {
                possible = true;
                break;
            }
        }
        if(!possible) return 0;
    }
    while(*test != STOP);

    return 1;
}

bool IsPrime(ULL n)
{
    if(n < 2) return 0;
    if(n <= 3) return 1;
    if(n % 2 == 0 || n % 3 == 0) return 0;

    if(n >= limit * 2) return MillerRabin(n);

    return sieve[n/2];
}

void Sieve(ULL n)
{
    limit = n / 2 + 1;

    sieve = new char[limit];
    fill(sieve, sieve + limit, 1);
    sieve[0] = 0;

    for(ULL p = 1; p*p*2 < limit; p++)
    {
        if(sieve[p])
        {
            for(ULL i = (3*p)+1; i < limit; i += (2*p)+1)
            {
                sieve[i] = 0;
            }
        }
    }
}

bool ContainsSubstring(ULL n)
{
    while(n >= 100)
    {
        if(n % 10 == s[2] - '0')
        {
            ULL temp = n / 10;
            int index = 1;

            while(index >= 0)
            {
                if(temp % 10 != s[index]-'0') break;

                temp /= 10;
                index--;
            }
            if(index == -1) return 1;
        }
        n /= 10;
    }
    return 0;
}

bool IsPrimeproof(ULL n)
{
    string p = to_string(n);

    for(int i = p.size()-1; i >= 0; i--)
    {
        if(n % 2 == 0 && i < p.size() - 1) return 1;

        string temp = p;

        for(char j = (i) ? '0' : '1'; j <= '9'; j++)
        {
            if(j == p[i]) continue;
            if(j % 2 == 0 && i == p.size()-1) continue;

            temp[i] = j;

            if(IsPrime(stoull(temp))) return 0;
        }
    }
    return 1;
}

int main()
{
    cin >> s >> q;

    vector<int> queries(q);

    for(auto &n : queries) cin >> n;

    int mx = *max_element(queries.begin(), queries.end());

    Sieve(MAX);
    vector<ULL> primes = {2};
    vector<ULL> squbes;

    for(ULL i = 3; i <= MAX; i += 2)
    {
        if(IsPrime(i)) primes.push_back(i);
    }

    for(auto a : primes)
    {
        for(auto b : primes)
        {
            if(a == b) continue;

            ULL sqube = (a * a) * (b * b * b);

            if(sqube >= 1000000000000000) break;
            if(ContainsSubstring(sqube))
            {
                squbes.push_back(sqube);
            }
        }
    }
    set<ULL> S(squbes.begin(), squbes.end());
    vector<ULL> ans;

    for(auto sqube : S)
    {
        if(IsPrimeproof(sqube))
        {
            ans.push_back(sqube);

            if(ans.size() == mx) break;
        }
    }
    for(auto n : queries)
    {
        cout << ans[n-1] << "\n";
    }
    return 0;
}
