# Steps

1. Ensure you have tar, make, and the aws cli [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration) before beginning.

2 Download the dataset from s3 using `make pull`. You man clean up after this task by running `make clean`

3. Ensure you have installed python3 (tested with 3.7.0), have sourced a virtualenv, and have installed the deps from requirements.txt.

4. Make replay executable with `chmod +x ./replay`` 

5. You should now be able to run commands with replay which follow the same patterns from the `energyhub-code-sample.md` description.
