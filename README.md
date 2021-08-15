# DefferedGraphTheory 2021
# G00371316

# 1.	Explain the difference between regular expressions in infix notation and those in postfix notation.

# 2.	Explain how Thompson's construction for regular expressions works.
Thompson’s constructor, also known as McNaughton-Yamada is an algorithm which takes regular expressions and transforms them into an equivalent NFA (nondeterministic finite automaton) or an epsilon NFA.  This will then by recognised by the computer as patterns of text, this algorithm was invented by Ken Thompson in the 1960s. 
I will clarify what regular expressions and NFAs are, first of all, they are both formal languages.  And this algorithm will assist NFA’s to recognise the same language as the regular expression it is compared with.  Regular expressions are used to represented certain sets of strings in an algebraic way, NFAs are used for execution purposes in computing, especially when using regular expressions.
There are three basics concepts for operators and regular expressions which you need to know to understand Thompson’s constructor.  The basic operators are “.”, “|” and “*”.  I will give examples of these now.
•	“.” means concatenate, “a.b” means “a” followed by “b”.  
•	“|” means or, “a|b” means “a” or “b”.  
•	“*” means zero or more times, “a*” means zero or more “a’s”
When adding states, there will always be one state called initial and the other state is called final.  Nothing points at the start state except for the initial arrow, the basics you need to know for Thompson’s constructor is the transition, where you start, and the accept states, which is always a single accept state. Here are a few examples of turning a regular expression into an NFA. 
 
This is the Kleene star/ closure, this means 0 or more.  “q” is the initial state and “f” is the final state for all these diagrams.  This set will be {Ε, s, ss, sss ….} as it can be empty or have repetition.
 
This is the union state “|”, the expression used is “s|t”.  As you can see “s” goes one way and “t” goes another because this means “s” or “t” which then reaches its final state once either of these are found.
 
The concatenation state “.”.  “s.t” means “s” beside “t” so the final state cannot be reached without “s” and “t” being beside one another.

 
From this example you can see that this is the NFA for the regular expression (a|b)* abb using the Thompson constructor algorithm, all previous examples also used the same algorithm.  To find out if its correct, you would match this piece of text (Regular Expression) to the pattern that is shown and as seen in the diagram it does.  This shows the pattern matching which we are trying to prove.

# 3.	Explain what is meant by the term irregular language in the context of regular expressions.

