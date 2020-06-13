<!-- slide -->
## Question 8
### Explain test driven development, and how it affects the development process and code quality.

<!-- slide -->

## Red, Green, Refactor
![](https://i.imgur.com/TDqCuVd.png)

<!-- slide --->

## Testable code
Low Coupling & High Cohesion

<!-- slide --->

## Maintainable code
* Test Driven Development
* Dependency Injection
* Continuos Integration

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

<!-- slide -->

## Continuous Integration
![](https://i.imgur.com/klQuIlh.png)

<!-- slide --->

## Equivalence partitions
![equivalence partitions](../assets/equivalence-partitions.png)  

<!-- slide --->

## Positive & Negative Tests
Assert Positive and Negative Scenarios
Handle Exceptions

<!-- slide --->

## The Project