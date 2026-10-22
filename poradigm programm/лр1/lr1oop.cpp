#include <iostream>
#include <cmath>
#include <set>
using namespace std;
class Urav {
private:
    double A;
    double B;
    double C;
public:
    void setA(double a) { A = a; }
    void setB(double b) { B = b; }
    void setC(double c) { C = c; }
    void reshit() {
        if (A == 0) {
            if (B == 0) {
                if (C == 0) {
                    cout << "Бесконечно много решений (0 = 0)" << endl;
                } else {
                    cout << "Корней нет" << endl;
                }
                return;
            }
            double x = -C / B;
            cout << "Линейное уравнение. Корень:" << endl;
            cout << "x = " << x << endl;
            return;
        }
        double D = B * B - 4 * A * C;
        cout << "Дискриминант = " << D << endl;
        set<double> korni;
        if (D < 0) {
            cout << "Корней нет" << endl;
            return;
        }
        if (D == 0) {
            double t = -B / (2 * A);
            if (t < 0) {
                cout << "Корней нет" << endl;
                return;
            } else {
                korni.insert(sqrt(t));
                korni.insert(-sqrt(t));
            }
        }
        if (D > 0) {
            double t1 = (-B + sqrt(D)) / (2 * A);
            double t2 = (-B - sqrt(D)) / (2 * A);
            if (t1 >= 0) {
                korni.insert(sqrt(t1));
                korni.insert(-sqrt(t1));
            }
            if (t2 >= 0) {
                korni.insert(sqrt(t2));
                korni.insert(-sqrt(t2));
            }
        }
        if (korni.empty()) {
            cout << "Корней нет" << endl;
            return;
        }
        cout << "Корни:" << endl;
        for (double x : korni) {
            cout << "x = " << x << endl;
        }
    }
};
int main() {
    double a, b, c;
    cout << "Введите A: ";
    cin >> a;
    cout << "Введите B: ";
    cin >> b;
    cout << "Введите C: ";
    cin >> c;
    Urav u;
    u.setA(a);
    u.setB(b);
    u.setC(c);
    u.reshit();
    return 0;
}