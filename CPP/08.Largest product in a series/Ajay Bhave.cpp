// Project Euler : Problem Number 08
#include<iostream>
#include<string>
using namespace std;
#define ll long long
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n,k;
        cin>>n>>k;
        string s;
        cin>>s;
        int a[n];
        for(ll i=0;i<n;i++)
        {
            a[i]=(int)(s[i])-48;
        }
        ll m=INT_MIN;
        for(ll i=0;i<n-k+1;i++)
        {
            ll s=1;
            for(ll j=0;j<k;j++)
            s*=a[j+i];
            m=max(m,s);
        }
        cout<<m<<endl;
    }
    return(0);
}

