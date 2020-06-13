<!-- slide -->

## Question 3

---
Explain what kinds of test can be 
carried out without running any code.

---
Explain how it can be used
on non-code documents as well.

<!-- slide -->

## Manual Code Review
![code review](../assets/code-review.png)

<!-- slide -->

## Cyclomatic Complexity
```java
foo() {
    if (condition) {                    // CC 1

        if (condition) {                // CC 2
            // code here...
        }

        while (condition) {             // CC 3

            if (condition) {            // CC 4
                // code here...
            } else {                    // CC 5
                // code here...
            }

        }  
    }
}
```

<!-- slide -->

## Reviews
![reviews](../assets/reviews.png)

<!-- slide -->

## Informal Review
"Hey dude - can you check my code? 👻"

* source code

<!-- slide -->

## Walk-Through
A meeting with creator as host.

* source code

<!-- slide -->

## Technical reviews
Technical decisions is made.

* Source Code
* Use Cases
* ReadMe
* API Documentation
* Design Documentation

<!-- slide -->

## Management reviews
Management decisions is made.

* Schedule
* Overall Process

<!-- slide -->

## Inspection
Product improvement is made.

* Software Requirements Specifications
* Software Test Documentation
* Software User Documentation
* Installation Procedures

<!-- slide -->

## Audit
Performed by external specialists. 

e.g. GDPR data audit

<!-- slide -->

## Static analysis
|||
|---|---|
| StyleCop | Coding standards |
| FindBugs | Bugs & potential bugs |
| PMD | Warns Against bad practice |

<!-- slide -->

## The Project