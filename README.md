# Validate a phone number

A [Supercode](http://gosupercode.com) function that validates a phone number and formats it according to E164 format.

## Usage

[Supercode](http://gosupercode.com) SDK will be available after the launch.

```
import supercode
import pprint

country_code = 'PH'
phone_number = '09555555555'

response = supercode.call(
    "super-code-function",
    "your-supercode-api-key",
    country_code,
    phone_number)

pprint(response)
```

**Note:** Supercode has not been launched yet. This is for internal testing only.
