#include <iostream>

int cmmdc(int a, int b) {
    while (a != b) {
        if (a > b) {
            a -= b;
        } else {
            b -= a;
        }
    }
    return a;
}

int main() {
    int a, b;
    std::cout << "Enter two numbers: ";
    std::cin >> a >> b;
    std::cout << "The cmmdc of " << a << " and " << b << " is " << cmmdc(a, b) << std::endl;
    return 0;
}
