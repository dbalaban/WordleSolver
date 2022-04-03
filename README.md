# WordleSolver
A simple python script which helps you solve the game wordle and variants.

Run the application from the command line:

python3 src/main.py

You will be provided with suggested guesses, to refine the suggestion enter the word you guessed along with the result string from the game's feedback.

Result string format: 'g', 'b', or 'y' representing "green", "black" or "yellow" for each corresponding letter in the guessed word.

For example if you guess "cares" and the result was: black, black, black, yellow, green; type "cares-bbbyg" and hit "enter" at the prompt.

Known issue: when guessing words with double letters, if the true word contains only one letter wordle will color one of them black, the app will interpret the corresponding result string as a contradiction and claim there are no possible words left to try. In these cases, the user should prefer the character 'y' over 'b'. For example if you guessed "idiom" and the result string would otherwise be "gybyb" input "gyyyb" instead.
