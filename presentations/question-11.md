<!-- slide -->

## Question 11

---
Elaborate on dependencies in software,
and how it’s related to the subject of test.

<!-- slide -->

## Dependencies between layers
Avoid layered dependencies - Use Facades
... or Dependency Injection

<!-- slide --->

## System resources
System Clock, Network & File IO

<!-- slide --->

## Relations between objects
Higher relation between objects reduce testability, refactoring & maintainability

<!-- slide --->

## Dependency inversion
![dependency inversion](../assets/dependency-inversion.png)


<!-- slide --->

## Dependency injection
Problem
```java
foo(String name, int age) {
    User user = new User(name, age);
    // code here ...
}
```

Solution
```java
foo(IUser user) {
    // code here...
}
```
```java
IUser user = new User(name, age);
foo(user);
```

<!-- slide --->

## Mocks

|||
|---|---|
| **Dummy** | Doesn't know anything |
| **Stub** | Knows what you told it |
| **Spy** | Stub with features |
| **Mock** | Expects a lot |
| **Fake** | You cant tell the difference |

<!-- slide --->

## The Project