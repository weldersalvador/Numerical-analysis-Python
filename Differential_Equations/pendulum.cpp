#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double g = 9.81;
    double L = 10.0;

    double w = 0.5; //Initial condition
    double theta = 0.0; //Initial condition

    double dt = 0.01;

    for(int i = 0; i < 10000; i++){
        double new_w = w - (g/L)*sin(theta)*dt;
        double new_theta = theta + w*dt;

        theta = new_theta;
        w = new_w;

        cout << "Time: " << i*dt << endl;
        cout << "Theta: " << theta << endl;
        cout << endl;
    }

    return 0;
}