#include <bits/stdc++.h>
using namespace std;


const long long mod1 = 1e9 + 7;
const long long mod2 = 1e9 + 9;
const long long pw1 = 31;
const long long pw2 = 37;

vector<long long> h1(2002, 0), h2(2002, 0);
vector<long long> p1(2002, 1), p2(2002, 1);

pair<long long, long long> get_hash(int l, int r) {
    pair<long long, long long> res = {(h1[r] - h1[l] * p1[r - l]) % mod1, (h2[r] - h2[l] * p2[r - l]) % mod2};
    if (res.first < 0) res.first += mod1;
    if (res.second < 0) res.second += mod2;
    return res;
}

void solve(){
    string s;
    unordered_set<uint64_t> st;

    cin >> s;

    int n = s.size();

    for (int i = 0; i < n; i++) {
        h1[i + 1] = (h1[i] * pw1 + (s[i] - 'a' + 1)) % mod1;
        h2[i + 1] = (h2[i] * pw2 + (s[i] - 'a' + 1)) % mod2;
    }

    for(int i = 1; i <= s.size(); i++){
        for(int j = 0; j + i <= s.size(); j++){
            pair<long long, long long> p = get_hash(j, j + i);
            uint64_t combine = ((uint64_t)p.first << 32) | ((uint64_t)p.second);
            st.insert(combine);
        }
    }
    cout << st.size();


}

int main() {
    int t;
    for (int i = 1; i < 2002; i++) {
        p1[i] = (p1[i-1] * pw1) % mod1;
        p2[i] = (p2[i-1] * pw2) % mod2;
    }
    solve();
    return 0;
}