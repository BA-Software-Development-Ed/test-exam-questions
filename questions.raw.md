---
export_on_save:
  markdown: true
markdown:
  path: README.md
  ignore_from_front_matter: true
---

# Questions | Test Exam 2020
By **Stephan Djurhuus**  
Institute **CPHBusiness**  
Education **Software Development**  


```python {cmd="python" hide=true}
with open('questions.raw.md') as file:
    incomplete_objectives = 0
    complete_objectives = 0

    for line in file:
        if '[ ]' in line:
            incomplete_objectives += 1
            
        if '[x]' in line:
            complete_objectives += 1

print('acquired objectives', complete_objectives - 1, '/', complete_objectives + incomplete_objectives - 15)
```

##  Content Progress / [_edit_](table-of-content.md)
@import "table-of-content.md"

## 1.
**We have looked at some static analysis tools like StyleCop, PMD, FindBugs and SonarLint. Explain how static analysis can improve code quality. Explain how it helped you or could have helped you in your project.**

### 1.1 StyleCop, PMD, FindBugs

**StyleCop**  
This tool is a static source analyser for `C#` code made by Microsoft. It validates the code and checks if it complies the rules given by StyleCop. These rules are based on Microsoft's coding standards but can be modified or extended. 

The rules are classified into theses categories - Documentation, Layout, Maintainability, Naming, Ordering, Readability and Spacing.

