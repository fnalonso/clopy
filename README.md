### Introduction

This repository contains a python implementation for interesting functions from clojure.


### Installation

```shell script
python setup.py install
```


### Functions


#### get_in

Walks through a sequence of keys inside dictionary.
If key is missing returns the default value set and the key
else returns the value for the last key in keys.

Inspired on: https://clojuredocs.org/clojure.core/get-in

Definition

``def get_in(dictionary: Dict, keys: List[Hashable], default_value=None) -> Tuple[Optional[Hashable], Optional[Any]]``

Example:

```python
from clopy.functions import get_in

my_nested_dict = {
                    'my': {
                        'super': {
                            'nested': {
                                'dict': {
                                    'with': 'Hello!'
                                }
                            }
                        }
                    }
                }

# Success
get_in(my_nested_dict, ['my', 'super', 'nested', 'dict', 'with'], 'Not found!')
# (None, "Hello!")

# Failure
get_in(my_nested_dict, ['my', 'super', 'needed', 'nested', 'secret'])
# ("needed", None)
```