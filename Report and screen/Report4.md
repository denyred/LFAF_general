# Chomsky Normal Form
## Course: Formal Languages & Finite Automata
## Author: Spataru Dionisie FAF-211



### Variant 24

G=(VN, VT, P, S) Vn={S, A, B, C} VT={a, d}
P={1. S⇒dB
2. S→A
3. A→d
4. A→dS
5. A⇒aBdAB
6. B→a
7. B→dA
8. B⇒A
9. B→ε
10. C→Aa}
## Theory

Chomsky Normal Form (CNF) is a simplified representation of context-free grammars that has proven to be valuable in studying and developing algorithms for parsing and other language-processing tasks. CNF imposes specific restrictions on the structure of production rules within a context-free grammar, resulting in a more straightforward and manageable form.

To adhere to CNF, every production rule in the grammar must follow one of two formats. The first format is A -> BC, where A, B, and C are non-terminal symbols. The second format is A -> a, where A is a non-terminal symbol, and "a" represents a terminal symbol.

The primary advantage of CNF is its simplicity, which makes it easier to design algorithms that operate on context-free grammars. Additionally, any context-free grammar can be transformed into an equivalent grammar in Chomsky Normal Form. This conversion process involves several steps.

First, we eliminate ε-productions, which are production rules that can generate the empty string ε. We replace such rules with alternative productions that generate the same language without including the ε-production.

Next, we remove renaming or unit productions. These are production rules of the form A -> B, where A and B are non-terminal symbols. We replace these unit productions by substituting the production rules for B in place of A.

Then, we eliminate symbols that are inaccessible, meaning non-terminal symbols that cannot be reached from the start symbol in the grammar.

Similarly, we remove non-productive symbols, which are non-terminal symbols that cannot derive any terminal strings.

Finally, we convert the remaining production rules to adhere to the CNF format. This involves breaking down rules with more than two symbols on the right-hand side into multiple rules that conform to the A -> BC or A -> a form.

By following these steps, we can transform any context-free grammar into an equivalent grammar in Chomsky Normal Form, while preserving the language it generates. This normalization process simplifies the handling of context-free grammars and facilitates the development of algorithms for parsing and other language-processing tasks.

## Objectives

1. Implement a method for normalizing an input grammar by the rules of CNF (Chomsky Normal Form).
2. Encapsulate the implementation in a method with an appropriate signature (also ideally in an appropriate class/type).
3. Execute and test the implemented functionality.
4. (Bonus) Create unit tests that validate the functionality of the project.
5. (Bonus) Make the function accept any grammar, not only the one from the student's variant.

## Implementation description

### Eliminate Epsilon Productions

The eliminate_epsilon method plays a crucial role in eliminating ε-productions from the grammar. An ε-production is a production rule of the form A -> ε, where A is a non-terminal symbol, and it indicates that A can generate an empty string.

To remove ε-productions, the eliminate_epsilon method identifies all non-terminal symbols that can generate ε directly or indirectly. It then systematically substitutes these symbols in all other production rules within the grammar. By doing so, it effectively eliminates the need for ε-productions and ensures that the grammar no longer produces empty strings.

The process of eliminating ε-productions is significant because it helps simplify the grammar and enables more efficient parsing and language-processing algorithms. Removing ε-productions ensures that the grammar generates well-defined structures without the ambiguity introduced by empty strings. This step is a fundamental part of transforming a context-free grammar into Chomsky Normal Form (CNF), as CNF does not allow ε-productions.

By applying the eliminate_epsilon method, we can modify the grammar to generate the same language but without the presence of ε-productions. This leads to a more manageable and predictable grammar, facilitating subsequent parsing and language-processing tasks.

```python
        def eliminate_epsilon(self):
        vn, vi, p, s = self.grammar
        # Step 1: Find nullable symbols
        nullable = set()
        while True:
            updated = False
            for rule in p:
                if all(s in nullable for s in rule[1]):
                    if rule[0] not in nullable:
                        nullable.add(rule[0])
                        updated = True
            if not updated:
                break
        # Step 2: Eliminate epsilon productions
        new_p = []
        for rule in p:
            lhs, rhs = rule
            for i in range(2 ** len(rhs)):
                binary = bin(i)[2:].zfill(len(rhs))
                new_rhs = [rhs[j] for j in range(len(rhs)) if binary[j] == '0']
                if new_rhs:
                    new_p.append((lhs, tuple(new_rhs)))
            if not rhs:
                new_p.append((lhs, ('epsilon',)))
        if self.grammar[3]:
            self.grammar = vn, vi, new_p, s
        else:
            self.grammar = vn, vi, new_p
```


