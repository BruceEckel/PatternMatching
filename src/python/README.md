Polymorphism Unbound

Polymorphism means a function parameter can accept more than one type. If you
only understand inheritance polymorphism, this more general view of polymorphism
can be confusing. This presentation expands your understanding of polymorphism
and programming in general, enabling you to create better designs. We will look
at inheritance polymorphism, duck typing, and Python 3.10 pattern matching with
type unions and sealed classes.

---

If a function accepts more than one type for a parameter, there are two questions: What types can be accepted, and what can you do with those types?

The concepts are demonstrated using one example implemented in four different
ways:

1. Classic inheritance polymorphism. Shows how `self` is different for each
subclass. Inheritance constrains `self` to be a subtype, and also determines
what member functions can be called via the Liskov Substitution Principle.

2. Duck typing. A valid type is based on what you do with it inside the
function. You never find out if an argument is a valid type until you execute
the code.

3. Using Python 3.10 Union Types and pattern matching. The type hint can specify
multiple disjoint types for the parameter.

4. Using Python 3.10 pattern matching with sealed classes. Enforcing proper type
usage ensures that a pattern match can be exhaustive over all possible types.

All concepts and terms will be explained during the presentation.

Examples are at:
https://github.com/BruceEckel/PatternMatching/src/python


# Audience:

1. Advanced beginner to Intermediate level Python programmers.

2. Some exposure to polymorphism, but don't necessarily have a clear understanding of it.

3. Attendees will gain a deeper understanding of polymorphism, the value of type systems, and the reasons for the Python 3.10 features of type unions, pattern matching and sealed classes.

# Outline

I. Short introduction:

1. My own discovery of polymorphism while dissecting C++ and discovering virtual functions.

2. Teaching polymorphism through the lens of inheritance. Recent years, starting
to wonder what polymorphism *really* means.

3. Seeing polymorphism in functional programming, realizing it means that
function parameters take different types, overhauling my perspective.

II. The remainder of the presentation is an exploration of the examples in
https://github.com/BruceEckel/PatternMatching/tree/master/src/python

1. Classic Inheritance Polymorphism (Inheritance.py). Uses an abstract base
class. Also introduces data classes with the frozen option.

2. Duck Typing (DuckTyping.py). Disjoint classes (no common base class)
containing a common operation. Type can only be validated at runtime.

3. Pattern Matching (PatternMatch.py). Disjoint classes passed as a type union.
Simple use of pattern match on type. Note that the actions formerly inside the
overridden methods have moved inside the pattern match.
Also introduces `case _:`.

4.Pattern Matching with Sealed Classes (PatternMatchSealed.py). Using sealed
classes to automatically produce an exhaustive type union argument for a
complete pattern match.

5. If there's time, mention problems with type checkers for Python (primarily,
lack of support for new versions of Python).

If desired, this presentation can instead be placed in a 45-minute time slot.

# Category: Python Language and Features

# Past Experience:

I've been writing books, articles, and given hundreds of presentations and
seminars throughout the world for over 30 years. I have a focus on languages and
have been working with Python since the mid-90's. I've given closing keynotes at
two Pycons (see https://www.linuxjournal.com/article/4731 and
http://ftp.ntua.gr/mirror/python/pycon/dc2004/), as well as a couple of Pycon
talks over the years. I've attended most Pycons since the late 90s. I've also
given keynotes at international Pycons, for example
https://ep2009.europython.eu/.

See https://www.mindviewllc.com/about/#biography

I've studied and written about pattern matching in Scala, Kotlin and Java. I'm
currently coauthoring a book on functional programming.

I've created a programming podcast with my friend James Ward for the past year: https://www.happypathprogramming.com/

Some Presentations:

https://www.youtube.com/watch?v=U_tEIcP6zEo&ab_channel=NextDayVideo

https://www.youtube.com/watch?v=3OTMR-H2IUI&ab_channel=GiuseppeRomagnoli

https://www.youtube.com/watch?v=d25z-wO1zzs&ab_channel=jetconf

https://www.youtube.com/watch?v=y901lgIuRx0&ab_channel=VMwareTanzu

https://www.youtube.com/watch?v=vWsWoAUjjck&list=PLv24vSVeA7jCV2CMyGHxhy5jQzuKp4_xW&ab_channel=FunctionalTV

https://www.youtube.com/watch?v=6DYLJGwrTo0&ab_channel=VuWall
