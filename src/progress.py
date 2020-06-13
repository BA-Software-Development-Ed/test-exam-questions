with open('table-of-content.md') as file:
    incomplete_objectives = 0
    complete_objectives = 0

    for line in file:
        if '- [ ] [ ' in line:
            incomplete_objectives += 1

        if '- [x] [ ' in line:
            complete_objectives += 1

print('acquired objectives', complete_objectives, '/', complete_objectives + incomplete_objectives)
