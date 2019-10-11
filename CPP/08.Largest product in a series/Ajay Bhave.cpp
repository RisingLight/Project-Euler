// Project Euler : Problem Number 08
#include<iostream>
#include<string>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        string s;
        cin>>s;
        long long int ans=0;
        for(int i=0;i+k<n;i++)
        {
            long long int r=1;
            for(int j=0;j<k;j++)
                r*=s[i+j]-'0';
            if(ans<r)
                ans=r;
        }
        cout<<ans<<endl;
    }
    return(0);
}