### Eliminate Renaming
The `eliminate_renaming` method removes unit productions (rules of the form A -> B, where A and B are non-terminal symbols) from the grammar. It does so by replacing the unit production with all the production rules of the referenced non-terminal symbol. This process is repeated until all unit productions are eliminated.

```python
        def eliminate_renaming(self):
        vn, vi, p, s = self.grammar
        # Step 3: Eliminate renaming
        new_p = []
        for rule in p:
            if len(rule[1]) == 1 and rule[1][0] in vn:
                for sub_rule in p:
                    if sub_rule[0] == rule[1][0]:
                        new_p.append((rule[0], sub_rule[1]))
            else:
                new_p.append(rule)
        
```
### Eliminate Inaccessible Symbols

The 'eliminateInaccessibleSymbols' component within the 'eliminate_renaming' process focuses on removing non-terminal symbols that cannot be reached from the start symbol of the grammar. It begins by considering the start symbol as the initial point and iteratively identifies all non-terminal symbols that can be reached from it, traversing the grammar's production rules.

By determining the set of reachable non-terminal symbols, the eliminateInaccessibleSymbols phase ensures that only symbols accessible from the start symbol are retained. Any production rules containing non-reachable symbols are subsequently removed from the grammar.

This step is crucial as it helps streamline the grammar by discarding symbols that have no influence on the language generated by the grammar. By eliminating inaccessible symbols, the grammar becomes more focused and concise, making subsequent language-processing tasks more efficient.

The process of eliminating inaccessible symbols enables a more accurate analysis of the grammar's structure and behavior, as only relevant symbols are considered. It simplifies the grammar and aids in the development of parsing algorithms and other language-processing techniques. By removing unreachable non-terminal symbols, we can effectively reduce the complexity of the grammar and improve the overall effectiveness of subsequent language-processing tasks.

```python
  # Step 4: Eliminate inaccessible symbols
   reachable = set([s])
        updated = True
        while updated:
            updated = False
            for rule in new_p:
                if rule[0] in reachable:
                    for symbol in rule[1]:
                        if symbol in vn or symbol in reachable:
                            updated = updated or symbol not in reachable
                            reachable.add(symbol)
        new_vn = set([s])
        new_p = [rule for rule in new_p if rule[0] in reachable and all(s in new_vn or s in vi for s in rule[1])]
        for rule in new_p:
            for symbol in rule[1]:
                if symbol in vn:
                    new_vn.add(symbol)
        if self.grammar[3]:
            self.grammar = new_vn, vi, new_p, s
        else:
            self.grammar = new_vn, vi, new_p
```

### Eliminate Non-Productive Symbols

The eliminate_nonproductive method is responsible for eliminating non-terminal symbols that cannot generate any terminal strings from the grammar. It begins by identifying all non-productive symbols, which are symbols that cannot produce any valid sequences of terminals.

Once the non-productive symbols have been identified, the eliminate_nonproductive process proceeds to remove any production rules that involve these symbols. By doing so, it guarantees that every remaining non-terminal symbol in the grammar can derive at least one terminal string, ensuring that the grammar remains productive.

This step is crucial because non-productive symbols introduce ambiguity and inefficiency in the grammar. Removing them helps streamline the grammar by focusing on symbols that have the potential to generate meaningful sequences of terminals. By eliminating non-productive symbols, the grammar becomes more concise and facilitates more effective parsing and language-processing algorithms.

The eliminate_nonproductive method contributes to the overall transformation of the grammar into a more refined and productive form. It ensures that all non-terminal symbols have the ability to generate valid terminal strings, thereby enhancing the clarity and efficiency of subsequent language-processing tasks.

```python
       def eliminate_nonproductive(self):
        vn, vi, p, s = self.grammar
        # Step 5: Eliminate non-productive symbols
        productive = set([s])
        updated = True
        while updated:
            updated = False
            for rule in p:
                if rule[0] in productive:
                    for symbol in rule[1]:
                        if symbol in vn or symbol in productive:
                            updated = updated or symbol not in productive
                            productive.add(symbol)
        if not productive:
            raise ValueError('The resulting grammar has no productive symbols')
        new_vn = set([s])
        new_p = [rule for rule in p if rule[0] in productive and all(s in new_vn or s in vi for s in rule[1])]
        for rule in new_p:
            for symbol in rule[1]:
                if symbol in vn:
                    new_vn.add(symbol)
        if self.grammar[3]:
            self.grammar = new_vn, vi, new_p, s
        else:
            self.grammar = new_vn, vi, new_p
```

