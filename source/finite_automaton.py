import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from collections import defaultdict

class FiniteAutomaton:
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

    def to_regular_grammar(self):
        rules = []
        # Create a rule for each transition
        for (state, symbol), next_state in self.transitions.items():
            # If the transition goes to an accept state, add it to the RHS of the rule
            if next_state in self.accept_states:
                rhs = symbol
            # Otherwise, add a new nonterminal symbol and create a rule to that symbol and the symbol on the RHS
            else:
                rhs = f"<{next_state}> {symbol}"
                rules.append(f"<{next_state}> {'|'.join([symbol + f'<{s}>' for s in self.states if (next_state, s) in self.transitions.keys()])}")
            # Add the new rule to the list of rules
            rules.append(f"<{state}> {rhs}")
        # Create the start symbol and add it to the rules
        rules.append(f"S <{self.start_state}>")
        # Join the list of rules and return them as a string
        return "\n".join(rules)

    def is_deterministic(self):
        # implementation of is_deterministic method
        visited_states = set()
        queue = [self.start_state]
        while queue:
            curr_state = queue.pop(0)
            if curr_state in visited_states:
                return False
            visited_states.add(curr_state)
            for symbol in self.alphabet:
                next_states = set()
                for state, trans_symbol in self.transitions.keys():
                    if state == curr_state and trans_symbol == symbol:
                        next_states.add(self.transitions[(state, trans_symbol)])
                if len(next_states) != 1:
                    return False
                queue.extend(next_states)
        return True

    def convert_to_dfa(self):
        """
        Converts an NDFA to a DFA
        """
        # Set of states in the DFA
        dfa_states = set()
        # Dictionary representing the transition function of the DFA
        dfa_transitions = {}
        # Start state of the DFA
        dfa_start_state = frozenset([self.start_state])
        # Set of accept states in the DFA
        dfa_accept_states = set()
        # Queue for storing states to be processed
        queue = [dfa_start_state]

        # Loop through states in the queue
        while queue:
            # Get the next state from the queue
            state = queue.pop(0)
            # Add the state to the set of DFA states
            dfa_states.add(state)
            # Check if the state contains an accept state from the NDFA
            if any(s in self.accept_states for s in state):
                dfa_accept_states.add(state)
            # Loop through each symbol in the alphabet
            for symbol in self.alphabet:
                # Get the set of states reachable from the current state with the current symbol
                next_state = set()
                for s in state:
                    if (s, symbol) in self.transitions:
                        next_state.update(self.transitions[(s, symbol)])
                # If the set of states is not empty
                if next_state:
                    # Convert the set of states to a single state name
                    next_state_name = frozenset(next_state)
                    # Add the transition to the DFA transition function
                    dfa_transitions[(state, symbol)] = next_state_name
                    # If the next state has not been processed, add it to the queue
                    if next_state_name not in dfa_states:
                        queue.append(next_state_name)

        # Create a new DFA object with the computed properties
        dfa = FiniteAutomaton(states=dfa_states, alphabet=self.alphabet,
                              transitions=dfa_transitions, start_state=dfa_start_state,
                              accept_states=dfa_accept_states)
        return dfa


    def render(self):
        # Create a directed graph using networkx
        G = nx.DiGraph()

        # Add nodes to the graph
        for state in self.states:
            G.add_node(state, shape='circle')
        G.nodes[self.start_state]['shape'] = 'doublecircle'
        for state in self.accept_states:
            G.nodes[state]['peripheries'] = 2

        # Add edges to the graph
        for (from_state, symbol), to_states in self.transitions.items():
            for to_state in to_states:
                G.add_edge(from_state, to_state, label=symbol)

        # Set up positions for the nodes using networkx spring_layout
        pos = nx.spring_layout(G, seed=42)

        # Draw the graph using matplotlib
        nx.draw_networkx_nodes(G, pos, node_size=1000, alpha=0.8)
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.8)
        nx.draw_networkx_labels(G, pos, font_size=18, font_family='sans-serif')
        edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=18, font_family='sans-serif')
        plt.axis('off')
        plt.show()




    def __str__(self):
        s = "Finite Automaton:\n"
        s += "States: " + str(self.states) + "\n"
        s += "Alphabet: " + str(self.alphabet) + "\n"
        s += "Transitions:\n"
        for transition in self.transitions:
            s += str(transition[0]) + " --" + str(transition[1]) + "--> " + str(self.transitions[transition]) + "\n"
        s += "Start state: " + str(self.start_state) + "\n"
        s += "Accept states: " + str(self.accept_states) + "\n"
        return s
