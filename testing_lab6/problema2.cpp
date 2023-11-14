
#include <iostream>
#include <vector>

using namespace std;

void sieve(int n) {
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) {
            cout << i << " ";
        }
    }
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Prime numbers up to " << n << " are: ";
    sieve(n);
    cout << endl;
    return 0;
}
