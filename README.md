# 🐢 Turtle Concentric Circles

A simple yet visual **Python Graphics Script** using the `turtle` module. This program asks the user for a number and automatically draws that many perfectly aligned concentric circles, expanding outwards from a central point.



[Image of python turtle concentric circles]


## 🚀 Features

* **User Interaction:** Accepts a custom number of circles (`n`) from the console.
* **Dynamic Drawing:**
    * Automatically calculates radius expansion.
    * Adjusts the starting coordinates (`y-axis`) to keep all circles centered around the same point.
* **Visuals:** Uses standard Turtle graphics with high drawing speed.

## 🛠️ Logic Explained

The script uses a loop to draw circles while adjusting the turtle's position to maintain a common center:

| Variable | Purpose |
| :--- | :--- |
| `n` | Total number of circles to draw (User Input). |
| `radius` | Starts at 20 and increases by `offset` (10) each iteration. |
| `offset` | The gap between each circle. |
| `turtle.goto(x, y-offset)` | Moves the drawing cursor down so the new, larger circle remains concentric. |

## 💻 How to Run

### 1. Prerequisites
You need Python installed. The `turtle` library is included with Python by default, so no extra installation is needed.

### 2. Run the Script
Open your terminal or command prompt and run:

```bash
python main.py
```

### 3. Input
The program will look like it is "frozen" in the terminal. It is waiting for you to type a number and press Enter.
```bash
Enter Number of Circles: 10
```
A separate window will pop up and draw the circles immediately.

## 📝 Example Usage
#### Console Input:
```text
Enter Number of Circles: 15
```
## Result:
* The Turtle window opens.
* It draws 15 circles.
* The smallest circle has a radius of 20.
* The largest circle has a radius of $20 + (14 \times 10) = 160$.


## ⚠️ Requirements
* **Python 3.x**
* **Tkinter support** (Usually installed with Python automatically).
