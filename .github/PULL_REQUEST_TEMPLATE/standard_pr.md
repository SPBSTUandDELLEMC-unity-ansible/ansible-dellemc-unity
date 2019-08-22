Before you are open PR be shure that your changes doesn't brake any other code in reposytory: run playbooks from playbooks/test.
Add your own playbooks for testing your changes.

Check that your code works, please, don't ask review of WIP PRs (we can help you and will review code if you directly ask us about it @ansible-dellemc-unity/experts [experts](https://github.com/orgs/ansible-dellemc-unity/teams/experts))

To merge code to the master branch at least one of [reviewers](https://github.com/orgs/ansible-dellemc-unity/teams/reviewers) should approve your changes

- [ ] Unit tests are successfully passed (till they doesn't exists could be uchecked)
- [ ] All exists test playbooks are successfully works

If you have added new functionality (submodule)
- [ ] Unit tests for submodule are added
- [ ] Playbooks that demonstrate work of submodule are added
- [ ] CI tests for submodule are added
