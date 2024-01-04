import json
import requests

from card import Card


def _card_list_search(link):
    """Send Scryfall Request and Return A CardList object"""
    response = requests.get(link)
    response = response.content.decode('utf8')
    data = json.loads(response)
    if 'status' not in data.keys():
        card_list = []
        for card in data['data']:
            card_list.append(Card(card))
        return card_list
    else:
        raise Exception(f'No Cards Found With Parameter at link {link}')


def _card_search(link):
    """Send Scryfall Request and Return A Card object"""
    response = requests.get(link)
    response = response.content.decode('utf8')
    data = json.loads(response)
    if 'status' not in data.keys():
        card = data['data'][0]  # The first result in the returned card list
        return card
    else:
        raise Exception(f'No Cards Found With Parameter at link {link}')


def random_card():
    """Return a random card as a Card object"""
    response = requests.get('https://api.scryfall.com/cards/random')
    response = response.content.decode('utf8')
    data = json.loads(response)
    return Card(data)


def get_card(card_name):
    """Return a Card Object for a card with the exact given name"""
    return _card_search(f'http://api.scryfall.com/cards/search?q=!"{card_name}"')

# Search Methods // Lists

def name_search(card_name):
    """Return a CardList of all results with name search"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=name={card_name}')


def oracle_search(oracle_text):
    """Return a CardList of all results with oracle text search"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=o="{oracle_text}"')

def type_search(card_type):
    """Return a CardList of all results with the type or subtype given"""
    if isinstance(card_type, list):
        card_type_search = ''
        for mtg_type in card_type:
            card_type_search += f'type={mtg_type} AND '
        card_type_search = card_type_search[:-5]
    elif isinstance(card_type, str):
        card_type_search = f'type={card_type}'
    return _card_list_search(f'http://api.scryfall.com/cards/search?q={card_type_search}')

def color_search(colors, search_type='exact'):
    """Return a CardList of all results with color search"""
    if search_type == 'exact':
        oper = '='
    elif search_type == 'at least':
        oper = '>='
    elif search_type == 'at most':
        oper = '<='
    elif search_type == 'up to':
        oper = '<'
    elif search_type == 'more than':
        oper = '>'
    else:
        raise LookupError(f'Invalid color search type {search_type}')
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=color{oper}"{colors}"')

def color_identity_search(colors):
    """Return a CardList of all results with the given color identity"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=commander={colors}"')

def mana_value_search(mana_value, search_type='exact'):
    """Return a CardList of all results with the given mana value"""
    if search_type == 'exact':
        oper = '='
    elif search_type == 'at least':
        oper = '>='
    elif search_type == 'at most':
        oper = '<='
    elif search_type == 'up to':
        oper = '<'
    elif search_type == 'more than':
        oper = '>'
    else:
        raise LookupError(f'Invalid mana value search type {search_type}')
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=mv{oper}{mana_value}"')

def power_search(power, search_type='exact'):
    """Return a CardList of all results with the given power"""
    if search_type == 'exact':
        oper = '='
    elif search_type == 'at least':
        oper = '>='
    elif search_type == 'at most':
        oper = '<='
    elif search_type == 'up to':
        oper = '<'
    elif search_type == 'more than':
        oper = '>'
    else:
        raise LookupError(f'Invalid power search type {search_type}')
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=power{oper}{power}"')

def toughness_search(toughness, search_type='exact'):
    """Return a CardList of all results with the given toughness"""
    if search_type == 'exact':
        oper = '='
    elif search_type == 'at least':
        oper = '>='
    elif search_type == 'at most':
        oper = '<='
    elif search_type == 'up to':
        oper = '<'
    elif search_type == 'more than':
        oper = '>'
    else:
        raise LookupError(f'Invalid toughness search type {search_type}')
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=toughness{oper}{toughness}"')

def loyalty_search(loyalty, search_type='exact'):
    """Return a CardList of all results with the given loyalty"""
    if search_type == 'exact':
        oper = '='
    elif search_type == 'at least':
        oper = '>='
    elif search_type == 'at most':
        oper = '<='
    elif search_type == 'up to':
        oper = '<'
    elif search_type == 'more than':
        oper = '>'
    else:
        raise LookupError(f'Invalid loyalty search type {search_type}')
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=loy{oper}{power}"')

def set_search(set):
    """Return a CardList of all results from a given set"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=set={set}')


def advanced_search(arguments):
    """Return a CardList of all results with advanced argument search (using Scryfall args)"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q={arguments}')


def get_printings(card):
    """Return a CardList of all other versions of an inputted Card object"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=%21"{card.name()}"+include%3Aextras&unique=prints')