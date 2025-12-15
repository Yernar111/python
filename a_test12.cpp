#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<long long> get_h(string s) {
    int n = s.size();
    vector<long long> h(n);

    h[0] = s[0];
    long long p = 29;
    long long p_pow = 29;

    for (int i = 1; i < n; i++) {
        h[i] = h[i - 1] + s[i] * p_pow;
        p_pow *= p;
    }

    return h;
}

int main() {
    string s;
    cin >> s;

    int n = s.size();

    // Precompute powers
    vector<long long> p(n);
    p[0] = 1;
    for (int i = 1; i < n; i++)
        p[i] = p[i - 1] * 29;

    // Compute prefix hashes
    vector<long long> h = get_h(s);

    // Use set to store unique hashes
    set<long long> distinct_hashes;

    // Generate all substrings
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            // Hash of substring [i, j]
            long long hash = h[j];
            if (i > 0)
                hash = hash - h[i - 1];

            distinct_hashes.insert(hash);  // O(log n)
        }
    }

    cout << "Number of distinct substrings: ";
    cout << distinct_hashes.size() << endl;

    return 0;
}