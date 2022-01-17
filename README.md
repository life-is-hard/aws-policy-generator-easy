# aws-policy-generator-easy
Making AWS IAM policy easy by giving the ability to provide high level human understandable action words, and converting them to actual IAM JSON policy.

This makes developer's life easy by giving them human understandable terms instead of complicated AWS Action terms.

**Faster dev turn arounds = _PROFIT_**

## Running the code
`python .\generator\main.py`

## Idea behind it
There would be input given in the form of CSV file - as depected by `inputs` variable

There are predefined mapping (`mapping` variable) that is provided which will convert the input to actual action.

## TODO
- Make this into a moduler function
- Have the ability to run this on lambda followed by API gateway
