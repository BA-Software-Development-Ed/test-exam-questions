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

##  Content Progress
  
- [ ] [1.](#1 )
    - [x] [1.1 StyleCop, PMD, FindBugs](#11-stylecop-pmd-findbugs )
    - [ ] [1.2 Linters, SonarLint](#12-linters-sonarlint )
    - [ ] [1.3 Security](#13-security )
- [ ] [2.](#2 )
    - [ ] [2.1 Unit testing](#21-unit-testing )
    - [ ] [2.2 Integration testing](#22-integration-testing )
    - [ ] [2.3 System testing](#23-system-testing )
    - [ ] [2.4 Load testing](#24-load-testing )
    - [ ] [2.5 Static testing](#25-static-testing )
    - [ ] [2.6 Acceptance testing](#26-acceptance-testing )
- [ ] [3.](#3 )
    - [ ] [3.1 Reviews](#31-reviews )
    - [ ] [3.2 Technical reviews](#32-technical-reviews )
    - [ ] [3.3 Management reviews](#33-management-reviews )
    - [ ] [3.4 Audit](#34-audit )
    - [ ] [3.5 Static analysis](#35-static-analysis )
    - [ ] [3.6 Linters](#36-linters )
- [ ] [4.](#4 )
    - [ ] [4.1 Unit testing](#41-unit-testing )
    - [ ] [4.2 Integration testing](#42-integration-testing )
    - [ ] [4.3 Refactoring](#43-refactoring )
    - [ ] [4.4 Maintenance](#44-maintenance )
    - [ ] [4.5 Continuous Integration](#45-continuous-integration )
    - [ ] [4.6 Code reviews](#46-code-reviews )
- [ ] [5.](#5 )
    - [ ] [5.1 Testable code](#51-testable-code )
    - [ ] [5.2 Names of tests**](#52-names-of-tests )
    - [ ] [5.3 “sufficient” tests of a method or class**](#53-sufficient-tests-of-a-method-or-class )
    - [ ] [5.4 Assertions, defensive programming**](#54-assertions-defensive-programming )
    - [ ] [5.5 Dependency injection**](#55-dependency-injection )
- [ ] [6.](#6 )
    - [ ] [6.1 Maintainability](#61-maintainability )
    - [ ] [6.2 Product quality](#62-product-quality )
    - [ ] [6.3 Temporal coupling](#63-temporal-coupling )
    - [ ] [6.4 Continuous Integration](#64-continuous-integration )
    - [ ] [6.5 Static Analysis](#65-static-analysis )
    - [ ] [6.6 Dependency injection, inversion of control](#66-dependency-injection-inversion-of-control )
    - [ ] [6.7 Low coupling, high cohesion](#67-low-coupling-high-cohesion )
    - [ ] [6.8  Cyclomatic code complexity](#68-cyclomatic-code-complexity )
- [ ] [7.](#7 )
    - [ ] [7.1 What and why](#71-what-and-why )
    - [ ] [7.2 Unit Under Test System Under Test](#72-unit-under-test-system-under-test )
    - [ ] [7.3 Unit test lifecycle(BeforeAll, AfterAll _ SetUp, TearDown)_](#73-unit-test-lifecyclebeforeall-afterall-_-setup-teardown_ )
    - [ ] [7.4 Test doubles (mock, fake, stub, spy)](#74-test-doubles-mock-fake-stub-spy )
    - [ ] [7.5 Matchers(Hamcrest)](#75-matchershamcrest )
    - [ ] [7.6 Test Driven Development](#76-test-driven-development )
    - [ ] [7.7 Dependency Injection](#77-dependency-injection )
    - [ ] [7.8 Equivalence classes, boundary value analysis, equivalence partitions](#78-equivalence-classes-boundary-value-analysis-equivalence-partitions )
- [ ] [8.](#8 )
    - [ ] [8.1 Red, Green, Refactor](#81-red-green-refactor )
    - [ ] [8.2 Testable code](#82-testable-code )
    - [ ] [8.3 Maintainable code](#83-maintainable-code )
    - [ ] [8.4 Equivalence partitions](#84-equivalence-partitions )
    - [ ] [8.5 Positive, negative tests](#85-positive-negative-tests )
- [ ] [9.](#9 )
    - [ ] [9.1 JMock, mocks, spies, stubs, fakes, dummies](#91-jmock-mocks-spies-stubs-fakes-dummies )
    - [ ] [9.2 Dependency injection](#92-dependency-injection )
    - [ ] [9.3 Interfaces, contracts](#93-interfaces-contracts )
    - [ ] [9.4 Black-box vs white-box](#94-black-box-vs-white-box )
- [ ] [10.](#10 )
    - [ ] [10.1 Defensive programming](#101-defensive-programming )
    - [ ] [10.2 Black-box development](#102-black-box-development )
    - [ ] [10.3 Interfaces, contracts](#103-interfaces-contracts )
    - [ ] [10.4 Inversion of control](#104-inversion-of-control )
    - [ ] [10.5 Dependency injection](#105-dependency-injection )
    - [ ] [10.6 Components](#106-components )
- [ ] [11.](#11 )
    - [ ] [11.1 Dependencies between layers](#111-dependencies-between-layers )
    - [ ] [11.2 System resources](#112-system-resources )
    - [ ] [11.3 Relations between objects](#113-relations-between-objects )
    - [ ] [11.4 Dependency inversion, Inversion of Control, Dependency Injection](#114-dependency-inversion-inversion-of-control-dependency-injection )
    - [ ] [11.5 Mocks](#115-mocks )
- [ ] [12.](#12 )
    - [ ] [12.1 What is Continuous Integration?](#121-what-is-continuous-integration )
    - [ ] [12.2 How can a CI help regarding tests?](#122-how-can-a-ci-help-regarding-tests )
    - [ ] [12.3 What is a regression?](#123-what-is-a-regression )
    - [ ] [12.4 What test levels can be covered by a CI system?](#124-what-test-levels-can-be-covered-by-a-ci-system )
- [ ] [13.](#13 )
    - [ ] [13.1 Equivalence partitioning](#131-equivalence-partitioning )
    - [ ] [13.2 Boundary value analysis](#132-boundary-value-analysis )
    - [ ] [13.3 Edge cases](#133-edge-cases )
    - [ ] [13.4 Decision tables](#134-decision-tables )
    - [ ] [13.5 Code coverage](#135-code-coverage )

## 1.
**We have looked at some static analysis tools like StyleCop, PMD, FindBugs and SonarLint. Explain how static analysis can improve code quality. Explain how it helped you or could have helped you in your project.**

### 1.1 StyleCop, PMD, FindBugs

**StyleCop**

This tool is a static source analyser for `C#` code made by Microsoft. It validates the code and checks if it complies the rules given by StyleCop. These rules are based on Microsoft's coding standards but can be modified or extended. 

The rules are classified into theses categories - Documentation, Layout, Maintainability, Naming, Ordering, Readability and Spacing.

[source](https://en.wikipedia.org/wiki/StyleCop)

**PMD**

This is also a source analyser that finds common programming flaws like unused variables, empty catch blocks, unnecessary object creation etc. It support multiple languages.

[source](https://pmd.github.io/#about)

**FindBugs**

This is a static analyser tool that looks for bugs in Java.

[source](http://findbugs.sourceforge.net/)

### 1.2 Linters, SonarLint


**Linters**

A Linter is a tool that static analyses the source code and flags programming errors like bugs, stylish errors and suspicious constructs.


**Static Analysis**  
Static Analysis means that automated software runs through your code source without executing it. It statically checks for potential bugs, memory leaks, and any other check that may be useful.

...

[source](https://sourcelevel.io/blog/what-is-a-linter-and-why-your-team-should-use-it)

**SonarLint**

...

### 1.3 Security

...
[source not implemented]()


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