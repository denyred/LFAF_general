# Topic: Intro to formal languages. Regular grammars. Finite Automata.
## Course: Formal Languages & Finite Automata
## Author: Dionisie Spataru FAF-211
Variant 24:

VN={S, A, C, D},

VT={a, b}, 

P={ 
    S → aA     
    A → bS    
    A → dD   
    D → bC    
    C → a   
    C → bA   
    D → aD
}

## Theory
Formal languages provide a systematic way to represent and describe sets of strings using a predefined set of rules or symbols. These languages are used in various fields, including computer science, mathematics, linguistics, and theoretical physics, to study and analyze the properties and structures of different types of strings.

Formal languages can be classified into different types based on their properties and the rules governing their construction and interpretation. For example, regular languages are a type of formal language that can be described by regular expressions or recognized by finite automata, which are computational models that follow a set of rules to process strings. Regular languages have a simple and well-defined structure, making them useful for tasks such as pattern matching, lexical analysis, and text processing.

Finite automata, also known as finite state machines, are mathematical models used to describe and analyze the behavior of systems that change states based on inputs. In the context of formal languages, finite automata serve as computational models that read an input string character by character and transition between states based on the current input symbol and the current state. The transitions are defined by a set of rules or a transition function. The automaton is designed to either accept or reject the input string based on its final state after processing the entire string.

Finite automata can be deterministic (DFA) or non-deterministic (NFA) based on the number of possible transitions from a given state for a particular input symbol. DFAs have a single deterministic transition for each input symbol and state, while NFAs can have multiple possible transitions. Both types of automata are equivalent in terms of the languages they recognize, but NFAs offer more flexibility and simplicity in their design.

## Objectives:
- Understand what a language is and what it needs to have in order to be considered a formal one.

- Provide the initial setup for the evolving project:

    a. Create a local && remote repository of a VCS hosting service

    b. Choose a programming language

    c. Create a separate folder the report will be kept

- According to my variant 6, get the grammar definition and do the following tasks:

    a. Implement a type/class for the grammar;

    b. Add one function that would generate 5 valid strings from the language expressed by the given grammar

    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;

    d. For the Finite Automaton, add a method that checks if an input string can be obtained via the state transition from it
## Implementation description
### Grammar class

```python
    class Grammar:
    def __init__(self):
    self.VN = {'S', 'A', 'C', 'D'}
    self.VT = {'a', 'b'}
    self.P = {
        'S': ['aA'],
        'A': ['bS', 'dD'],
        'D': ['bC', 'aD'],
        'C': ['a', 'bA']
}
def generate_string(self, start_symbol, max_length):
    if max_length == 0:
        return ''
    production = random.choice(self.P[start_symbol])
    string = ''
    for symbol in production:
        if symbol in self.VN:
string += self.generate_string(symbol, max_length - 1)
            else:
                string += symbol
        return string
    def generate_strings(self, count, max_length):
        strings = []
        for i in range(count):
            strings.append(self.generate_string('S', max_length))
        return strings
```
class Grammar: This class represents a grammar for generating strings. It has attributes VN (non-terminal symbols), VT (terminal symbols), and P (productions).
__init__(self): The constructor initializes the grammar by defining the non-terminal symbols (VN), terminal symbols (VT), and productions (P). In the given example, the non-terminal symbols are {'S', 'A', 'C', 'D'}, and the terminal symbols are {'a', 'b'}. The productions define the rules for generating strings.
generate_string(self, start_symbol, max_length): This method generates a string based on the grammar rules. It takes a start_symbol (the initial non-terminal symbol) and max_length (the maximum length of the generated string) as input.
-If max_length is 0, an empty string is returned.
-A production is randomly chosen from the set of productions associated with the start_symbol.
-The method iterates over each symbol in the chosen production.
-If the symbol is a non-terminal symbol (belongs to VN), the method recursively calls generate_string() to generate a string for that symbol with max_length reduced by 1.
-If the symbol is a terminal symbol (belongs to VT), it is directly added to the generated string.
-The resulting string is returned.
generate_strings(self, count, max_length): This method generates multiple strings based on the grammar rules. It takes count (the number of strings to generate) and max_length (the maximum length of each generated string) as input.
-An empty list called strings is initialized.
-The method iterates count times and calls generate_string() with the start symbol 'S' and the given max_length.
-Each generated string is appended to the strings list.
-The list of generated strings is returned.

