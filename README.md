# Game of Life - Python exercise

This is a small project done in order to introduce programming in python to a small group of students.

## How to execute the program
- With the terminal go to the program directory and run the command `python game_of_life.py` (if needed install python first by following any of the many tutorials available online)
- By default the program generate a random map of 80x20 cells
- If you want to use your own map or one of the examples in `/maps` run the command adding the path to the map at the end (for example `python game_of_life.py maps/square.map`)
- For seek of simplicity the code do not handle properly maps that are not correct (and will give strange results in those cases)

## The Game of Life
- The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970 ([Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)).
- There is 4 Rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Useful resources
- [LifeWiki](https://www.conwaylife.com/wiki/Main_Page) to know everything about Life
- [The Art of Code (Video)](https://www.youtube.com/watch?v=6avJHaC3C2U) is a nice presentation of unsual applications of programming, including Life (at minute 4:20)
- [Golly](http://golly.sourceforge.net/) an open source, cross-platform application for exploring Conway's Game of Life and many other types of cellular automata.

## Acknowledgements
- The big book of small python projects, by Al Sweigart, was a very useful resource both for the choice of the subject than for inspiration for code.
- Special thanks to [Alex](https://github.com/protsaq) for offering me the opportunity to participate to this project.