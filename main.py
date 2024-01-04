import scrypy
import card
import time

def main():
    lines = []
    input_file = open("cardlist.csv", "r")
    for line in input_file:
        lines.append(line.strip().split(','))
    input_file.close()

    cards = []
    index = 1
    for line in lines:
        if 'z' in line[1]:
            time.sleep(.1)
            cards.append([scrypy.advanced_search(f'set:{line[0]} cn:"{line[1][:-1]}"')[0], scrypy.advanced_search(f'set:{line[0]} cn:"{line[1]}"')[0]])
            print(index, line[0], line[1])
            index += 1


    output_file = open("output.csv", "w")
    for card in cards:
        normal_price = None
        if card[0].prices()['usd'] == None:
            normal_price = card[0].prices()['usd_foil']
        else:
            normal_price = card[0].prices()['usd']
        if normal_price is not None and card[1].prices()['usd_foil'] is not None:
            my_string = f"{card[0].name().replace(',', '')}, {card[0].set_code()}, {normal_price}, {card[1].prices()['usd_foil']}\n"
            output_file.write(my_string)

    output_file.close()

main()