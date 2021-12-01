# -*- coding: utf-8 -*
import json 

def parse(query: str):

    return json.loads(query)

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'cat', 'color': 'black'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'bog', 'color': 'red'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'mouse', 'color': 'green'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'hourse', 'color': 'pink'}
    assert parse('http://example.com/?name=Dima') == {'name': 'John'}
    assert parse('http://example.com/?name=Dima') == {'name': 'Hugh'}
    assert parse('http://example.com/?name=Dima') == {'name': 'Britney'}
    assert parse('http://example.com/?name=Dima') == {'name': 'Gregg'}
    


def parse_cookie(query: str):
    
    return json.loads(query)


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('name=Dima;') == {'name': 'John'}
    assert parse_cookie('name=Dima;') == {'name': 'Hugh'}
    assert parse_cookie('name=Dima;') == {'name': 'Britney'}
    assert parse_cookie('name=Dima;') == {'name': 'Gregg'}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'John', 'age': '35'}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Hugh', 'age': '38'}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Britney', 'age': '40'}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Gregg', 'age': '25'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'John=Admin', 'age': '35'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Gregg=User', 'age': '25'}