#include <iostream>

class Geek {

public:
    static int i;

    Geek() {
        i = 0;
    }

    void myFunction() {

        i++;
        std::cout << "Hello Geek!!!" << i << std::endl;
    }
};

int Geek::i;

int main() {
// Creating an object
    Geek t;

// Calling function
    t.myFunction();

    return 0;
}

extern "C" {
Geek *Geek_new() { return new Geek(); }
void Geek_myFunction(Geek *geek) { geek->myFunction(); }
}