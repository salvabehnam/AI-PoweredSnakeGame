# 🐍 AI-Powered Snake Game

This project presents an **AI-driven Snake game** developed in Python, featuring multiple AI algorithms for autonomous gameplay, including **A* Search**, **Depth-First Search (DFS)**, and **Neural Networks**.

## 📌 Features

- **Multiple AI Algorithms**: Implements A* Search, DFS, and a Neural Network-based AI.
- **Customizable AI Behavior**: Neural Network can be trained and saved for better performance.
- **Game Interface**: Built with Pygame for smooth visualization.
- **Modular Code Structure**: Allows easy expansion and modification of AI behavior.

## 📂 Project Structure

    AI-PoweredSnakeGame/
    ├── Snake.py
    ├── A_STAR.py
    ├── DFS.py
    ├── NN.py
    ├── Algorithm.py
    ├── Fruit.py
    ├── Utility.py
    ├── images/
    │   ├── astar.gif
    │   ├── dfs.gif
    ├── requirements.txt
    └── README.md


## 🚀 Installation & Usage

1. **Clone the Repository**

    ```bash
    git clone https://github.com/salvabehnam/AI-PoweredSnakeGame.git
    cd AI-PoweredSnakeGame
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Game**

    ```bash
    python Snake.py
    ```

    During gameplay, you can select the desired AI algorithm for controlling the snake.

## 🔥 AI Algorithms

- **A star Search (A_STAR.py)**: Uses the A* algorithm for efficient pathfinding.
- **Depth-First Search (DFS.py)**: Explores all possible paths using DFS.
- **Neural Network (NN.py)**: Uses a feedforward neural network to control the snake.

## ✨ Technologies Used

- Python
- Pygame (for game interface)
- NumPy (for numerical computations)
- Pickle (for saving and loading neural network models)

## 🔧 Requirements

```plaintext
pygame
numpy
