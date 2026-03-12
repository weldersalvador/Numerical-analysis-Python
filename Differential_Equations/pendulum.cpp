#include <iostream>
#include <cmath>

#include <SFML/Graphics.hpp>
using namespace std;

int main(){
    double g = 9.81;
    double L = 10.0;

    double w = 0.5; //Initial condition
    sf::Angle theta = sf::degrees(0.0); //Initial condition

    sf::Time dt = sf::seconds(0.01);

    sf::Time time = sf::seconds(0);

    sf::RenderWindow window(sf::VideoMode({800,600}), "Teste");

    window.setFramerateLimit(60);

    sf::CircleShape circle(50);
    circle.setPosition({375,275});

    while(window.isOpen())
    {
        while(const std::optional event = window.pollEvent())
        {
            if(event->is<sf::Event::Closed>())
                window.close();
        }

        window.clear(sf::Color::Black);
        window.draw(circle);
        window.display();
    }


    for(int i = 0; i < 100; i++){
        double new_w = w - (g/L)*sin(theta.asRadians())*dt.asSeconds();
        sf::Angle d_angle = sf::degrees(dt.asSeconds()*w);
        sf::Angle new_theta = theta + d_angle;

        theta = new_theta;
        w = new_w;

        time += dt;

        cout << "Time: " << time.asSeconds() << "s" << endl;
        cout << "Theta: " << theta.asDegrees() << endl;
        cout << endl;
    }

    return 0;
}