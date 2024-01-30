import json
import sys
from typing import Any, Dict, Generator, Iterable, Mapping, Sequence


def json_chucked_in_num_bytes_fancy(json_body: Iterable, num_bytes: int) -> Generator[Dict, Any, None]:
    iterator = iter(json_body)
    first_element = next(iterator)

    if isinstance(json_body, Mapping):
        sub_body = {first_element: json_body[first_element]}  # Start with first populated
        for next_element in iterator:
            sub_body_part = {next_element: json_body[next_element]}
            if (sys.getsizeof(json.dumps(sub_body)) + sys.getsizeof(json.dumps(sub_body_part))) > num_bytes:
                yield sub_body
                sub_body = {}
            sub_body.update(sub_body_part)
        yield sub_body
    else:
        sub_body = [first_element]  # Start with first populated
        for next_element in iterator:
            if (sys.getsizeof(json.dumps(sub_body)) + sys.getsizeof(json.dumps(next_element))) > num_bytes:
                yield json.dumps(sub_body)
                sub_body = []
            sub_body.append(next_element)
        yield json.dumps(sub_body)


def json_chucked_in_num_elements(json_body: dict, num_elements: int) -> Generator[Dict, Any, None]:
    return (json_body[i : i + num_elements] for i in range(0, len(json_body), num_elements))


def json_seq_chunked_in_num_bytes(json_body: Sequence, num_bytes: int) -> Generator[Dict, Any, None]:
    iterator = iter(json_body)
    first_element = next(iterator)
    sub_body = [first_element]  # Start with first populated
    for next_element in iterator:
        if (sys.getsizeof(json.dumps(sub_body)) + sys.getsizeof(json.dumps(next_element))) > num_bytes:
            yield json.dumps(sub_body)
            sub_body = []
        sub_body.append(next_element)
    yield json.dumps(sub_body)


if __name__ == "__main__":
    s = iter(json_chucked_in_num_bytes_fancy({"a": 1, "b": 2}, 30 * 1024 * 1024))
    for a in s:
        print(a)

    asd = [{"a": 1, "b": 2}, {"c": 3}]
    print(sys.getsizeof(json.dumps(asd)))
    s = iter(json_chucked_in_num_bytes_fancy(asd, 40))
    for a in s:
        print(a)

    print(isinstance({1: 2}, Sequence))

    s = iter(json_seq_chunked_in_num_bytes(asd, 40))
    for a in s:
        print(a)