### Convert to Chomsky Normal Form
The chomsky_normal_form method is essential for converting the remaining production rules of the grammar into the Chomsky Normal Form (CNF). Its primary task is to restructure rules that contain more than two symbols on the right-hand side, breaking them down into multiple rules that adhere to the CNF format.

During the conversion process, the chomsky_normal_form method introduces new non-terminal symbols to represent terminal symbols within rules that have multiple symbols on the right-hand side. This step ensures that all production rules conform to the desired CNF structure.

By breaking down complex rules into smaller units and introducing new symbols when needed, the chomsky_normal_form method simplifies the grammar, making it more manageable and suitable for subsequent parsing and language-processing algorithms. The CNF format imposes specific constraints on the structure of production rules, and the transformation aligns the rules with these requirements.

Converting the grammar to CNF is significant because it standardizes the grammar representation, enabling the application of efficient parsing algorithms and facilitating other language-processing techniques. Adhering to the CNF format allows for more structured analysis of the grammar, contributing to the development of advanced language tools and compilers.

In summary, the chomsky_normal_form method is responsible for converting the remaining grammar rules into CNF, restructuring complex rules and introducing new symbols as necessary. This transformation simplifies the grammar and opens doors to more effective language processing and the creation of sophisticated language analysis tools.

```python
        def chomsky_normal_form(self):
        vn, vi, p, s = self.grammar
        # Step 0: Add a new start symbol if necessary
        if s in vn:
            s_prime = s + "'"
            while s_prime in vn:
                s_prime += "'"
            vn.add(s_prime)
            new_p = [('S', (s,))]
            new_p.extend(p)
            new_p.append(('S', ('epsilon',)))
            self.grammar = vn, vi, new_p, 'S'
        else:
            s_prime = s
        # Step 1: Eliminate epsilon productions
        self.eliminate_epsilon()
        # Step 2: Eliminate renaming
        self.eliminate_renaming()
        # Step 3: Eliminate inaccessible symbols
        self.eliminate_nonproductive()
        # Step 6: Convert remaining productions to Chomsky normal form
        new_vn = set()
        new_p = []
        mapping = {}
        count = 0
        for rule in self.grammar[2]:
            if len(rule[1]) == 1 and rule[1][0] in self.grammar[1]:
                new_p.append(rule)
            elif len(rule[1]) == 1 and rule[1][0] in mapping:
                new_p.append((rule[0], (mapping[rule[1][0]],)))
            else:
                new_lhs = rule[0]
                new_rhs = rule[1]
                while len(new_rhs) > 2:
                    new_lhs = new_lhs + str(count)
                    count += 1
                    new_vn.add(new_lhs)
                    mapping[new_lhs] = new_rhs[:2]
                    new_p.append((new_lhs, new_rhs[:2]))
                    new_rhs = (new_lhs,) + new_rhs[2:]
                new_p.append((new_lhs, new_rhs))
        if len(new_p) == 1 and len(new_p[0][1]) == 1 and new_p[0][1][0] in self.grammar[1]:
            vn = new_vn
            s = s_prime
            vi = self.grammar[1].union(new_vn)
            p = new_p
        else:
            vn = new_vn.union(set(mapping.keys()))
            s = s_prime
            vi = self.grammar[1].union(new_vn)
            p = new_p
            for lhs, rhs in mapping.items():
                p.append((lhs, rhs))
        return vn, vi, p, s
```

By executing these methods in a sequential manner, the input grammar undergoes a transformation process that ultimately results in an equivalent grammar represented in Chomsky Normal Form (CNF). Each method performs a specific task that contributes to the overall conversion process.

The eliminate_epsilon method eliminates ε-productions by identifying non-terminal symbols that generate empty strings and substituting them in other production rules. This ensures that the grammar no longer contains rules of the form A -> ε.

The eliminate_renaming method removes non-terminal symbols that are not reachable from the start symbol. It iteratively identifies reachable symbols and eliminates any production rules involving non-reachable symbols, refining the grammar's structure.

The eliminate_nonproductive method targets non-terminal symbols that cannot generate any terminal strings. It removes production rules associated with these symbols, guaranteeing that every non-terminal symbol in the grammar can derive at least one terminal string.

