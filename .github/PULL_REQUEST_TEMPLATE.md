Before open PR be sure that your changes doesn't brake any other code in repository: run playbooks from playbooks/test.
Add your own playbooks for testing your changes.

Check that your code works, please, don't ask review of WIP PRs (we can help you and will review code if you directly ask us about it @ansible-dellemc-unity/experts [experts](https://github.com/orgs/ansible-dellemc-unity/teams/experts))

To merge code into the master at least one of [reviewers](https://github.com/orgs/ansible-dellemc-unity/teams/reviewers) should approve your changes

Confirm checklist:
- [ ] Unit tests are successfully passed (till they doesn't exists could be unchecked)
- [ ] All exists test playbooks are successfully works

If you have added new functionality (submodule)
- [ ] Unit tests for submodule are added
- [ ] Playbooks that demonstrate work of submodule are added
- [ ] CI tests for submodule are added (could be unchecked till CI process haven't created)
