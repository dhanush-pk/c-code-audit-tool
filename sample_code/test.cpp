#include <iostream>
using namespace std;

int main() {
    char buffer[10];
    gets(buffer);  // unsafe
    cout << buffer;
    return 0;
}