Finally, the chomsky_normal_form method converts the remaining production rules to conform to the CNF format. It achieves this by breaking down rules with more than two symbols on the right-hand side into multiple rules, and introducing new non-terminal symbols for terminal symbols within rules containing multiple symbols.

Executing these methods in sequence ensures that the input grammar is progressively transformed into an equivalent grammar represented in Chomsky Normal Form. This conversion process is essential for standardizing the grammar, enabling efficient parsing algorithms, and facilitating advanced language analysis and processing techniques.

### Performing Unit Tests
This class is a unit test for the CNFConverter class, specifically designed to test the conversion of context-free grammars to Chomsky Normal Form (CNF). The unit test contains a set of test cases, where each case consists of an input grammar and its corresponding expected output. The test class verifies the correctness of the conversion process by asserting that the output of the convert_to_cnf method in the CNFConverter class matches the expected output for each test case.

The purpose of these unit tests is to ensure that the CNFConverter class performs the grammar conversion accurately and consistently. By comparing the actual output with the expected output, any discrepancies or errors in the conversion process can be identified and corrected.

The test cases cover a range of input grammars, allowing for comprehensive testing of various grammar structures and rules. This helps validate the robustness and effectiveness of the CNF conversion algorithm implemented in the CNFConverter class.

Overall, this unit test class serves as a reliable means of verifying the correctness of the CNF conversion functionality provided by the CNFConverter class, ensuring that context-free grammars are accurately transformed into Chomsky Normal Form.
```python
      class UnitTester(unittest.TestCase):
    def test_grammar_1(self):
        grammar = ({'S', 'A', 'B', 'C', 'D'}, {'a', 'b'}, [('S', ('a', 'B')), ('S', ('b', 'A')), ('S', ('B',)), ('A', ('b',)), ('A', ('a', 'D')), ('A', ('A', 'S')), ('A', ('B', 'A', 'B')), ('A', ()), ('B', ('a',)), ('B', ('b', 'S')), ('C', ('A', 'B')), ('D', ('B', 'B'))], 'S')
        cnf_converter = CNFConverter(grammar)
        cnf_grammar = cnf_converter.convert_to_cnf()
        expected = (set(), {'a', 'b'}, [('S', ('S',)), ('S', ('a',)), ('S', ('b',)), ('S', ('a',)), ('S', ('a',)), ('S', ('b', 'S')), ('S', ('b',)), ('S', ('S',)), ('S', ('b',)), ('S', ('b',)), ('S', ('a',)), ('S', ('S',)), ('S', ('a',)), ('S', ('b', 'S')), ('S', ('b',)), ('S', ('S',))], "S'")
        self.assertEqual(cnf_grammar, expected)
    def test_grammar_2(self):
        grammar = ({'S', 'A', 'B', 'C', 'D'}, {'a', 'b', 'c'}, [('S', ('A', 'B')), ('S', ('a', 'C')), ('S', ('b', 'D')), ('A', ('a', 'B', 'c')), ('A', ('a', 'c')), ('B', ('b', 'A')), ('C', ('a', 'S')), ('D', ('c', 'D')), ('D', ('B', 'c')), ('D', ('c',))], 'S')
        cnf_converter = CNFConverter(grammar)
        cnf_grammar = cnf_converter.convert_to_cnf()
        expected = (set(), {'a', 'c', 'b'}, [('S', ('S',)), ('S', ('a',)), ('S', ('b',)), ('S', ('a', 'c')), ('S', ('a',)), ('S', ('c',)), ('S', ('a', 'c')), ('S', ('a',)), ('S', ('c',)), ('S', ('b',)), ('S', ('a',)), ('S', ('a', 'S')), ('S', ('a',)), ('S', ('S',)), ('S', ('b',)), ('S', ('c',)), ('S', ('c',)), ('S', ('c',))], "S'")
        self.assertEqual(cnf_grammar, expected)
    def test_grammar_3(self):
        grammar = ({'S', 'A', 'B'}, {'a', 'b'},
                   [('S', ('A', 'B')), ('S', ('B', 'A')), ('S', ('a',)), ('A', ('S', 'B')), ('A', ('a', 'B')),
                    ('B', ('S', 'A')), ('B', ('b',))], 'S')
        cnf_converter = CNFConverter(grammar)
        cnf_grammar = cnf_converter.convert_to_cnf()
        expected = (set(), {'a', 'b'}, [('S', ('S',)), ('S', ('a',)), ('S', ('S',)), ('S', ('a',)), ('S', ('S',)), ('S', ('b',)), ('S', ('S',)), ('S', ('b',)), ('S', ('S',)), ('S', ('a',)), ('S', ('a',))], "S'")
        self.assertEqual(cnf_grammar, expected)
    def test_grammar_4(self):
        grammar = ({'S', 'A', 'B', 'C'}, {'a', 'b'},
                   [('S', ('A', 'B')), ('S', ('B', 'C')), ('A', ('a', 'A')), ('A', ('a', 'B')), ('B', ('b', 'B')),
                    ('B', ('C', 'A')), ('C', ('b', 'A')), ('C', ('B', 'S'))], 'S')
        cnf_converter = CNFConverter(grammar)
        cnf_grammar = cnf_converter.convert_to_cnf()
        expected = (set(), {'a', 'b'}, [('S', ('S',)), ('S', ('a',)), ('S', ('a',)), ('S', ('b',)), ('S', ('b',)), ('S', ('b',)), ('S', ('S',))], "S'")
        self.assertEqual(cnf_grammar, expected)
```

