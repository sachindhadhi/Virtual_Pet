# Virtual Pet Game

Welcome to the Virtual Pet Game, a console-based simulation inspired by the classic Tamagotchi. This interactive game allows users to adopt, care for, and interact with a virtual pet in a fun and engaging way. The game continuously updates the pet's status, providing a dynamic and immersive experience.

## Features

- **Adopt a Pet**: Name your pet and choose its species to start your journey.
- **Real-Time Updates**: The pet's hunger and happiness levels change over time, simulating a realistic environment.
- **Interactive Commands**: Feed and play with your pet to keep it happy and healthy.
- **Mood Indicator**: The pet's mood changes based on its hunger and happiness levels, adding an emotional dimension to the game.
- **Dynamic Status Display**: A beautifully formatted status display shows the pet's current state, including its name, species, hunger, happiness, and mood.

## How It Works

- The game runs in a loop, allowing the user to feed or play with the pet.
- A background thread continuously updates the pet's hunger and happiness levels every 10 seconds.
- If either the hunger or happiness level drops below 25, the pet's mood changes to "Sad". Otherwise, the mood remains "Happy".
- The game can be exited gracefully by pressing `Ctrl+C`.

## Getting Started

1. **Clone the repository**:
   ```sh
   git clone https://github.com/sachindhadhi/Virtual_Pet.git
   ```
2.**Navigate the project directory**:
```sh
cd virtual-pet-game
```
3.**Run the game**

## Technologies Used

- **Python**: The primary programming language used for the game logic and threading.
- **Threading**: Used to update the pet's status in real-time without blocking user interactions.

## Future Enhancements

- **More Interactive Commands**: Add commands such as "clean", "sleep", etc., to provide more ways to interact with the pet.
- **Graphical User Interface (GUI)**: Implement a GUI to make the game more visually appealing and user-friendly.
- **Unique Pet Behaviors**: Introduce different species of pets, each with unique behaviors and needs.
- **Sound Effects and Animations**: Add audio and visual effects to enhance the gaming experience.

## Contributions

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and create a pull request.