[source, wikipedia.org](https://en.wikipedia.org/wiki/StyleCop)

**PMD**  
This is also a source analyser that finds common programming flaws like unused variables, empty catch blocks, unnecessary object creation etc. It support multiple languages.

[source, github.io](https://pmd.github.io/#about)

**FindBugs**  
This is a static analyser tool that looks for bugs in Java.

[source, sourceforge.net](http://findbugs.sourceforge.net/)

### 1.2 Linters, SonarLint

**Linters**  
A Linter is a tool that static analyses the source code and flags programming errors like bugs, stylish errors and suspicious constructs. To avoid replacing tabs with spaces, creating incorrect indentations and inconsistent line breaks, a linter can set the rules for how the source should be structured. 

**Static Analysis**  
Static Analysis means that automated software runs through your code source without executing it. It statically checks for potential bugs, memory leaks, and any other check that may be useful.

[source, sourcelevel.io](https://sourcelevel.io/blog/what-is-a-linter-and-why-your-team-should-use-it)

**SonarLint**  
SonarLint is an IDE extension that helps you detect and fix quality issues as you write code.
Like a spell checker, SonarLint squiggles flaws so that they can be fixed before committing code.

Works with Eclipse, InteliJ IDEA, Visual Studio and VS Code.

It constrains features as Instant View where you can see se an explanation, description and time of the issue. Its validates while your are typing and gives you instant messages if an issue has occurred. It has push notifications that tells you about the source status. 

[source, sonarlint.org](https://www.sonarlint.org/)
[source, sonarsource.com](https://www.sonarsource.com/products/sonarlint/)

### 1.3 Security

Static application security testing (SAST) is a static analyzing tool for locating security vulnerabilities. 

These tools can scan millions of lines of code in a matter of minutes. SAST tools automatically identify critical vulnerabilities—such as buffer overflows, SQL injection, cross-site scripting, and others—with high confidence.

[source, synopsys.com](https://www.synopsys.com/glossary/what-is-sast.html)


## 2.
**Explain test levels, and what characterizes the individual levels. Then, relate to your own project.**

### 2.1 Unit testing

...
[source not implemented]()

### 2.2 Integration testing

...
[source not implemented]()

### 2.3 System testing

...
[source not implemented]()

### 2.4 Load testing

...
[source not implemented]()

### 2.5 Static testing

...
[source not implemented]()

### 2.6 Acceptance testing

...
[source not implemented]()

## 3.
**Explain what kinds of test can be carried out without running any code. Explain how it can be used on non-code documents as well.**

### 3.1 Reviews

...
[source not implemented]()

### 3.2 Technical reviews

...
[source not implemented]()

### 3.3 Management reviews

...
[source not implemented]()

### 3.4 Audit

...
[source not implemented]()

### 3.5 Static analysis

**Static Analysis**  
Static Analysis means that automated software runs through your code source without executing it. It statically checks for potential bugs, memory leaks, and any other check that may be useful.

...

[source](https://sourcelevel.io/blog/what-is-a-linter-and-why-your-team-should-use-it)
...
[source not implemented]()

### 3.6 Linters

...
[source not implemented]()

## 4.
**Explain test activities, and how they are related to each other. Then explain the test activities you carried out in your project.**

### 4.1 Unit testing

...
[source not implemented]()

### 4.2 Integration testing

...
[source not implemented]()

### 4.3 Refactoring

...
[source not implemented]()

### 4.4 Maintenance

...
[source not implemented]()

### 4.5 Continuous Integration

...
[source not implemented]()

### 4.6 Code reviews

...
[source not implemented]()

## 5.
**Testing is related to ensuring higher code quality. Elaborate on what characterizes high code quality, and what makes code testable.**

### 5.1 Testable code

...
[source not implemented]()

### 5.2 Names of tests**

...
[source not implemented]()

### 5.3 “sufficient” tests of a method or class**

...
[source not implemented]()

### 5.4 Assertions, defensive programming**

...
[source not implemented]()

### 5.5 Dependency injection**

...
[source not implemented]()

## 6.
**Explain the concept of maintainable code, and how it’s related to test. Explain how to find out if a code base is maintainable.**

### 6.1 Maintainability

...

[source not implemented]()

### 6.2 Product quality

...

[source not implemented]()

### 6.3 Temporal coupling

...

[source not implemented]()

### 6.4 Continuous Integration

...

[source not implemented]()

### 6.5 Static Analysis

...

[source not implemented]()

### 6.6 Dependency injection, inversion of control

...

[source not implemented]()

### 6.7 Low coupling, high cohesion

...

[source not implemented]()

### 6.8  Cyclomatic code complexity

...

[source not implemented]()


## 7.
**Explain unit testing, and what characterizes it in contrast to other types of test.**

### 7.1 What and why

...

[source not implemented]()

### 7.2 Unit Under Test System Under Test

...

[source not implemented]()

### 7.3 Unit test lifecycle(BeforeAll, AfterAll _ SetUp, TearDown)_

...

[source not implemented]()

### 7.4 Test doubles (mock, fake, stub, spy)

...

[source not implemented]()

### 7.5 Matchers(Hamcrest)

...

[source not implemented]()

### 7.6 Test Driven Development

...

[source not implemented]()

### 7.7 Dependency Injection

...

[source not implemented]()

### 7.8 Equivalence classes, boundary value analysis, equivalence partitions

...

[source not implemented]()


## 8.
**Explain test driven development, and how it affects the development process and code quality.**

### 8.1 Red, Green, Refactor

...

[source not implemented]()

### 8.2 Testable code

...

[source not implemented]()

### 8.3 Maintainable code

...

[source not implemented]()

### 8.4 Equivalence partitions

...

[source not implemented]()

### 8.5 Positive, negative tests

...

[source not implemented]()


## 9.
**Explain about test doubles. Explain how and why mocking is useful, and in what test areas.**

### 9.1 JMock, mocks, spies, stubs, fakes, dummies

...

[source not implemented]()

### 9.2 Dependency injection

...

[source not implemented]()

### 9.3 Interfaces, contracts

...

[source not implemented]()

### 9.4 Black-box vs white-box

...

[source not implemented]()


## 10.
**Characterize high quality software. Explain how writing tests can increase code quality.**

### 10.1 Defensive programming

...

[source not implemented]()

### 10.2 Black-box development

...

[source not implemented]()

### 10.3 Interfaces, contracts

...

[source not implemented]()

### 10.4 Inversion of control

...

[source not implemented]()

### 10.5 Dependency injection

...

[source not implemented]()

### 10.6 Components

...

[source not implemented]()


## 11.
**Elaborate on dependencies in software, and how it’s related to the subject of test.**

### 11.1 Dependencies between layers

...

[source not implemented]()

### 11.2 System resources

...

[source not implemented]()

### 11.3 Relations between objects

...

[source not implemented]()

### 11.4 Dependency inversion, Inversion of Control, Dependency Injection

...

[source not implemented]()

### 11.5 Mocks

...

[source not implemented]()


## 12.
**Explain problems in test automation, and how a continuous integration tool can help.**

### 12.1 What is Continuous Integration?

...

[source not implemented]()

### 12.2 How can a CI help regarding tests?

...

[source not implemented]()

### 12.3 What is a regression?

...

[source not implemented]()

### 12.4 What test levels can be covered by a CI system?

...

[source not implemented]()


## 13.
**Explain specification-based testing, and how you can be more confident that you have written a sufficient amount of tests.**

### 13.1 Equivalence partitioning

...

[source not implemented]()

### 13.2 Boundary value analysis

...

[source not implemented]()

### 13.3 Edge cases

...

[source not implemented]()

### 13.4 Decision tables

...

[source not implemented]()

### 13.5 Code coverage

...

[source not implemented]()