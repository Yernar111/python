#include <bits/stdc++.h>
using namespace std;


const long long mod = 1e9 + 7;
const long long pw = 31;
string s[155], long_str;
long long mx, str_cnt[155];

vector<long long> prefix_hash(string s) {
    int n = s.size();
    vector<long long> h(n + 5, 0), p(n + 5, 1);
    for (int i = 0; i < n; i++) {
        h[i + 1] = (h[i] * pw + (s[i] - 'a' + 1)) % mod;
        p[i + 1] = (p[i] * pw) % mod;
    }
    return h;
}

long long get_hash(const vector<long long> &h, const vector<long long> &p, int l, int r) {
    long long res = (h[r] - h[l] * p[r - l]) % mod;
    if (res < 0) res += mod;
    return res;
}

void solve(int n){
    mx = INT_MIN;

    for(int i = 1; i <= n; i++) cin >> s[i];

    cin >> long_str;

    auto h = prefix_hash(long_str);

    vector<long long> p(long_str.size() + 1, 1);

    for (int i = 1; i <= long_str.size(); i++) p[i] = (p[i - 1] * pw) % mod;

    for(int i = 1; i <= n; i++){
        long long hash_s = 0, cnt = 0;
        for(char c : s[i]) hash_s = (hash_s * pw + (c - 'a' + 1)) % mod;
        for(int j = 0; j + s[i].size() <= long_str.size(); j++){
            long long substr_hash = get_hash(h, p, j, j + s[i].size());
            if(substr_hash == hash_s) cnt++;
        }
        mx = max(mx, cnt);
        str_cnt[i] = cnt;
    }
    cout << mx << '\n';
    for(int i = 1; i <= n; i++){
        if(str_cnt[i] == mx) cout << s[i] << '\n';
    }
}

int main() {
    int t;
    while(true){

        cin >> t;

        if(t == 0) break;
        else solve(t);

    }
    return 0;
}