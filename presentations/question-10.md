<!-- slide -->
## Question 10
### Characterize high quality software. 
### Explain how writing tests can increase code quality.

<!-- slide -->

## Defensive programming
Assert Positive and Negative Scenarios
Handle Exceptions

<!-- slide --->

## Black-box development

<!-- slide --->

## Interfaces, contracts
|||
|---|---|
|Interface| Class Rules |
|Contract| System Rules |

<!-- slide --->

## Inversion of control

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

## Components

<!-- slide --->

## The Project