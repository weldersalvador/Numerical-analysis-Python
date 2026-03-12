#include <SFML/Graphics.hpp>
#include <thread>
#include <chrono>

int main()
{
    sf::RenderWindow window(sf::VideoMode({800,600}), "Teste");

    std::this_thread::sleep_for(std::chrono::seconds(5));

    return 0;
}