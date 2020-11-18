from typing import Dict, List, Hashable, Tuple, Any, Optional


def get_in(dictionary: Dict, keys: List[Hashable], default_value=None) -> Tuple[Optional[Hashable], Optional[Any]]:
    """
    Walks through a sequence of keys inside dictionary.
    If key is missing returns the default value set and the key
    else returns the value for the last key in keys.

    Ref: https://clojuredocs.org/clojure.core/get-in

    Example::

        $ my_nested_dict = {
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
        $ get_in(my_nested_dict, ['my', 'super', 'nested', 'dict', 'with'], 'Not found!')
        > (None, Hello!)

        # Failure
        $ get_in(my_nested_dict, ['my', 'super', 'needed', 'nested', 'secret'])
        > ('needed', None)


    :param dictionary: Dict to search
    :param keys: keys containing the path inside the dictionary
    :param default_value: Value to be return if a key is not found
    :return: if success Tuple(None, Value) else (key, None)
    """
    for key in keys:
        dictionary = dictionary.get(key)
        if not dictionary:
            return key, default_value
    return None, dictionary