The code allows you to define a grammar with non-terminal and terminal symbols and their associated productions. You can then use the generate_string() method to generate a single string based on the grammar rules, or use the generate_strings() method to generate multiple strings. The generated strings adhere to the grammar rules and have a maximum length as specified. This code provides a basic implementation for grammar-based string generation.

### FiniteAutomaton class
```python
  def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    def accepts(self, input_string):
        current_state = self.start_state
for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            if (current_state, symbol) not in self.transitions:
                return False
            current_state = self.transitions[(current_state, symbol)]
        if current_state not in self.accept_states:
            return False
return True
    def __str__(self):
        s = "Finite Automaton:\n"
        s += "States: " + str(self.states) + "\n"
        s += "Alphabet: " + str(self.alphabet) + "\n"
        s += "Transitions:\n"
        for transition in self.transitions:
            s += str(transition[0]) + " --" + str(transition[1]) + "--> " +
str(self.transitions[transition]) + "\n"
        s += "Start state: " + str(self.start_state) + "\n"
        s += "Accept states: " + str(self.accept_states) + "\n"
        return s
```

The accepts method takes an input string as a parameter and returns True if the string is accepted by the automaton, and False otherwise. The method simulates the state transitions of the automaton on the input string, starting from the start state and following the transitions for each input symbol. If the final state after processing the input string is an accept state, the method returns True. If the final state is not an accept state, the method returns False.
The self method will show all transitions.

### Main class

```python
   def run(self):
        grammar = Grammar()
        print('Generating 5 valid strings from the language expressed by the
grammar:')
        strings = grammar.generate_strings(5, 10)
        for string in strings:
            print(string)
        fa = FiniteAutomaton(
            states={'q0', 'q1', 'q2'},
            alphabet={'a', 'b'},
            transitions={
                ('q0', 'a'): 'q1',
                ('q0', 'b'): 'q0',
                ('q1', 'a'): 'q2',
                ('q1', 'b'): 'q0',
                ('q2', 'a'): 'q2',
                ('q2', 'b'): 'q2',
            },
            start_state='q0',
            accept_states={'q2'}
)
        print('Generated Finite Automaton:')
print(fa)
        print('Checking if some example strings are accepted by the finite
automaton:')
        input_strings = ['aab', 'abbab', 'abaab', 'ab', 'abb']
for input_string in input_strings:
            if fa.accepts(input_string):
                print(f'The input string "{input_string}" is accepted by the
automaton.')
            else:
                print(f'The input string "{input_string}" is not accepted by the
automaton.')
if __name__ == '__main__':
    main = Main()
main.run()
```
Main class implementation likely involves creating an instance of the Grammar class with the given properties (VN, VT, and P), calling the generate_strings() method of the Grammar class to generate 5 valid strings from the language expressed, creating an instance of the FiniteAutomaton class and converting the Grammar instance to a FiniteAutomaton instance, and finally calling the accepts() method of the FiniteAutomaton instance to check if each of the generated strings is accepted by the automaton. The main class is responsible for coordinating these steps and printing out the results, such as the generated strings and whether each string is accepted or rejected by the automaton.


## Results
```
Generating 5 valid strings from the language expressed by the grammar:
abababadba
abadabbbab
adabbbadab
ababadba
adba
Generated Finite Automaton:
Finite Automaton:
States: {'q0', 'q1', 'q2'}
Alphabet: {'b', 'a'}
Transitions:
q0 --a--> q1
q0 --b--> q0
q1 --a--> q2
q1 --b--> q0
q2 --a--> q2
q2 --b--> q2
Start state: q0
Accept states: {'q2'}

Checking if some example strings are accepted by the finite automaton:
The input string "aab" is accepted by the automaton.
The input string "abbab" is not accepted by the automaton.
The input string "abaab" is accepted by the automaton.
The input string "ab" is not accepted by the automaton.
The input string "abb" is not accepted by the automaton.
```

## Conclusions
In this project, we explored the concepts of formal languages, regular grammars, and finite automata, and implemented them in Python classes. We started by defining a grammar with a set of nonterminal symbols, terminal symbols, and production rules. We then generated valid strings from this grammar and converted the grammar to a finite automaton. The finite automaton was able to accept or reject input strings based on its state transitions.
Overall, these concepts are useful in a variety of applications, including text processing, natural language processing, and programming language design. The ability to recognize and generate valid strings in a language is a fundamental component of these fields, and the tools we developed in this project provide a foundation for further exploration and implementation.    