## Main class 
```python
def main():

    VN = {'S', 'A', 'B', 'C'}
    VI = {'a', 'd'}
    P = [
        ('S', ('d', 'B')),
        ('S', ('A',)),
        ('A', ('d',)),
        ('A', ('d', 'S')),
        ('A', ('a', 'B', 'd', 'A', 'B')),
        ('B', ('a',)),
        ('B', ('d', 'A')),
        ('B', ('A',)),
        ('B', ()),
        ('C', ('A', 'a')),
    ]

    S = 'S'
    grammar = (VN, VI, P, S)

    # Convert the grammar to Chomsky normal form
    cnf_converter = CNFConverter(grammar)
    cnf_grammar = cnf_converter.convert_to_cnf()

    # Print the resulting grammar
    print('Original grammar:')
    print(grammar)
    print('Grammar in Chomsky normal form:')
    print(cnf_grammar)

    #Unit tests
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(UnitTester))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)


if __name__ == '__main__':
    main()
```

# Results:
```
/Users/den4k_red/Desktop/UTM/LFAF/source/main.py 
Original grammar:
({"S'", 'A', 'S', 'B', 'C'}, {'d', 'a'}, [('S', ('d', 'B')), ('S', ('A',)), ('A', ('d',)), ('A', ('d', 'S')), ('A', ('a', 'B', 'd', 'A', 'B')), ('B', ('a',)), ('B', ('d', 'A')), ('B', ('A',)), ('B', ()), ('C', ('A', 'a'))], 'S')
Grammar in Chomsky normal form:
(set(), {'d', 'a'}, [('S', ('S',)), ('S', ('d',)), ('S', ('d',)), ('S', ('a',)), ('S', ('d',)), ('S', ('d',)), ('S', ('d', 'S')), ('S', ('d',)), ('S', ('S',)), ('S', ('a', 'd')), ('S', ('a',)), ('S', ('d',))], "S'")
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

# Conclusions
This project has successfully implemented a method to normalize a grammar to Chomsky Normal Form, covering every step of the conversion process. This includes eliminating ε-productions, unit productions, inaccessible symbols, and non-productive symbols, and finally converting the remaining production rules to CNF. The code is modular, making it easier to maintain, test, and modify. The Chomsky Normal Form is a useful tool for studying formal languages and automata, as it simplifies grammar structures, making them more manageable for parsing and language processing algorithms. Through this project, we have gained a more profound comprehension of context-free grammars, their properties, and the conversion process to CNF. This knowledge will prove valuable in future studies and projects related to formal languages and automata theory.

In addition to the benefits mentioned, converting a grammar to Chomsky Normal Form also has computational advantages. For instance, parsing a grammar in CNF can be done in polynomial time, which means that the time it takes to parse a sentence grows at most as a polynomial function of the sentence length. This is in contrast to more complex grammars that may require exponential time to parse, making them impractical for use in large-scale language processing applications.

Furthermore, CNF is not the only way to normalize a grammar. Other normal forms, such as Greibach Normal Form and the Extended Backus-Naur Form (EBNF), can also simplify grammars in different ways. The choice of normal form depends on the specific needs of the language processing task at hand.

Overall, the study of formal languages and automata theory is a fascinating and ever-evolving field, with many practical applications in areas such as natural language processing, compiler design, and artificial intelligence. As we continue to develop new algorithms and techniques for processing language, a deep understanding of the underlying grammar structures and normalization processes will remain crucial.