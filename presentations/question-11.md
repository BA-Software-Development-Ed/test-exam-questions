<!-- slide -->

## Question 11
### Elaborate on dependencies in software, and how it’s related to the subject of test.

<!-- slide -->

## Dependencies between layers

<!-- slide --->

## System resources
System Clock, Network & File IO

<!-- slide --->

## Relations between objects

<!-- slide --->

## Dependency inversion, Inversion of Control, Dependency Injection

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

<!-- slide --->

## The Project